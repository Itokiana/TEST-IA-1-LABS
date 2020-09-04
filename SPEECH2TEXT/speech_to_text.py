
# NOTE: this example requires PyAudio because it uses the Microphone
import speech_recognition as sr

# obtain audio from the microphone 
r = sr.Recognizer() 
with sr.Microphone() as source:
  print("Please wait. Calibrating microphone...")
  # listen for 5 seconds and create the ambient noise energy level        
  r.adjust_for_ambient_noise(source, duration=2)
  while (1):
    print("Say something!")
    audio = r.listen(source)

    # recognize speech using Sphinx
    # try:
    #   print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    # except sr.UnknownValueError:
    #   print("Sphinx could not understand audio")
    # except sr.RequestError as e:
    #   print("Sphinx error; {0}".format(e)) 

    # recognize speech using Google language="fr-FR"
    try:
      print("Google thinks you said :" + r.recognize_google(audio, language = "fr-FR"))
    except sr.UnknownValueError:
      print("Google could not understand audio")
    except sr.RequestError as e:
      print("Google error; {0}".format(e))
