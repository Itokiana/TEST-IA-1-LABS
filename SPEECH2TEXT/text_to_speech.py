import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS('Bonjour, bienvenue chez Sayna', lang="fr")

# save the audio file
tts.save("hello.wav")

# play the audio file
playsound("hello.wav")