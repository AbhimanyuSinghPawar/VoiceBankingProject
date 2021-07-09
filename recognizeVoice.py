import speech_recognition as sr
import pyttsx3 as txt
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = txt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say('I am HSBC Chat bot')
engine.say('How can i help you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listning...')
            voice = listener.listen(source)
            command1 = listener.recognize_google(voice)
            print(command1)
            command = command1.lower()
            print(command)
            if 'hsbc' in command:
                engine.say('mai Hu Don Mai hu Don Mai Hu Don')
                talk(command)
                command = command.replace('hsbc','')
    except:
        pass
    return command


def run_hsbc():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        talk(' Current time is ' + time)
        talk(' Current time with am/pm is ' + time1)
    elif 'search' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        talk(jokes)
        print(jokes)
    else:
        talk('Sorry I cant understand. Can you please repeat')


while True:
    run_hsbc()

