import pyttsx3
import speech_recognition as sr
import datetime
import os
import  webbrowser
from requests import get
import wikipedia
import pywhatkit as kit
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)


def Speak(Audio):

    print(f": {Audio}")
    engine.say(Audio)
    engine.runAndWait()

def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        Speak("Good morning")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon")

    else:
        Speak("Good Evening")
    Speak("I am Jarvis Sir")

def welcome():
    Speak("May I know your name")
    name = takecommand().lower()
        
    if 'anirudh' in name:
        Speak("Taking Biometric scan")
        Speak("Biometric scan complete")
        Speak("Welcome back anirudh")

    elif 'haripriya' in name:
        Speak("Biometric scan incomplete")
        Speak("You are not allowed to access to acces Anirudh database")
        Speak("Accesing the sattelite")
        Speak("Accesing Adhar information")
        Speak("You are doctor haripriya")
        Speak("You are Anirudh sister")
        Speak("Informing Anirudh")
        Speak("Sending message to edith")
        Speak("getting message from edith")    
        Speak("Permission granted by Anirudh")
        Speak("welcome back haripriya")
    
    else:
        Speak("Sorry you are not there in Anirudh database")
        Speak("You are not allowed to access this database")
        sys.exit()    
                                                                                            
if __name__ == "__main__":                                                                                            
    wishMe()
    welcome()
    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

                
        elif "open vs code"in query:
            Speak("opening vs code")
            mpath = "C:\\Users\\Anirudh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(mpath)

        elif "open pycharm" in query:
            Speak("opening pycharm")
            ppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.2.1.lnk"
            os.startfile(ppath)

        elif "open vlc" in query:
            opath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player.lnk"
            os.startfile(opath)
          
        elif "open bittorrent" in query:
            apath = "C:\\Users\\Anirudh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\BitTorrent.lnk"
            os.startfile(apath)

        elif "open edge" in query:
            bpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
            os.startfile(bpath)

        elif "open chrome" in query:
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(cpath)

        elif "open spotify" in query:
            dpath = "C:\\Users\\Anirudh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
            os.startfile(dpath)
        
        elif "who is your creator" in query:
            Speak("Anirudh is my creator")

        elif "who is the creator of you" in query:
            Speak("Anirudh he is the creator of me.Thanks to Anirudh")
            
        elif "open settings" in query:
            epath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Immersive Control Panel.lnk"
            os.startfile(epath)

        elif "open excel" in query:
            fpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(fpath)

        elif "open powerpoint" in query:
            gpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(gpath)

        elif "open word" in query:
            hpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(hpath)

        elif "open task manager" in query:
            ipath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk"
            os.startfile(ipath)
           
        elif "open zoom" in query:
            lpath = "C:\\Users\\Anirudh\\Desktop\\Zoom.lnk"
            os.startfile(lpath)

        elif "open whatsapp" in query:
            Speak("Opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif "open google developer" in query:
            webbrowser.open("https://developers.google.com/")

        elif "open amazon developer" in query:
            webbrowser.open("https://developers.amazon.com/")

        elif "open microsoft developer" in query:
            webbrowser.open("https://developers.microsoft.com/")

        elif "open apple developer" in query:
            webbrowser.open("https://developers.apple.com/")

        elif "open facebook developer" in query:
            webbrowser.open("https://developers.facebook.com/")
           
        elif "open downloads" in query:
            jpath = "C:\\Users\\Anirudh\\Downloads"
            os.startfile(jpath)

        elif "open my file" in query:
            kpath = "E:\Anirudh's Code\Code's"
            os.startfile(kpath)

        elif "close notepad" in query:
            os.system("taskkill /f /in notepad.exe")
        
        elif "close chrome" in query:
            os.startfile("taskill /F /in chrome.exe")

        elif 'close edge' in query:
            os.startfile("taskill /F /in msedge.exe")

        elif "close vs code" in query:
            os.startfile("taskill /F /in Code.exe")

        elif "close vlc" in query:
            os.startfile("taskill /F /in vlc.exe")

        elif "close bittorrent" in query:
            os.startfile("taskill /F /in BitTorrent.exe")

        elif "close spotify" in query:
            os.startfile("taskill /F /in Spotify.exe")

        elif "close settings" in query:
            os.startfile("taskill /F /in Control.exe")

        elif "close excel" in query:
            os.startfile("taskill /F /in EXCEL.EXE")

        elif "what is my ip address" in query:
            ip = get('https://api.ikpify.org').text
            Speak(f"Yor IP address is {ip}")

        elif "wikipedia" in query:
            Speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=5 )
            Speak("According to wikipedia")
            Speak(results)

        elif "open youtube" in query:
            Speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in query:
            Speak("What should I search on Google")
            cm =takecommand()
            webbrowser.open(f"{cm}")
           
        elif "send message" in query:
            kit.sendwhatmsg("+916364825477","This is testing protocol",2,24)

        elif "no thanks" in query:
            Speak("Thanks for using me sir")
            sys.exit()

        elif "bye" in query:
            sys.exit()

        elif "bhai" in query:
            sys.exit()

        elif "bike" in query:
            sys.exit()
        
        elif "just shut your mouth" in query:
            Speak("Sorry Sir")
            break
        
        
    