from fuzzywuzzy import fuzz
from src.settings import Event
import time
import pyttsx3
import speech_recognition as sr

class Bot:

    def __init__(self):
        self.__running = True
        self.event = Event()
        # for recognations voice
        self.speak_engine = pyttsx3.init()
        self.recog = sr.Recognizer()
        self.micro = sr.Microphone(device_index=1)
        self.voices = self.speak_engine.getProperty('voices')
        self.speak_engine.setProperty('voice', self.voices[2].id)
        self.opts = {
                    'alias': ('filip', 'snake', 'bot', 'robot', 'ai', 'intelligence'),
                    'tbr': ('reverse', 'make', 'go', 'reverse'),
                    'cmds': {
                        'change_one': ('one', 'first', '1'),
                        'change_two': ('two', 'second', '2'),
                        'change_three': ('three', 'third', '3'),
                        'change_four': ('four', 'fourth', '4'),
                        'change_five': ('five', 'fifth', '5'),
                        'change_six': ('six', 'sixth', '6'),
                        'change_seven': ('seven', 'seventh', '7'),
                        'change_eight': ('eight', 'eighth', '8'),
                        'change_nine': ('nine', 'ninth', '9'),
                        'change_ten': ('ten', 'tenth', '10'),
                        'pause_play': ('pause', 'play', 'start'),
                        'exit': ('exit', 'finish')
                    }
                }

    def listen(self):
        print('start work')
        with self.micro as source:
            self.recog.adjust_for_ambient_noise(source)

        stop_listening = self.recog.listen_in_background(self.micro,
                                                         self.callback)
        while (self.__running): time.sleep(0.01)

    def callback(self, recognizer, audio):
        print('calbaack')
        try:
            voice = recognizer.recognize_google(audio,
                                                language='en-En')
            print('[log] Done: ' + voice)

            if voice.startswith(self.opts['alias']):
                cmd = voice
                for x in self.opts['alias']:
                    cmd = cmd.replace(x, '').strip()
                for x in self.opts['tbr']:
                    cmd = cmd.replace(x, '').strip()
                cmd = self.recognizer_cmd(cmd)
                print(cmd['cmd'])
                # self.execute_cmd(cmd['cmd'])
                self.event.set_event(cmd['cmd'])

        except sr.UnknownValueError:
            print('Unknown voice!')
        except sr.RequestError as e:
            print('[log] Error!Problem with internet, maybe!?')

    def recognizer_cmd(self, cmd):
        print('recognizer_cmd')
        RC = {'cmd': '', 'percent': 0}
        for c, v in self.opts['cmds'].items():
            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > RC['percent']:
                    RC['cmd'] = c
                    RC['percent'] = vrt
        return RC
