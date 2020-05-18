class Settings:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        self.screen = (self.WIDTH, self.HEIGHT) = 600, 600
        self.back_picture = '../image/back_2.jpg'
        self.back_picture_pos = [-10, -10]
        self.position_avatar = (260, 325)
        self.name_app = 'Dancing girl'