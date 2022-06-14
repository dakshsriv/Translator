import speech_recognition as sr
import time

t_end = time.time() + 10
r = sr.Recognizer()
audio2 = ""
while time.time() < t_end:
	try:
		with sr.Microphone(device_index=2) as source2:
			r.adjust_for_ambient_noise(source2, duration=0.2)             
			audio2 = r.listen(source2)
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e)) 
	except sr.UnknownValueError:
		print("unknown error occured")
MyText = r.recognize_google(audio2) 
MyText = MyText.lower()
print("Did you say "+MyText)