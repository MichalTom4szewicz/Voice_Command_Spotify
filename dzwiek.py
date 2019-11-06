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




if __name__ == "__main__":

    #app = Application().start(r"C:\Users\michal_internet\AppData\Roaming\Spotify\Spotify.exe")
    #dlg_spec = app.window(title='Spotify Premium')
    #time.sleep(10)
    #dlg_spec.minimize()  # in production

    fs = 44100
    seconds=2
    skok=7

    app = Application().connect(title='Spotify Premium')

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
    while(warunek == 1):
        q_pressed =0

        while(q_pressed==0):
            if(keyboard.is_pressed('q')):
                q_pressed=1

        print('mow:')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('1.wav', fs, myrecording)  # Save as WAV file

        x, _ = librosa.load('1.wav', sr=16000)
        sf.write('1.wav', x, 16000)

        harvard = sr.AudioFile('1.wav')

        with harvard as source:
            audio = recognizer.record(source)
        tekst= recognizer.recognize_google(audio)


        #qqtekst = rec_from_mic(recognizer, microphone)
        print('komenda:'+str(tekst))

        if(tekst == 'next'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.right)
            controller.release(Key.ctrl_l)
            controller.release(Key.right)
            window.Minimize()

        if (tekst == 'previous'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.left)
            controller.release(Key.ctrl_l)
            controller.release(Key.left)
            window.Minimize()

        if (tekst == 'up'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.up)
                controller.release(Key.ctrl_l)
                controller.release(Key.up)
            window.Minimize()

        if (tekst == 'down'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.down)
                controller.release(Key.ctrl_l)
                controller.release(Key.down)
            window.Minimize()

        if (tekst == 'start' or tekst =='stop'):
            window.Maximize()
            #window.SetFocus()
            time.sleep(0.1)
            controller.press(Key.space)
            controller.release(Key.space)
            #q window.LooseFocus()
            window.Minimize()
            #q window.SetFocus()qq



        if(tekst == 'exit'):
            warunek=0

    window.Maximize()
    time.sleep(0.1)
    controller.press(Key.space)
    controller.release(Key.space)
    window.Minimize()
    print('zakonczono')

