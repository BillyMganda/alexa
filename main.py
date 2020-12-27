import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pytz
import geopy

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'my time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, i have a headache')
    elif 'are you single' in command:
        talk('Sorry, i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'what is the time in' in command:
        tz = pytz.timezone('Europe/Berlin')
        berlin = datetime.datetime.now(tz).strftime('%I:%M %p')
        print(berlin)
        talk(berlin)

    else:
        talk('Please say that again.')

while True:
    run_alexa()