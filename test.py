import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

contact = {'vaibhav': 'antrikshmisri61@gmail'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def Tostring(s):
    str = " "
    return (str.join(s))

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('antrikshmisri61@gmail.com','Antriksh@123')
    server.sendmail('antrikshmisri61@gmail.com',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak("hello sir i am gogo , how may i help you?")


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio)
            print(query)
        except Exception as e:
            print(e)
            print("say that again please")
            return "None"
        return query




wishMe()
while True:
    query = take().lower()
    searchstring = query.split()

    for i in range(1 , len(searchstring) - 1):
        if(searchstring[i] == 'on' or 'On'):
            newstring = searchstring[1:i]
            website = searchstring[i+1:]

    if 'wikipedia' in query:
        speak('Searching wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'search'  in query:
        speak("sure sir , searching" + Tostring(newstring) + "on" + str(website[0]) + ",")
        # noinspection PyUnboundLocalVariable
        webbrowser.open("https://" + str(website[0]) + ".com" + "/search?q=" + Tostring(newstring), new=1, autoraise=True)


    elif 'play music' in query:
        speak("sure sir")
        music_dir = 'D:\\songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")

    elif 'send email' in query:
        try:
            speak("To whom should i send the mail sir?")
            w=take()
            for w,m in  contact.items():
                speak("what message should i send sir?")
                content=take()
                to= contact
                sendemail(to, content)

        except Exception as e:
            print(e)
            speak("sorry sir, couldn't send mail")









