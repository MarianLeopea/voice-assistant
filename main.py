import sys
import warnings
import pyttsx3
import speech_recognition as sr
import os
import datetime
import calendar
import random
from gtts import gTTS
import webbrowser
from function_sound_file import function_sound
import wikipedia
import winshell
import pyjokes
import subprocess
import pywhatkit
import requests


warnings.filterwarnings("ignore")

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
# engine.setProperty('voice', voices[0].id)
engine.setProperty("voice", voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        recog.energy_threshold = 10000
        recog.adjust_for_ambient_noise(source, duration=0.60)
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition")

    return data


def response(text):
    print(text)

    tts = gTTS(text=text)
    audio = "Audio.mp3"

    tts.save(audio)

    function_sound()
    
    os.remove(audio)


def call(text):
    action_cll = "assistant"

    text = text.lower()

    if action_cll in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1th",
        "2th",
        "3th",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21th",
        "22th",
        "23th",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29h",
        "30th",
        "31h",
    ]

    return f"Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}."


def say_hello(text):
    greet = [
        "hi",
        "hey",
        "holla",
        "wassup",
        "hello",
        "howdy",
        "what's good",
        "hey there",
    ]

    response = [
        "hi",
        "hey",
        "holla",
        "wassup",
        "hello",
        "howdy",
        "what's good",
        "hey there",
    ]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" or list_wiki[i].lower() == "what" and list_wiki[i + 1].lower() == "is":
            b = list_wiki[i + 2:]
            if len(b) > 1:
                list_wiki = b[0] + ' ' +  b[1]
            else:
                list_wiki = b[0]
            return list_wiki


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def multy_number(text):
    list_number = text.split()
    for i in range(0, len(list_number)):
        if (
            i + 3 <= len(list_number) - 1
            and list_number[i].lower() == "multiply"
            and list_number[i + 2].lower() == "with"
            or list_number[i + 2].lower() == "and"
            or list_number[i + 2].lower() == "to"
            or list_number[i + 2].lower() == "by"
            or list_number[i + 2].lower() == "x"
        ):
            first = int(list_number[i + 1])
            secund = int(list_number[i + 3])
            result = first * secund
            return (
                list_number[i + 1]
                + " multiply "
                + list_number[i + 3]
                + " is equal to : "
                + str( '%g' % result))


def minus_number(text):
    list_number = text.split()
    for i in range(0, len(list_number)):
        if (
            i + 3 <= len(list_number) - 1
            and list_number[i].lower() == "decrease"
            or list_number[i].lower() == "make"
            and list_number[i + 2].lower() == "by"
            or list_number[i + 2].lower() == "to"
            or list_number[i + 2].lower() == "and"
            or list_number[i + 2].lower() == "-"
        ):
            first = int(list_number[i + 1])
            secund = int(list_number[i + 3])
            result = first - secund
            return (
                list_number[i + 1]
                + " minus "
                + list_number[i + 3]
                + " is equal to : "
                + str( '%g' % result))


def divide_number(text):
    list_number = text.split()
    for i in range(0, len(list_number)):
        if (
            i + 3 <= len(list_number) - 1
            and list_number[i].lower() == "divide"
            and list_number[i + 2].lower() == "by"
            or list_number[i + 2].lower() == "to"
            or list_number[i + 2].lower() == "and"
        ):
            first = float(list_number[i + 1])
            secund = float(list_number[i + 3])
            result = first / secund
            return (
                list_number[i + 1]
                + " divide to "
                + list_number[i + 3]
                + " is equal to : "
                + str('%g' % result))


def plus_number(text):
    list_number = text.split()
    for i in range(0, len(list_number)):
        if (
            i + 3 <= len(list_number) - 1
            and list_number[i].lower() == "assambly"
            or list_number[i].lower() == "add"
            or list_number[i].lower() == "make"
            and list_number[i + 2].lower() == "by"
            or list_number[i + 2].lower() == "to"
            or list_number[i + 2].lower() == "and"
            or list_number[i + 2].lower() == "+"
        ):
            first = int(list_number[i + 1])
            secund = int(list_number[i + 3])
            result = first + secund
            return ( first + " plas " + secund + " is equal to : " + str('%g' % result))


