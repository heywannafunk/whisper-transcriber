# Audio Recorder and Transcriber

This project records audio from your microphone, saves it as a WAV file, and then transcribes the audio using the Whisper model from OpenAI.

## Features

- Records audio in real-time using the PyAudio library.
- Saves recorded audio in WAV format.
- Transcribes the audio using the Whisper model.
- Outputs the transcription to a text file.

## Requirements

- Python 3.x
- `pyaudio` for audio recording
- `whisper` for transcription
- `wave` for handling WAV files

## Installation

To set up the environment and install the required packages, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install pyaudio openai-whisper
   ```

## Usage

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Start recording by speaking into your microphone. The program will capture audio until you press `Ctrl+C`.

3. Once you stop the recording, the audio will be saved as a WAV file, and the transcription will be generated and saved in a text file.

## Output Files

- **Audio File**: Saved in the format `timestamp_audio.wav`
- **Transcription File**: Saved in the format `timestamp_transcription.txt`

Both files will be located in the same directory as the script.

## Example Output

When you run the script, you will see output similar to the following:

```
recording...
ctrl+c to stop
writing audio file...
transcribing...
file length: 10.5 seconds
transcribed in: 3.2 seconds
Your transcribed text goes here.
transcription successfully written to file timestamp_transcription.txt
program cycle complete, press ctrl+c to exit
```
