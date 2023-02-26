import time, sys, os
from pygame import mixer
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

def repeat(response):
	x = mixer.music.Sound(response)
	mixer.play(x)

def speak(text, lang):
	mixer.init()

	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/ubuntu/Translator/translator-378115-8e87c6b909b1.json'
	client = texttospeech_v1.TextToSpeechClient()

	synthesis_input = texttospeech_v1.SynthesisInput(text=text)

	voice = texttospeech_v1.VoiceSelectionParams(
		language_code="en-ca",
		ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
	)
	if lang == "en":
		voice = texttospeech_v1.VoiceSelectionParams(
		language_code="uk",
		ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE)
	audio_config = texttospeech_v1.AudioConfig(
		audio_encoding=texttospeech_v1.AudioEncoding.MP3
	)


	response = client.synthesize_speech(
		input=synthesis_input,
		voice=voice,
		audio_config=audio_config
	)

	#print(help(texttospeech.AudioConfig()))
	with open('/home/ubuntu/Translator/synthesized_audio.mp3', 'wb') as output:
		output.write(response.audio_content)

	mixer.music.load("/home/ubuntu/Translator/synthesized_audio.mp3")
	mixer.music.set_volume(0.7)
	mixer.music.play()
	time.sleep(5)
