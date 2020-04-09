from gtts import gTTS
tts = gTTS(text ="your sentence",lang = 'en')
#In case of hindi , type lang="hi"
tts.save("Location where your file should be saved along with it`s name")
# E.g - C://Users//Pankhuri//Desktop//audioClipsP//udit.mp3
