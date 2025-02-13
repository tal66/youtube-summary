import logging
import os
import re
import sys
import urllib.parse as urlparse
from dataclasses import dataclass
from pathlib import Path

import requests
from dotenv import load_dotenv
from yt_dlp import YoutubeDL

load_dotenv()
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

OUT_DIR = Path(__file__).parent / "out_files"
OUT_DIR.mkdir(exist_ok=True)
logger.info(f"OUT_DIR: {OUT_DIR}")


########### transcript


def get_transcript(vi: "VideoInfo") -> str:
    """
    get transcript from url, unless already saved as file.
    """

    result_transcript_fname = f"{OUT_DIR}/{vi.video_id}_subs.txt"
    # try saved file
    if Path(result_transcript_fname).exists():
        transcript = Path(result_transcript_fname).read_text()
        logger.info(f"used saved transcript: {result_transcript_fname}")
        return transcript

    subs_options = _get_subs_options(vi)
    subs_ext_dict = {item["ext"]: item["url"] for item in subs_options}

    if "vtt" in subs_ext_dict:
        subs_url = subs_ext_dict["vtt"]
        response = requests.get(subs_url)
        if response.status_code == 200:
            vtt_data = response.text
            transcript = _get_transcript_from_vtt(vtt_data)

            # save
            Path(result_transcript_fname).write_text(transcript)
            logger.info(f"save transcript to {result_transcript_fname}")
            return transcript
        else:
            logger.info(f"Error: {response.status_code}")
    else:
        logger.info(f"No vtt subtitles found. write parser for other formats: {subs_ext_dict.keys()}")
    return ""


def _format_hhmmss(seconds):
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def to_chapters_str(chapters) -> str:
    chapter_str = ""
    for chapter in chapters:
        start_time = chapter["start_time"]
        start_time_f = _format_hhmmss(start_time)
        title = chapter["title"]
        chapter_str += f"{start_time_f} {title}\n"
    return chapter_str


def _get_transcript_from_vtt(vtt_data):
    timestamp_pattern = r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}"
    text_list = []
    in_caption = False
    for line in vtt_data.splitlines():
        if in_caption:
            if line.strip() == "":
                in_caption = False
            else:
                if "</c>" in line:  # sometimes heb subs are messed up
                    continue
                if text_list and (line == text_list[-1]):
                    continue
                text_list.append(line)
        if re.match(timestamp_pattern, line):
            vtt_data = vtt_data.replace(line, "")
            in_caption = True

    transcript = "\n".join(text_list)
    return transcript.strip()


def _get_subs_options(vi: "VideoInfo") -> list[dict]:
    if not vi.language:
        logger.warning("no language found. set default languages.")
        languages = ["iw", "en", "en-US", "en-GB"]
    else:
        languages = [vi.language]

    if "en" not in languages:  # sometimes 'en-US' but need 'en', good fallback anyway
        languages.append("en")

    for language in languages:
        orig_lang = f"{language}-orig"  # happens

        if language in vi.subtitles_d:
            logger.info(f"subtitles in: {language}")
            return vi.subtitles_d[language]
        else:
            if language in vi.automatic_captions_d:
                logger.info(f"automatic_captions in: {language}")
                return vi.automatic_captions_d[language]
            elif orig_lang in vi.automatic_captions_d:
                logger.info(f"automatic_captions in: {orig_lang}")
                return vi.automatic_captions_d[orig_lang]
            else:
                logger.warning(f"no subtitles found (language: {language}).")

    return []


########### models

DEFAULT_PROMPT_PREFIX = (
    "Summarize this video transcript. "
    "Break into sections and include main ideas from each section."
    "Add executive summary: what is the purpose of the video? what are the main takeaways?"
)
DEFAULT_PROMPT_PREFIX_OPENAI = (
    "Summarize this video transcript. "
    "Break into sections and include main ideas from each section. Elaborate. "
    "Add executive summary: what is the purpose of the video and main takeaways?"
)


def ask_openai(video_str, prompt_prefix=DEFAULT_PROMPT_PREFIX_OPENAI) -> str:
    logger.info("get openai summary..")
    from openai import OpenAI

    if not os.getenv("OPENAI_API_KEY"):
        logger.error("OPENAI_API_KEY is not set")
        return ""

    client = OpenAI()
    prompt = f"{prompt_prefix}\n\n{video_str}"

    # get
    completion = client.chat.completions.create(model="gpt-3.5-turbo", store=True,
                                                messages=[{"role": "user", "content": prompt}])

    msg = completion.choices[0].message
    msg_content = msg.content

    usage = completion.usage
    logger.info(f"prompt_tokens: {usage.prompt_tokens}, completion_tokens: {usage.completion_tokens}")
    return msg_content


def ask_gemini(video_str, prompt_prefix=DEFAULT_PROMPT_PREFIX) -> str:
    logger.info("get gemini summary..")
    from google import genai

    key = os.getenv("GEMINI_KEY")
    if not key:
        logger.error("GEMINI_KEY is not set")
        return ""

    client = genai.Client(api_key=key)

    # prompt
    prompt = f"{prompt_prefix}\n\n{video_str}"

    # get
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    return response.text


