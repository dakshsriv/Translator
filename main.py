from speak import speak
from googletrans import Translator

def run(preText):
    translator = Translator()
    count = 0
    translated_text = translator.translate(preText)
    print(translated_text.text)
    speak(translated_text.text)