def temper(text):
    cityName = text.split()
    for i in range(0, len(cityName)):
        if (i + 2 <= len(cityName) -1  and cityName[i].lower() == 'temperature' or cityName[i].lower() == 'weather' and cityName[i + 1].lower() == "in"):
            b = cityName[i + 2:]
            if len(b) > 1:
                city = b[0] + ' ' +  b[1]
            else:
                city = b[0]

            baseURL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d3cda74a2e68185af6dbf09f8339c5bc'
            response  = requests.get(baseURL)
            data = response.json()
            c_temp = data['main']['temp'] -273.15

            for x in range(int(c_temp)):
                clod_temp = ''
                if x <= 10 :
                    clod_temp = str(f'It is  cold at {city} this time. ')
                elif x >= 11 and x == 18 :
                    clod_temp = str(f'The weather in {city} is good for this time of year. ')
                elif x > 18 :
                    clod_temp = str(f'The weather in {city} is good. ')

            max_temp = data['main']['temp_max']-273.15
            min_temp = data['main']['temp_min']-273.15
            f_like_temp = data['main']['feels_like']-273.15
            visib = data["visibility"]/3.281
            humid = data["main"]["humidity"]
            cloud = data["clouds"]["all"]

            for x in range(cloud):
                clod = ''
                if x <= 10 :
                    clod = str('The sky is clear')
                elif x >= 11 and x <= 50:
                    clod = str('The sky was a little cloudy') 
                elif x > 50 :
                    clod = str('The sky is clouded over')

            return ( clod_temp + ' Curent Temperature is: ' + '%g' % c_temp + ' degrees celsius.' 
                                            + 'maximum temperature is : ' + '%g' % max_temp + ' degrees celsius.' 
                                            + 'minimum temperature is : ' + '%g' % min_temp + ' degrees celsius.' 
                                            + 'Temperature feels like :' + '%g' % f_like_temp + ' degrees celsius.'
                                            + 'The humidity is :' + '%g' % humid + ' %.'
                                            + 'Visibility is :' + '%g' % visib + ' m.'
                                            + clod )


def voce():
    while True:

        try:

            text = rec_audio()
            speak = " "

            if call(text):
                speak = speak + 'Yes sir. How can I help you?'
                speak = speak + say_hello(text)

            elif "date" in text or "day" in text or "month" in text :
                get_today = today_date()
                speak = speak + " " + get_today

            elif "hi" in text or "hola" in text or "hello" in text or "wassup" in text or "what's good" in text :
                speak = speak + say_hello(text)

            elif "weather" in text.lower() or "temperature" in text.lower():
                temp_today = temper(text)
                speak = speak + " " + temp_today
            
            elif "multiply" in text.lower():
                if "multiply" in text.lower():
                    first_num = multy_number(text)
                    speak = speak + first_num

            elif "decrease" in text.lower() :
                if "decrease" in text.lower():
                    first_num = minus_number(text)
                    speak = speak + first_num

            elif "divide" in text.lower():
                if "divide" in text.lower():
                    first_num = divide_number(text)
                    speak = speak + first_num
            
            elif "assembly" in text.lower() or "add" in text.lower():
                if "assembly" in text.lower() or "plus" in text.lower():
                    first_num = plus_number(text)
                    speak = speak + first_num

            elif "thanks" in text.lower() or "thank you" in text.lower():
                speak = (
                    speak
                    + "It was a pleasure to help you. If you want something else, just let me know. "
                )

            elif "exit" in text.lower() or "finish" in text.lower() or "close" in text.lower() or "stop" in text.lower():
                speak = speak + "You say yes , so good bye!!."
                print('exit')
                break

            elif "time" in text.lower():
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "who are you" in text.lower() or "define your self" in text.lower():
                speak = speak + """ I am an Assistant. Your Assistant. I ame here to make your life easier. You 
                can command me to perform various tasks such end solving mathemetical questions or open application."""
            elif "you name" in text.lower():
                speak = speak + "my name is assistant"

            elif "Who am I" in text.lower() or "you know who I am" in text.lower():
                speak = speak + "You probably have to be human"

            elif "why do you exist" in text.lower() or "why did you come" in text.lower():
                speak = speak + "It is a secret"

            elif "how are you" in text.lower():
                speak = speak + "I am fine, thanks you"
                speak = speak + "\nHow are you"

            elif "fine" in text.lower() or "good" in text.lower():
                speak = speak + "It's good to know that you are fine"
            
            elif "wikipedia" in text or"Wikipedia" in text:
                if "who is" in text.lower() or "what is" in text.lower():
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=4)
                    speak = speak + " " + wiki

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

                elif "world" in text.lower():
                    speak = speak + "Opening Microsoft world"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft excel"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google"
                    webbrowser.open("https://google.com/")

                elif "facebook" in text.lower():
                    speak = speak + "Opening facebook"
                    webbrowser.open("https://www.facebook.com/")
                
                elif "tiktok" in text.lower():
                    speak = speak + "Opening tik tok"
                    webbrowser.open("https://www.tiktok.com/")
                
                elif "twitter" in text.lower():
                    speak = speak + "Opening twitter"
                    webbrowser.open("https://twitter.com/")
                
                elif "instagram" in text.lower():
                    speak = speak + "Opening instagram"
                    webbrowser.open("https://www.instagram.com/")

                else:
                    speak = speak + "Application not available "

            elif "play" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                pywhatkit.playonyt(search)
                speak = speak + "Opening and play " + str(search) + "on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                print(search)
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching" + str(search) + "on google"

            elif "where is" in text.lower():
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "+".join(location)
                webbrowser.open(url)
                speak = speak + "This is were" + str(location) + " is."

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "recycle bin emptied"

            elif "note" in text or "remember this" in text:
                talk("What would you like me to write down")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that"

            elif "joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()

            response(speak)

        except:
            talk("?")
