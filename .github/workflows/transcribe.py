import os
import sys
from google.cloud import speech

def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    transcription = ''
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <audio-file-path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    transcription = transcribe_audio(audio_path)

    output_path = os.path.splitext(audio_path)[0] + '.txt'
    with open(output_path, 'w') as output_file:
        output_file.write(transcription)

    print(f"Transcription saved to {output_path}")
