import imp
from socket import timeout
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import pywhatkit
import wikipedia
import pyjokes



flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
        speak("i am olivia")
        speak("your personal assistant")
        speak("how may i help you")
    else:
        speak("Good afternoon")
        speak("i am olivia")
        speak("your personal assistant")
        speak("how may i help you")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.olivia()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            R.pause_threshold = 1
            audio = R.listen(source, timeout=1, phrase_time_limit=5)
        try:
            print("Recognizing......")
            text = R.recognize_google(audio)

            if 'olivia' in self.query:
                self.query = self.query.replace('olivia', '')
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def olivia(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            elif 'play' in self.query:
                song = self.query.replace('play', '')
                print('Playing ' + song)
                speak('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Now the time is ' + time)
                speak('Now the time is ' + time)
            elif 'about' in self.query:
                person = self.query.replace('about', '')
                info = wikipedia.summary(person, 2)
                print(info)
                speak(info)
            elif 'joke' in self.query:
                print(pyjokes.get_joke())
                speak(pyjokes.get_joke())
            elif 'open notepad' in self.query:
                speak('opening notepad')
                notepad = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(notepad)
            elif 'close notepad' in self.query:
                speak('closing notepad')
                os.system('taskkill /f /im notepad.exe')

            elif 'open browser' in self.query:
                speak('opening browser')
                browser = 'C:\\Program Files\\Google\\Chrome\\Application\\crome.exe'
                os.startfile(browser)
            elif 'close browser' in self.query:
                speak('closing browser')
                os.system('taskkill /f /im crome.exe')
            else:
               speak('Please say the command again.')










FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='black'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())