def ask_private_endpoint(video_str, prompt_prefix=DEFAULT_PROMPT_PREFIX) -> str:
    # TODO
    endpoint = ""
    return ""


# for simplicity not using interfaces
AI_FUNC_DICT = {"openai": ask_openai, "gemini": ask_gemini, "private_endpoint": ask_private_endpoint}


#################


@dataclass
class VideoInfo:
    video_id: str = ""
    title: str = ""
    channel: str = ""
    duration: int = 0
    duration_string: str = ""
    chapters: list = None
    upload_date: str = ""
    language: str = ""
    subtitles_d: dict = None
    automatic_captions_d: dict = None
    transcript: str = ""

    @classmethod
    def new(cls, yt_info_dict):
        upload_date = yt_info_dict.get("upload_date", "")
        vi = VideoInfo(
            title=yt_info_dict.get("title", ""),
            video_id=yt_info_dict.get("id", ""),
            channel=yt_info_dict.get("uploader", ""),
            duration=yt_info_dict.get("duration", 0),
            duration_string=yt_info_dict.get("duration_string", ""),
            chapters=yt_info_dict.get("chapters", []),
            upload_date=f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}",
            language=yt_info_dict.get("language", ""),
            subtitles_d=yt_info_dict.get("subtitles", {}),
            automatic_captions_d=yt_info_dict.get("automatic_captions", {}),
        )
        return vi


def get_summary(ai_provider: str, vi: VideoInfo) -> str:
    if ai_provider not in AI_FUNC_DICT:
        logger.error(f"AI provider not found: {ai_provider}. options: {AI_FUNC_DICT.keys()}")
        return ""

    if len(vi.transcript) > 100_000:
        # ask user
        ans = input(f"transcript is very long ({len(vi.transcript)}). continue? [y]/n: ")
        ans = ans.strip()
        if ans and (ans.lower() != "y"):
            print("abort")
            return ""

    # get
    func = AI_FUNC_DICT.get(ai_provider)
    ai_result = func(vi.transcript)

    # save
    title_sanitized = re.sub(r"[^\w\s\-\(\)\[\]]", "_", vi.title)
    f = f"{OUT_DIR}/{vi.video_id}__{vi.channel[:30]}_{title_sanitized[:40]}.{ai_provider}.md"
    Path(f).write_text(f"## {vi.title}\n## {vi.channel}\n\n{ai_result}")

    logger.info(f"summary saved to {f}")
    return ai_result


########### out


def highlight_bold(text):
    RESET = "\033[0m"
    UNDERLINE = "\033[4m"
    return re.sub(r"\*\*(.*?)\*\*", rf"{UNDERLINE}\1{RESET}", text)


###########

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Get video summary",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("youtube_url", type=str, help="youtube url")
    parser.add_argument("-t", "--transcript-only", action="store_true", help="transcript only, no summary")
    parser.add_argument("-a", "--ai_provider", type=str, default="gemini",
                        help=f"AI provider: {",".join(AI_FUNC_DICT.keys())}")
    parser.add_argument("-v", action="store_true", help="verbose")
    # maybe in the future
    # parser.add_argument("-o", ...)
    args = parser.parse_args()

    youtube_url = args.youtube_url

    BASE_URL = "https://www.youtube.com"
    if not youtube_url.startswith(BASE_URL):
        logger.error("invalid youtube url")
        sys.exit(1)

    if args.v:
        logger.setLevel(logging.INFO)

    if not youtube_url.startswith(f"{BASE_URL}/shorts"):
        # keep just video id (avoid problems with extra params)
        youtube_url_video_id = urlparse.parse_qs(urlparse.urlparse(youtube_url).query)["v"][0]
        youtube_url = f"{BASE_URL}/watch?v={youtube_url_video_id}"

    logger.info(f"youtube_url: {youtube_url}")
    with YoutubeDL({"quiet": True, "no_warnings": True, "verbose": False}) as ydl:
        yt_info_dict = ydl.extract_info(youtube_url, download=False)

    # video_info
    vi = VideoInfo.new(yt_info_dict)
    video_str = f"\n{vi.title}\n{vi.channel} | duration {vi.duration_string} | {vi.upload_date}"
    logger.info(video_str)
    if vi.chapters:
        chapters_str = to_chapters_str(vi.chapters)
        video_str += f"\n{chapters_str}"

    print(video_str)

    # transcript
    transcript = get_transcript(vi)
    if transcript:
        vi.transcript = transcript
        t_print = f"\n\n{transcript}"

        if args.transcript_only:
            print(t_print)
        else:
            video_str += t_print
            provider = args.ai_provider
            ai_result = get_summary(provider, vi)

            colored_text = highlight_bold(ai_result)
            print(f"\n\n{colored_text}\n")
