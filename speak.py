import time, sys, os
from pygame import mixer
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

def speak(text):
	mixer.init()

	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'modified-keep-352519-6f1cc9c75c52.json'
	client = texttospeech_v1.TextToSpeechClient()

	synthesis_input = texttospeech_v1.SynthesisInput(text=text)

	voice = texttospeech_v1.VoiceSelectionParams(
		language_code="en-ca",
		ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
	)

	audio_config = texttospeech_v1.AudioConfig(
		audio_encoding=texttospeech_v1.AudioEncoding.MP3
	)


	response = client.synthesize_speech(
		input=synthesis_input,
		voice=voice,
		audio_config=audio_config
	)

	#print(help(texttospeech.AudioConfig()))
	with open('synthesized_audio.mp3', 'wb') as output:
		output.write(response.audio_content)

	mixer.music.load("synthesized_audio.mp3")
	mixer.music.set_volume(0.7)
	mixer.music.play()
	time.sleep(5)
