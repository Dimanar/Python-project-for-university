import pygame
from src.background import BackGround
from src.settings import Settings
from src.avatar import move
import sys
import pyganim

class App:
    def __init__(self):
        self.sett = Settings()
        self._size = self.weight, self.height = Settings().screen
        self.boltAnim = move[5]
        self.on_init()
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.background = BackGround(self.sett.back_picture, self.sett.back_picture_pos)

    def on_init(self):
        pygame.init()
        self.boltAnim.play()
        self.display_surf = pygame.display.set_mode(
            self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(self.sett.name_app)
        self.__running = True

    def clean(self):
        pygame.quit()
        sys.exit()

    def on_event(self, event):
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            self.boltAnim.loop = False
            self.__running = False
        if keys[pygame.K_q]:
            self.boltAnim.togglePause()
        if keys[pygame.K_w]:
            self.boltAnim.stop()
        if keys[pygame.K_1]:
            self.boltAnim = move[0]
            self.boltAnim.play()
        if keys[pygame.K_2]:
            self.boltAnim = move[1]
        if keys[pygame.K_3]:
            self.boltAnim = move[2]
        if keys[pygame.K_4]:
            self.boltAnim = move[3]
        if keys[pygame.K_5]:
            self.boltAnim = move[4]
        if keys[pygame.K_6]:
            self.boltAnim = move[5]
        if keys[pygame.K_7]:
            self.boltAnim = move[6]
        if keys[pygame.K_8]:
            self.boltAnim = move[7]
        if keys[pygame.K_9]:
            self.boltAnim = move[8]
        if keys[pygame.K_0]:
            self.boltAnim = move[9]

    def on_execute(self):
        self.on_init()
        while self.__running:

            self.display_surf.blit(self.background.image, self.background.rect)
            self.boltAnim.blit(self.display_surf, self.sett.position_avatar)

            pygame.time.delay(100)
            self.clock.tick(115)


            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.update()
        self.clean()


if __name__ == '__main__':
    app = App()
    app.on_execute()
