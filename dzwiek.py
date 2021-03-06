import sounddevice as sd
from pynput.keyboard import Key, Controller
import time
import speech_recognition as sr
from pywinauto.application import Application
import soundfile as sf
import pywinauto
import keyboard
import os


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

    fs = 16000
    seconds = 2.5
    skok = 7

    try:
        app = Application().connect(title='Spotify Premium')
    except pywinauto.findwindows.ElementNotFoundError:
        os.system("taskkill /IM \"Spotify.exe\" /F")
        app = Application().start(r"C:\Users\michal_internet\AppData\Roaming\Spotify\Spotify.exe")

        for i in range(10):
            print(i + 1)
            time.sleep(1)

    handle = pywinauto.findwindows.find_windows(title='Spotify Premium')[0]

    window = app.window_(handle=handle)

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    controller = Controller()

    warunek = 1
    print('dziala:')
    licznik = 0
    while (warunek == 1):
        if (keyboard.is_pressed('q')):
            warunek = 0

        licznik = licznik % 10
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        sf.write(str(licznik) + '.wav', myrecording, 16000)

        harvard = sr.AudioFile(str(licznik) + '.wav')

        with harvard as source:
            audio = recognizer.record(source)
        try:
            tekst = recognizer.recognize_google(audio)
            print('komenda:' + str(tekst))
        except sr.UnknownValueError:
            # print("nie rozpoznano"+ str(licznik))
            tekst = ""

        #tekst = rec_from_mic(recognizer, microphone)

        if (tekst == 'next' or tekst == 'text' or tekst == 'ex' or tekst == 'neck' or tekst == 'max'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.right)
            controller.release(Key.ctrl_l)
            controller.release(Key.right)
            window.Minimize()

        if (tekst == 'previous' or tekst == 'envious' or tekst == 'prev' or tekst == 'pre'):
            time.sleep(0.1)
            window.Maximize()
            controller.press(Key.ctrl_l)
            controller.press(Key.left)
            controller.release(Key.ctrl_l)
            controller.release(Key.left)
            window.Minimize()

        if (tekst == 'up' or tekst == 'app' or tekst == 'hop'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.up) 
                controller.release(Key.ctrl_l)
                controller.release(Key.up)
            window.Minimize()

        if (tekst == 'down' or tekst == 'own' or tekst == 'dial' or tekst == 'dawn'):
            time.sleep(0.1)
            window.Maximize()
            for i in range(skok):
                controller.press(Key.ctrl_l)
                controller.press(Key.down)
                controller.release(Key.ctrl_l)
                controller.release(Key.down)
            window.Minimize()

        if (
                tekst == 'start' or tekst == 'stop' or tekst == 'star' or tekst == 'sta' or tekst == 'art' or tekst == 'op' or tekst == 'top'):
            window.Maximize()
            time.sleep(0.1)
            controller.press(Key.space)
            controller.release(Key.space)
            window.Minimize()

        if (tekst == 'exit' or tekst == 'it' or tekst == 'exi' or tekst == 'xit' or tekst == 'exit ' or tekst == 'eat'):
            warunek = 0

        licznik += 1

    window.Maximize()
    time.sleep(0.1)
    controller.press(Key.space)
    controller.release(Key.space)
    window.Minimize()
    print('zakonczono')
