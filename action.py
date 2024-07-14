import operator
import pyttsx3
import speech_recognition
import datetime
import os
import sys
from speech_to_text import takeCommand
import pyautogui
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Action(send):
    query = send.lower()
    if "wake up" in query:
        from greetme import greetMe
        greetMe()
        return "HELLO, Please tell me, How can I help you ?"
    elif "go to sleep" in query:
        speak("Ok sir , You can call me anytime")
        return "Ok sir , You can call me anytime"
        sys.exit()
    elif "google" in query:
        from SearchNow import searchGoogle
        searchGoogle(query)
        return "Searching now on google"
    elif "youtube" in query:
        from SearchNow import searchYoutube
        searchYoutube(query)
        return "Searching now on youtube"
    elif "wikipedia" in query:
        from SearchNow import searchWikipedia
        searchWikipedia(query)
        return "Searching from wikipedia"
    elif "time" in query:
        from datetime import datetime
        dt_obj = datetime.now()
        time= dt_obj.strftime('%I:%M %p')
        time.replace(":","")
        speak(f"Sir,The current time is {time}")
        return(f"Sir,The current time:{time}")
    elif "set an alarm" in query:
        try:
            speak("Please tell me the time.For example: set 5:30 am ")
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            my_string= my_string.replace("set ", "")
            my_string= my_string.replace(".", "")
            my_string = my_string.upper()
            import alarm
            alarm.alarm(my_string)
            return "alarm is running"
        except Exception as e:
            print("Say that again")
    elif "volume up" in query:
        import keyboard
        keyboard.volumeup()
        speak("Turning volume up,sir")
        return "Turning volume up,sir"
        volumeup()
    elif "volume down" in query:
        import keyboard
        keyboard.volumedown()
        speak("Turning volume down, sir")
        return "Turning volume down, sir"
        volumedown()
    elif "whatsapp" in query:
        from Whatsapp import sendMessage
        sendMessage()
        return " message sent"
    elif "open" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(2)
        pyautogui.press("enter")
        speak("Opening the application, sir")
        return "opening the application"
    elif "screenshot" in query:
        im = pyautogui.screenshot()
        im.save("ss.jpg")
        return"screenshot saved in the working directory"
    elif "calculate" in query:
        try:
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                speak("say what you want to calculate,example: 3 plus 3")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            def get_operator(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    '/': operator.truediv,

                }[op]

            def eval_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator(oper)(op1, op2)

            speak("your result is:")
            print("your result is:", eval_expr(*(my_string.split())))
            speak(eval_expr(*(my_string.split())))
            return "your result is:", eval_expr(*(my_string.split()))
        except Exception as e:
            speak("Something went wrong.....Call the calculate function again")
            return("Something went wrong.....Call the calculate function again")
    elif "translate" in query:
        from Translator import translategl
        query = query.replace("jarvis", "")
        query = query.replace("translate", "")
        translategl(query)
        return "Successfully Translated the given sentence"
    elif "audiobook" in query:
        try:
            import pyttsx3
            from pypdf import PdfReader
            import os
            import time
            path = r'C:\Users\hp\PycharmProjects\pythonProject\.idea'
            allFiles = os.listdir(path)
            pdf = [i for i in allFiles if '.pdf' in i]
            print("List of all audio books available:")
            for (i, a) in enumerate(pdf, start=1):
                print(i, a)
            speak("say which book you want to play by their serial number")
            b = int(input("enter the index:"))
            book = open(r'C:\Users\hp\PycharmProjects\pythonProject\.idea\{}'.format(pdf[b - 1]), 'rb')
            pdfReader = PdfReader(book)
            speaker = pyttsx3.init()
            number_of_pages = len(pdfReader.pages)
            for i in range(0, number_of_pages):
                page = pdfReader.pages[i]
                text = page.extract_text()
                speaker.say(text)
                speaker.runAndWait()
            speaker.save_to_file('text', 'audiobook.mp3')
            speaker.runAndWait()
            query = query.replace("jarvis", "")
            speak("playing the audiobook")
            return("playing the audiobook")
        except Exception as e:
            print("process terminated")
    else:
        speak("i'm unable to understand!")
        return("i'm unable to understand!")