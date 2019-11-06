from random import randint
#import numpy as np

# #hit roll 5+ z rerollem
#
# ile=0
# liczba = 10000000
#
# for i in range(liczba):
#     if(randint(1,6)<5):
#         if(randint(1,6)>4):
#             ile += 1
#     else:
#         ile +=1
#
#
# print(ile/liczba)


from datetime import date, time
import sounddevice as sd
from scipy.io.wavfile import write

from playsound import playsound

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import datetime

# from time import gmtime, strftime
# timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
#
# ts = str(timestamp)+".wav"
# print(ts)
#
#
# fs = 44100  # Sample rate
# seconds = 3 # Duration of recording
#
#
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write(ts, fs, myrecording)  # Save as WAV file
#
# #playsound(ts)
#
#
# import matplotlib.pyplot as plt
# from scipy.io import wavfile as wav
# rate, data = wav.read(ts)
#
# sd.play(data, fs)
#
# min=0
# max=0
#
# for i in data:
#     for j in i:
#         a = float(j)
#         if a<min:
#             min=a
#         if a>max:
#             max=a
#
# print("minimum: "+ str(min))
# print("maximum: "+ str(max))
# plt.plot(data)
# plt.show()
#
#
# import os
#
# list = os.listdir(r"C:\Users\michal_internet\Desktop\Pythony\Kwiatki")
#
# nazwa = "dane.txt"
#
#
# #jakiestam przetwarzanie ocena tego czy jest glosno czy cicho, najlepiej w dB
# # moze cos takiego https://github.com/SuperShinyEyes/spl-meter-with-RPi
#
# if nazwa in list:
#     f = open("dane.txt", "a")
#     f.write(str(timestamp)+" "+ str(min)+ " "+ str(max)+"\n")
#     f.close()
# else:
#     f = open("dane.txt", "x")
#     f.write(str(timestamp)+" "+ str(min)+ " "+ str(max)+"\n")
#     f.close()




import numpy as np
import pyaudio

import sounddevice as sd

##############################################################################################################################################################################

from pynput.keyboard import Key, Controller
import time
import speech_recognition as sr
from pywinauto.application import Application
import librosa
import soundfile as sf
import pywinauto
import keyboard



def rec_from_mic(recognizer, microphone):

    print("mow")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    x = recognizer.recognize_google(audio)

    print("przechwycono")
    print('komenda: {0}'.format(str(x)))
    return str(x)



import os

if __name__ == "__main__":

    #app = Application().start(r"C:\Users\michal_internet\AppData\Roaming\Spotify\Spotify.exe")
    #dlg_spec = app.window(title='Spotify Premium')
    #time.sleep(10)
    #dlg_spec.minimize()  # in production

    fs = 44100
    seconds=2.5
    skok=7

    try:
        app = Application().connect(title='Spotify Premium')
    except pywinauto.findwindows.ElementNotFoundError:
        os.system("taskkill /IM \"Spotify.exe\" /F")
        app = Application().start(r"C:\Users\michal_internet\AppData\Roaming\Spotify\Spotify.exe")

        for i in range(10):
            print(i+1)
            time.sleep(1)

    handle = pywinauto.findwindows.find_windows(title='Spotify Premium')[0]

    window = app.window_(handle=handle)


    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    controller = Controller()

    #window.Maximize()
    #window.SetFocus()
    #window.Minimize()

    warunek=1
    print('dziala:')
    licznik=0
    while(warunek == 1):
        # q_pressed =0
        #
        # while(q_pressed==0):
        if(keyboard.is_pressed('q')):
            warunek=0

        licznik=licznik%10
        print('mow:')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(str(licznik)+'.wav', fs, myrecording)  # Save as WAV file

        x, _ = librosa.load(str(licznik)+'.wav', sr=16000)
        sf.write(str(licznik)+'.wav', x, 16000)

        harvard = sr.AudioFile(str(licznik)+'.wav')

        with harvard as source:
            audio = recognizer.record(source)
        try:
            tekst= recognizer.recognize_google(audio)
            print('komenda:' + str(tekst))
        except sr.UnknownValueError:
            print("nie rozpoznano"+ str(licznik))
            tekst =""


        #qqtekst = rec_from_mic(recognizer, microphone)


        if(tekst == 'next'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.right)
            controller.release(Key.ctrl_l)
            controller.release(Key.right)
            window.Minimize()

        if (tekst == 'previous' or tekst =='envious' or tekst =='prev' or tekst =='pre'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.left)
            controller.release(Key.ctrl_l)
            controller.release(Key.left)
            window.Minimize()

        if (tekst == 'up' or tekst =='app' or tekst =='hop'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.up)
                controller.release(Key.ctrl_l)
                controller.release(Key.up)
            window.Minimize()

        if (tekst == 'down' or tekst =='own'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.down)
                controller.release(Key.ctrl_l)
                controller.release(Key.down)
            window.Minimize()

        if (tekst == 'start' or tekst =='stop' or tekst =='star' or tekst =='sta' or tekst =='art' or tekst =='op' or tekst =='top' ):
            window.Maximize()
            time.sleep(0.1)
            controller.press(Key.space)
            controller.release(Key.space)
            window.Minimize()

        if(tekst == 'exit' or tekst =='it' or tekst =='ex' or tekst =='exi' or tekst =='xit' or tekst =='exit '):
            warunek=0

        licznik+=1

    window.Maximize()
    time.sleep(0.1)
    controller.press(Key.space)
    controller.release(Key.space)
    window.Minimize()
    print('zakonczono')
