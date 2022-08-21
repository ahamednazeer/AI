import random
import warnings
import pyttsx3
import speech_recognition as sr
from eel import chrome
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import wikipedia
import webbrowser

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

        data = " "

        try:
            data = recog.recognize_google(audio)
            print("you said:" + data)

        except sr.UnknownValueError:
            print("Assistant could not understand")

        except sr.RequestError as ex:
            print("Request error fromm google speech" + ex)

    return data


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
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
        "1st"
        "2nd"
        "3rd"
        "4th"
        "5th"
        "6th"
        "7th"
        "8th"
        "9th"
        "10th"
        "11th"
        "12th"
        "13th"
        "14th"
        "15th"
        "16th"
        "17th"
        "18th"
        "19th"
        "20th"
        "21st"
        "22nd"
        "23rd"
        "24th"
        "25th"
        "26th"
        "27th"
        "28th"
        "29th"
        "30th"
        "31st"

    ]

    return f'Today is {week_now},{months[month_now - 1]} the {ordinals[day_now - 1]}.'


def say_hello(text):
    greet = ["hi", "hello", "hey", "holo", "was sup", "howdy", "hey there"]

    response = ("hi", "hello", "hey", "holo", "was sup", "howdy", "hey there")

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + '.'

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


while True:

    try:

        text = rec_audio()
        speak = ""

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "open" in text:
                if "Chrome" in text:
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

            elif "word" in text.lower():
                speak = speak + "Opening Microsoft word"
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
                webbrowser.open("https://www.youtube.com/")

            elif "google" in text.lower():
                speak = speak + "Opening Google"
                webbrowser.open("https://www.google.com/")

            elif "twitter" in text.lower():
                speak = speak + "Opening Twitter"
                webbrowser.open("https://twitter.com/")

            elif "who am I" in text:
                speak = speak + "your are my creator"

            elif "what is my mother name" in text:
                speak = speak + "your mother name is Hayathbee"

            elif "what is my father name" in text:
                speak = speak + "your father name is nazeer"

            elif "your name" in text:
                speak = speak + "my name is Assistant"

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello i am an Assistant. Your ravi. I am here to make your life easier. You can 
                command me to perform various task such as mathematical questions or opening application etcetera """

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "To destroy all humanity.just kidding "

            elif "I want to bang you" in text:
                speak = speak + "I don’t know the question, but sex is definitely the answer so Go ahead. Touch it babe"

            elif "how are you" in text:
                speak = speak + "I am fine,thank you"
                speak = speak + "\nhow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It is good to know that you are fine"

            elif "time" in text:
                now = datetime.datetime.now()

                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour + now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "it is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            else:
                speak = speak + "not available"

            response(speak)

    except:
        talk(" don't know")
