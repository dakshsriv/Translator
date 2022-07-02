from speak import speak
from googletrans import Translator

def run(preText):
    translator = Translator()
    final = ""
    count = 0
    lang = translator.detect(preText)
    if lang.lang == "en":
        translated_text = translator.translate(preText, dest="fr")
    else:
        translated_text = translator.translate(preText)
    print(lang, lang.lang)
    print(translated_text.text)
    speak(translated_text.text, lang.lang)

#run("Bonjour tout le monde.")
#run("Hello everyone!")
