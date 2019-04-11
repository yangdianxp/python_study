import pygame
from plane_sprites import *

class PlaneGame:
    """飞机大战主游戏"""
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    def __create_sprites(self):
        bg1 = Background() 
        bg2 = Background(True) 
        self.back_group = pygame.sprite.Group(bg1, bg2)
    def start_game(self):
        print("游戏开始")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_spirites()
            pygame.display.update()
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场。。。")
    def __check_collide(self):
        pass
    def __update_spirites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()