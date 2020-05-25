import pygame
import src.settings as st

class Avatar(pygame.sprite.Sprite):
    def __init__(self):
        super(Avatar, self).__init__()
        self.images = self.__create_image(self.__create_direct())
        self.index = 0
        self.index_move = 5
        self.image = self.images[self.index_move][self.index]
        self.rect = pygame.Rect(*st.Settings.position_avatar, 115, 132)

    def update(self):
        self.index += 1
        if self.index >= len(self.images[self.index_move]):
            self.index = 0
        self.image = self.images[self.index_move][self.index]

    def set_index(self, num):
        self.index_move = num if (num > -1) and (num < 10) else self.index_move

    def __create_direct(self):
        main_direct = '../image/image_part_0'
        result = []
        for x in range(1, 81):
            temp = '0' + str(x) if x < 10 else str(x)
            result.append(main_direct + temp + '.png')
        return result

    def __load(self, data):
        return [pygame.image.load(direct) for direct in data]

    def __create_image(self, direct):
        return [self.__load(direct[x:x+8]) for x in range(0, 80, 8)]

class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(st.Settings.back_picture)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = st.Settings.back_picture_pos
