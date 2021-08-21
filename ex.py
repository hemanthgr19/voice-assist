import pyttsx3 as p
import randfacts
import speech_recognition as sr
from selinium import infow
from youtube import music
from joke import joke
from piz import pizza
from day import today_date


engine = p.init()
##engine properties
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
#reducing the voice speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

r= sr.Recognizer()

speak("hello sir, iam your voice assistant, how are you")

##micrphone as a source it iwill take the input we are talking
with sr.Microphone() as source:
    r.energy_threshold = 10000
    ## threshold is nothing but multiple voice detect
    r.adjust_for_ambient_noise(source, 1.2)
    print("listining...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    ## our speech convert to text and it will send to the google
    print(text)


speak("what can i do for you")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listining...")
    audio = r.listen(source)
    text2 =r.recognize_google(audio)
    print(text2)

##n  getting information
    if 'information' and 'search' in text2:
        speak('what kind of information do you want')
        with sr.Microphone() as source:
            print("listining....")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        assist = infow()
        assist.get_info(infor)


        ## youtube
    elif 'youtube' and 'play' and 'video' and 'music' in text2:
        speak("which song do you want to play?")
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("listining...")
            audio = r.listen(source)
            vid = r.recognize_google(audio)

        print('playing {} on youtube'.format(vid))
        assist = music()
        assist.play(vid)
## random fact
    elif 'fact' in text2:
        x = randfacts.get_fact()
        print(x)
        speak(x)
## jokes
    elif "joke" in text2:
        ar = joke()
        print(ar[0])
        speak(ar[0])
        print(ar[1])
        speak(ar[1])

    elif "order" and "pizza" in text2:
        pizza()
        #pizza()

    elif "time" and "date" in text2:
        today_date()




