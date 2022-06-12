from speak import speak
from googletrans import Translator

translator = Translator()
count = 0

translated_text = translator.translate("Traduis ce texte")
print(translated_text.text)
speak(translated_text.text)
