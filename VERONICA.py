import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# (voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')
    elif hour >= 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good evening')

    speak('hello i am VERONICA, how may i help you ?')


def takecommand():
    # it takes microphone input from user and provide with string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening . . .')
        r.pause_threshold = 0.8
        r.energy_threshold = 2000
        audio = r.listen(source)
    try:
        print('Recognizing . . .')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')
    except Exception as e:
        print(e)  # to print errors
        print('say that again please')
        return 'None'
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia . . .')
            query = query.replace('wikipedia', ' ')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir = 'E:\\music\\eng'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 10)]))
            # random module generates random number and plays song according to the generated number
        elif 'open steam' in query:
            stmpath = "C:\\Program Files (x86)\\Steam\\Steam.exe"
            os.startfile(stmpath)


