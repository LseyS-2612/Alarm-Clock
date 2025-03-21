Certainly! Below is the updated README with the **"How to Use"** section edited to remove the second point about creating the Python script.

---

# Simple Alarm Clock using `playsound` (Minutes and Seconds Only)

This is a beginner-friendly Python alarm clock project that plays an alarm sound at a specified time, based on minutes and seconds. The alarm will go off once the system's time matches the user-set minutes and seconds. The project uses the `playsound` library to play the alarm sound.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed on your system
- A basic understanding of Python syntax
- An audio file (MP3) that will be played as the alarm sound

## Installation

1. **Install `playsound` Library:**

   To install the `playsound` library, open your command prompt or terminal and run:

   ```bash
   pip install playsound
   ```

2. **Prepare an MP3 File:**

   You will need an MP3 file to play as the alarm sound. Download or create an MP3 file (for example, `alarm.mp3`) and save it in the same directory as the Python script (or specify the file path in the script).

   Example: `mixkit-classic-alarm-995.mp3`

## How to Use

1. **Clone or Download the Project Files:**

   You can clone this repository or download the project files directly.

2. **Run the Script:**

   Once everything is set up, run the Python script:

   ```bash
   
   python Alarm-Clock.py
   
   ```

   The script will prompt you to enter the **minutes** and **seconds** for the alarm. For example, you might set it to `07` minutes and `30` seconds. When the current system time matches your set alarm time, the audio file will play, and the alarm will go off.

Here’s what you’ll see in your terminal when the script runs:

```text
Alarm will sound in: 00:00
```

## Troubleshooting

1. **Alarm not playing:**
   - Ensure the file path to the MP3 is correct.
   - Ensure that the MP3 file is in the same directory as the script or specify the correct file path in the code.

2. **ModuleNotFoundError:**
   - If you receive an error like `ModuleNotFoundError: No module named 'playsound'`, it means the `playsound` module is not installed. Install it using `pip install playsound`.

3. **Time format mismatch:**
   - Make sure you enter the alarm time in the correct format: **minutes** and **seconds** (e.g., `07` minutes and `30` seconds).

## Future Improvements

- Add functionality to set multiple alarms.
- Allow users to snooze the alarm for a few minutes.
- Add a graphical user interface (GUI) for a more interactive experience.
- Set custom alarm sounds based on user preferences.
