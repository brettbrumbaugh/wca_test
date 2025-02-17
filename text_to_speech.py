
# Assisted by watsonx Code Assistant 
import argparse
import os
from google.cloud import texttospeech
from google.cloud.texttospeech import enums
from google.cloud.texttospeech import types

def generate_audio(text):
    """Generates audio from the given text."""
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = types.AudioConfig(
        audio_encoding=enums.AudioEncoding.LINEAR16)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.wav', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate audio from .txt file.')
    parser.add_argument('file', type=str, help='Path to .txt file')
    args = parser.parse_args()

    text = ' '.join(line.strip() for line in open(args.file))
    generate_audio(text)
