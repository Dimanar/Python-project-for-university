import pygame
import sys
import src.voice as vc
import src.settings as st
from src.sprite import Avatar
import threading
from src.sprite import BackGround

class App:

    def __init__(self):
        self.__running = True
        self.__pause = False
        self.__intro = True
        self._size = self.weight, self.height = st.Settings.screen
        self.my_sprite = Avatar()
        self.my_group = pygame.sprite.Group(self.my_sprite)
        self.background = BackGround()
        self.event = st.Event()

        self.bot = vc.Bot()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(
            self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(st.Settings.name_app)

    def clean(self):
        pygame.quit()
        sys.exit()

    def on_event(self, event):
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            self.__running = False
        elif keys[pygame.K_ESCAPE]:
            self.__pause = not self.__pause
        if keys[pygame.K_1]:
            self.my_sprite.set_index(0)
        if keys[pygame.K_2]:
            self.my_sprite.set_index(1)
        if keys[pygame.K_3]:
            self.my_sprite.set_index(2)
        if keys[pygame.K_4]:
            self.my_sprite.set_index(3)
        if keys[pygame.K_5]:
            self.my_sprite.set_index(4)
        if keys[pygame.K_6]:
            self.my_sprite.set_index(5)
        if keys[pygame.K_7]:
            self.my_sprite.set_index(6)
        if keys[pygame.K_8]:
            self.my_sprite.set_index(7)
        if keys[pygame.K_9]:
            self.my_sprite.set_index(8)
        if keys[pygame.K_0]:
            self.my_sprite.set_index(9)

    def render(self):
        self.display_surf.fill(st.Settings.BLACK)
        self.display_surf.blit(self.background.image, self.background.rect)
        if not self.__pause:
            self.my_group.update()
        else:
            self.paused()
        self.my_group.draw(self.display_surf)
        pass

    def paused(self):
        self.on_init()
        while self.__pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__pause = False

            self.display_surf.fill(st.Settings.WHITE)
            self.display_surf.blit(self.background.image, self.background.rect)

            self.button('Continue', 'Quit', 1)

            pygame.display.update()

    def game(self):
        self.clock = pygame.time.Clock()

        while self.__running:
            pygame.time.delay(100)
            self.clock.tick(200)

            for event in pygame.event.get():
                self.on_event(event)

            temp = self.event.get_event()
            self.check(temp)

            self.render()
            pygame.display.update()
        self.clean()

    def intro(self):
        self.on_init()
        self.__intro = True
        while self.__intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__intro = False

            self.display_surf.fill(st.Settings.WHITE)
            self.display_surf.blit(self.background.image, self.background.rect)
            self.button('Go', 'Quit')

            pygame.display.update()

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def button(self, smg1, smg2, paus=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 100 + 150 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(self.display_surf,
                             st.Settings.BRIGHT_GREEN, st.Settings.button_play_cord)
            if (click[0] == 1) and (paus is None):
                self.__intro = False
            elif (click[0] == 1) and (paus is not None):
                self.__pause = not self.__pause
        else:
            pygame.draw.rect(self.display_surf,
                             st.Settings.GREEN, st.Settings.button_play_cord)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(smg1, smallText, st.Settings.BLACK)
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        self.display_surf.blit(textSurf, textRect)

        if 100 + 350 > mouse[0] > 350 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(self.display_surf,
                             st.Settings.BRIGHT_RED, st.Settings.button_exit_cord)
            if click[0] == 1 and paus is None:
                self.__intro = False
                self.__running = False
            elif click[0] == 1 and paus is not None:
                self.__intro = False
                self.__running = False
                self.__pause = False
        else:
            pygame.draw.rect(self.display_surf,
                             st.Settings.RED, st.Settings.button_exit_cord)
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(smg2, smallText, st.Settings.BLACK)
        textRect.center = ((350 + (100 / 2)), (450 + (50 / 2)))
        self.display_surf.blit(textSurf, textRect)

    def all(self):
        self.intro()
        self.game()

    def check(self, pocket):
        if pocket[0] is not None:
            self.__running = False
        elif pocket[1] is not None:
            self.__pause = not self.__pause
        elif pocket[2] is not None:
            self.my_sprite.set_index(pocket[2])

    def start(self):
        self.thread1 = threading.Thread(target=self.all)
        self.thread2 = threading.Thread(target=self.bot.listen)

        self.thread2.daemon = True
        self.thread1.start()
        self.thread2.start()
        self.thread1.join()

if __name__ == '__main__':
    app = App()
    app.start()