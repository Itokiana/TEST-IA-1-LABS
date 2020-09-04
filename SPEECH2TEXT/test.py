import speech_recognition as sr
import gtts
from playsound import playsound
import time

# obtain audio from the microphone 
r = sr.Recognizer() 
with sr.Microphone() as source:
  print("Please wait. Calibrating microphone...")
  # listen for 5 seconds and create the ambient noise energy level        
  r.adjust_for_ambient_noise(source, duration=2)
  while (1):
    print("Say something!")
    audio = r.listen(source)

    try:
      output = r.recognize_google(audio, language = "fr-FR")
      print("Google thinks you said :" + output)
      # make request to google to get synthesis
      tts = gtts.gTTS(output, lang="fr")

      # save the audio file
      tts.save("hello.wav")

      # play the audio file
      playsound("hello.wav")
      time.sleep( 5 )
      output = ""
    except sr.UnknownValueError:
      print("Google could not understand audio")
    except sr.RequestError as e:
      print("Google error; {0}".format(e))
    # time.sleep( 7 )