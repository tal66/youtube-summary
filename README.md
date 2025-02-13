## Video Summary

Summarize Youtube videos in the terminal fast and simple. Great results.


## Run

```bash
python main.py "<video_url>"
```

## Install

```bash
pip install yt-dlp python-dotenv requests
```

Also install AI deps of your choice:
```bash
pip install google-genai openai
```
(add keys in `.env`: `OPENAI_API_KEY`, `GEMINI_KEY`)

## Output Examples


<details>
<summary>Veritasium: The Most Important Algorithm Of All Time
</summary>

```

### The Most Important Algorithm Of All Time
### Veritasium

**Executive Summary:**

*   **Purpose:** The video explains the significance of the Fast Fourier Transform (FFT), highlighting its wide range of applications, its role in a critical historical juncture (nuclear test ban treaty), and its earlier, largely unknown discovery by Gauss.
*   **Main Takeaways:**
    *   The FFT is a crucial algorithm used in countless technologies involving signal processing (radar, sonar, video compression, etc.).
    *   The FFT could have potentially prevented the nuclear arms race if its development had been faster and its capabilities been applied earlier.
    *   The discovery of FFT was made well before its widespread adoption, and had it been applied earlier, would change the course of events.
    *   It is important to consider how you can make a positive impact with your career.

**Section Summaries:**

1.  **Introduction (0:00-0:30):**

    *   The video introduces the Fast Fourier Transform (FFT) as one of the most important algorithms of all time.
    *   Highlights its common usage in technologies like radar, sonar, 5G, and WiFi.
    *   Teases the idea that the FFT's development could have potentially altered the course of the nuclear arms race.
2.  **The Nuclear Arms Race and Test Ban Treaty (0:30-4:30):**

    *   Describes the initial willingness of the U.S. to negotiate about nuclear weapons decommissioning.
    *   Explains the Soviet rejection of the Baruch Plan, leading to the arms race.
    *   Details the effects of nuclear testing and public outcry, leading to talks of a comprehensive test ban.
    *   Highlights the difficulty in verifying compliance with an underground testing ban.
3.  **The Problem of Detection and the Fourier Transform (4:30-7:30):**

    *   Focuses on the challenge of distinguishing underground nuclear tests from earthquakes using seismometers.
    *   Introduces the concept of the Fourier Transform as a method to analyze the frequency components of seismometer signals.
    *   Explains that the goal was to determine the characteristics of an explosion (yield, depth) from the signal.
4.  **How Fourier Transforms Work (7:30-11:00):**

    *   Explains, in layman's terms, how Fourier Transforms decompose a signal into sine waves of different frequencies.
    *   Illustrates how multiplying a signal by a sine wave can reveal the presence and amplitude of that frequency within the signal.
    *   Mentions the use of Euler's formula for combining sine and cosine amplitudes.
5.  **The Discrete Fourier Transform (DFT) (11:00-15:00):**

    *   Explains the difference between idealized Fourier Transforms and Discrete Fourier Transforms (DFTs) for real-world signals.
    *   Describes how the frequency spectrum of a DFT is also discreet and finite.
    *   Explains the relationship between the number of samples, spacing, and frequency resolution in DFTs.
    *   Provides a simple example of calculating a DFT with eight samples.
6.  **The Need for a "Fast" Fourier Transform (15:00-16:30):**

    *   Highlights the computational burden of standard DFTs, requiring N-squared complex multiplications.
    *   Explains why this was too slow for analyzing large amounts of seismometer data with 1960's technology.
    *   Sets the stage for the introduction of the Fast Fourier Transform (FFT) as a solution.
7.  **The Discovery of the FFT (16:30-18:00):**

    *   Describes the discovery of the FFT algorithm by John Tukey at a meeting of the President's Science Advisory Committee.
    *   Emphasizes the significant speed improvement offered by the FFT over the traditional DFT.
8.  **How the FFT Works (18:00-21:30):**

    *   Explains, simplistically, how the FFT exploits symmetries in sinusoidal functions to reduce the number of calculations.
    *   Illustrates the process of splitting samples into even and odd index points to identify redundant calculations.
    *   Mentions that calculations scales as Nlog base two of N, compared to N squared in the DFT.
9.  **The Aftermath and Gauss's Prior Discovery (21:30-24:30):**

    *   Explains that the FFT's use came too late to prevent the nuclear arms race.
    *   Reveals that Carl Friedrich Gauss had developed the FFT algorithm a century and a half earlier but it went largely unnoticed because of how and where he published it.
    *   Poses the question of how history might have changed if Gauss's discovery had been widely adopted earlier.
10. **Modern Applications and the FFT's Significance (24:30-27:00):**

    *   Briefly touches on how FFTs are now used to compress images, like ones that you watch on the video.
    *   Lists numerous modern applications of FFTs, emphasizing their importance in signal processing.
    *   Quotes mathematician Gilbert Strang calling the FFT the most important numerical algorithm of our lifetime.
11. **Sponsor Segment (27:00-End):**

    *   Announces the video's sponsor, 80,000 Hours, a nonprofit that helps people find impactful careers.
    *   Describes how 80,000 Hours provides resources and advice for those who want to make a positive difference in the world with their careers.
    *   Encourages viewers to check out the 80,000 Hours website.

```

</details>

<br>

<details>
<summary>Lex Fridman: A day in my life
</summary>
    
