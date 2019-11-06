import sounddevice as sd
from pynput.keyboard import Key, Controller
import time
import speech_recognition as sr
from pywinauto.application import Application
import soundfile as sf
import pywinauto
import keyboard
import os
import threading

cmd = ""

def worker(id):

    global cmd
    fs = 16000
    seconds = 2
    recognizer = sr.Recognizer()

    #print('mow '+str(id))

    warunek=1

    licznik=0+(4*id)
    while(warunek==1):
        #time.sleep(0.2)

        licznik=(licznik%4) + (4*id)

        nazwa = str(licznik)+'.wav'
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        start = time.time()
        sf.write(nazwa, myrecording, 16000)

        with sr.AudioFile(nazwa) as source:
            audio = recognizer.record(source)

        try:
            tekst = recognizer.recognize_google(audio)
            print('komenda:'+str(id) + str(tekst))
        except sr.UnknownValueError:
            tekst = ""

        licznik+=1

        if(tekst != ""):
            cmd = tekst

        end = time.time()
        if(end-start<0.5):
            time.sleep(0.5-(end-start))

    return

if __name__ == "__main__":

    threads = []

    for i in range(2):
        threads.append(threading.Thread(target=worker, args=(i,)))

    for t in threads:
        t.start()
        time.sleep(1.25)

    for t in threads:
        t.join()

    print('zakonczono')

import math


