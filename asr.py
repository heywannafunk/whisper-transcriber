import whisper
import pyaudio
import wave
import time

def get_wav_length(filename):
    with wave.open(filename, 'r') as wav_file:
        framerate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        duration = num_frames / framerate
    return duration

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

print('recording...\nctrl+c to stop')
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

time_str = str(time.time())
audio_filename = time_str + "_audio.wav"
transription_filename = time_str + "_transription.txt"
print('writing audio file...')
sound_file = wave.open(audio_filename, "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()


print('transcribing...')
model = whisper.load_model("base")

start_time = time.time()
result = model.transcribe(audio_filename)
end_time = time.time()
execution_time = end_time - start_time

print(f'file length: {get_wav_length(audio_filename)} seconds\ntranscribed in: {execution_time} seconds')
print(result["text"])

with open(transription_filename, 'w') as file:
    file.write(result["text"])
print(f'transcription successfully written to file {transription_filename}')

print('program cycle complete, press ctrl+c to exit')
try:
    while True:
        pass
except KeyboardInterrupt:
    pass