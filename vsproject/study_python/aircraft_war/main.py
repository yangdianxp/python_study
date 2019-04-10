import pygame
from plane_sprites import *


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((480, 700))
    bg = pygame.image.load("./aircraft_war/images/background.png")
    hero = pygame.image.load("./aircraft_war/images/me1.png")
    clock = pygame.time.Clock()
    hero_rect = pygame.Rect(150, 300, 102, 126)

    enemy = GameSprite("./aircraft_war/images/enemy1.png")
    enemy1 = GameSprite("./aircraft_war/images/enemy1.png", 2)
    enemy_group = pygame.sprite.Group(enemy, enemy1)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出。。。")
                pygame.quit()
                exit()
        hero_rect.y -= 1
        if hero_rect.y <= -126:
            hero_rect.y = 700
        screen.blit(bg, (0, 0))
        screen.blit(hero, hero_rect)

        enemy_group.update()
        enemy_group.draw(screen)

        pygame.display.update()
        pass
    pygame.quit()

'''
print("游戏的代码。。。")
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 {} {}".format(hero_rect.x, hero_rect.y))
print("英雄的尺寸 {} {}".format(hero_rect.width, hero_rect.height))
print("{}".format(hero_rect.size))
'''