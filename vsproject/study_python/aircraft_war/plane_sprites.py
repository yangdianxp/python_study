
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt = False):
        super().__init__("./aircraft_war/images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./aircraft_war/images/enemy1.png")
    def update(self):
        pass