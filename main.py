from googletrans import Translator
from googletrans import LANGUAGES
import random

trans = Translator()

languages = []

#take input
print("What do you want to translate?")
text = str(input(">"))
print("And how many times?")
times = int(input(">"))

#map all the languages
for l in LANGUAGES:
	languages.append(l)

for i in range(times):
	lang = random.choice(languages)

	newText = trans.translate(text, dest=lang).text
	text = newText

	print(LANGUAGES[lang] + " -> " + text)

print(" ")

newText = trans.translate(text, dest="en").text
text = newText
print(LANGUAGES["en"] + " -> " + text)

newText = trans.translate(text, dest="nl").text
text = newText
print(LANGUAGES["nl"] + " -> " + text)
