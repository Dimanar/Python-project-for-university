class Settings:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    GREEN = (0, 200, 0)
    BRIGHT_RED = (255, 0, 0)
    BRIGHT_GREEN = (0, 255, 0)
    button_play_cord = (150, 450, 100, 50)
    button_exit_cord = (350, 450, 100, 50)
    screen = (WIDTH, HEIGHT) = 600, 600
    back_picture = '../image/back_2.jpg'
    back_picture_pos = [-10, -10]
    position_avatar = (250, 325)
    name_app = 'Dancing girl'

class Event:
    EVENT = (None, None, None)

    def __init__(self):
        self.exit = None
        self.pause = None
        self.change = None
        self.main = (self.exit, self.pause, self.change)

    def set_event(self, cmd):
        print('-'*8)
        print(cmd)
        print('-' * 8)
        if cmd == 'exit':
            self.main = (True, None, None)
        elif cmd == 'pause_play':
            self.main = (None, True, None)
        elif cmd == 'change_one':
            self.main = (None, None, 0)
        elif cmd == 'change_two':
            self.main = (None, None, 1)
        elif cmd == 'change_three':
            self.main = (None, None, 2)
        elif cmd == 'change_four':
            self.main = (None, None, 3)
        elif cmd == 'change_five':
            self.main = (None, None, 4)
        elif cmd == 'change_six':
            self.main = (None, None, 5)
        elif cmd == 'change_seven':
            self.main = (None, None, 6)
        elif cmd == 'change_eight':
            self.main = (None, None, 7)
        elif cmd == 'change_nine':
            self.main = (None, None, 8)
        elif cmd == 'change_ten':
            self.main = (None, None, 9)

        Event.EVENT = self.main

    @staticmethod
    def get_event():
        return Event.EVENT