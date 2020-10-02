import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import app
import pywhatkit as kit
import urllib.request

contact = {'vaibhav': 'antrikshmisri61@gmail'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

endst = ['bye' , 'goodbye' , 'end' , 'exit' , 'stop' , 'stop listening' , 'terminate']
#training the voicebot
app.trainbot()


def Tostring(s):
    str = " "
    return (str.join(s))

def Findorder(s):
    k=0
    for i in range(len(s) - 1):
        if(s[i] == 'on'):
            k=i

    return k

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail','yourpass')
    server.sendmail('youremail',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon ,")
    else:
        speak("good evening ,")

    speak("i am gogo , how may i help you?")


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
        if(searchstring[i] == 'on' or 'On' and i == Findorder(searchstring)):
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
        speak("sure , searching" + Tostring(newstring) + "on" + str(website[0]) + ",")
        # noinspection PyUnboundLocalVariable
        webbrowser.open("https://" + str(website[0]) + ".com" + "/search?q=" + Tostring(newstring), new=1, autoraise=True)


    elif 'play music' in query:
        if(Findorder(searchstring) != 0 and connect() == True):
            website = searchstring[i+1:]
            speak("what genre do you want to play?")
            genre = take().lower()
            speak("sure , playing" + genre + "music on" + Tostring(website))
            kit.playonyt(genre + " music")
        else:
            speak("sure sir")
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

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
    elif(query in endst):
        speak("Goodbye , have a nice day")
        exit("1: User terminated program")
    else:
        response = app.get_bot_response(query)
        speak(response)