```
## A day in my life | Lex Fridman
## Lex Fridman

Here's a summary of the video transcript, broken into sections with main ideas and an executive summary:

**Executive Summary**

*   **Purpose:**  The video aims to provide viewers with a detailed look into the daily routine of the speaker (Lex Fridman), focusing on his time management strategies and habits to maximize productivity.
*   **Main Takeaways:**
    *   **Structured Routine:**  A highly structured day with dedicated blocks for deep work, exercise, learning, and even leisure.
    *   **Mantra & Visualization:**  A morning mantra ritual to set intentions, focus on goals, and cultivate gratitude.
    *   **Focus & Discipline:**  Emphasis on deep work sessions with minimal distractions, disciplined use of social media, and consistent exercise.
    *   **Balance & Self-Reflection:** Importance of balancing hard work with personal passions, gratitude, and reflection on history and the nature of good and evil.

**Sections and Main Ideas**

1.  **Introduction (0:00 - 0:15):**
    *   Addressing requests to share a "day in the life" focusing on time management and productivity.
    *   Promises to outline a typical routine.

2.  **Morning Routine: Sleep & Sponsors (0:15 - 0:50):**
    *   Prioritizes 6-8 hours of sleep and emphasizes the importance of sleep, diet, and exercise for productivity.
    *   Acknowledges podcast sponsors (e.g., AC bed) and encourages viewers to support them.

3.  **Morning Routine: The Mantra (0:50 - 6:00):**
    *   Starts the day with a structured mantra/ritual:
        *   **Rules/Constraints:**  Reminds himself of rules regarding social media use (limited to posting), diet (keto), and exercise (daily).
        *   **Gratitude:** Meditates on being alive.
        *   **5-Year Goals:** Lists ambitious long-term goals.
        *   **End of Year Goals:** Lists reachable goals for the year.
        *   **Daily Visualization:**  Visualizes the day's tasks and struggles, focusing on timing and successful completion.
        *   **Principles:**  Recites principles centered around compassion, empathy, love, character, integrity, and strength.

4.  **Deep Work Session 1 (6:00 - 9:00):**
    *   Begins with a 4-hour deep work session focused on a single task (Tensorflow Lite).
    *   Strictly limits interruptions to water, coffee, and bathroom breaks, writing down other ideas to focus on later.
    *   Uses a standing desk and kinesis keyboard. Describes the work as difficult but necessary, and finds joy in completing it.

5.  **Social Media, Music & Exercise Prep (9:00 - 11:00):**
    *   Posts a podcast and checks social media for a maximum of 10 minutes.
    *   Plays guitar for relaxation and enjoyment.
    *   Prepares for a long run/exercise.

6.  **Exercise (11:00 - 15:00):**
    *   Goes for a run (minimum 6 miles), listening to brown noise initially and then an audiobook (The Rise and Fall of the Third Reich).
    *   Incorporates David Goggins-inspired "nickel and dime" workout (5 pull-ups, 10 push-ups every minute).
    *   Emphasizes fasted exercise for mental clarity and physical performance.

7.  **Exercise Reflections (15:00 - 17:00):**
    *   Details the exercise session: 7-mile run and 20 minutes of nickel and dimes.
    *   Reflects on the audiobook's content about Nazi Germany and the nature of evil.

8.  **Shower & Transition to Deep Work 2 (17:00 - 19:00):**
    *   Takes a cold shower, using a song to mark the 1-minute mark.
    *   Prepares for the second 4-hour deep work session, considering what to focus on based on the morning session's progress.

9.  **Deep Work Session 2 (19:00 - 22:00):**
    *   Commences the second 4-hour session, continuing the Tensorflow Lite work.
    *   May skip a meal during this session due to intermittent fasting.
    *   Reiterates the importance of discipline and perseverance during challenging tasks.

10. **Breaking the Fast (22:00 - 25:00):**
    *   Breaks the fast with Athletic Greens.
    *   Describes his typical meal: meat (ground beef) and vegetables (cauliflower).
    *   Discusses electrolytes (sodium, magnesium, potassium) and fish oil supplements.

11. **Lunch Prep & Relaxed Work Planning (25:00 - 28:00):**
    *   Quickly prepares the meal.
    *   Plans the third 4-hour session: email, video editing, and continuing deep work (Tensorflow).

12. **Work, Email, & Potential for Chaos (28:00 - 31:00):**
    *   Executes the third 4-hour session, balancing focused work with email management and video editing.
    *   Acknowledges the potential for randomness and adventure later in the day.

13. **Paper and Book Reading (31:00 - 33:00):**
    *   Completes the four hour work session; reflects that despite not being perfect, the day was successful.
    *   Plans to read papers and research for the next hour and then switch to book reading.

14. **Reading (33:00 - 36:00):**
    *   Spends one hour reading scientific papers, focusing on deep understanding and asking deeper questions.
    *   Spends another hour reading Dostoyevsky, preparing for upcoming conversations with translators, and considering the language and meaning.

15. **Gratitude & Closing (36:00 - 39:00):**
    *   After the hour of literature reading, takes a pause for gratitude.
    *   Ends the day by drifting to sleep while continuing to read.
    *   Expresses gratitude, emphasizing the value of hard work, love, and compassion.
    *   Encourages viewers to subscribe and support the podcast.

```

</details>

## Note

The summary is generated by AI models and may contain inaccuracies and hallucinations.
The purpose of this project is to provide a quick summary of the video content. This will never replace watching the video and absorbing the full context.