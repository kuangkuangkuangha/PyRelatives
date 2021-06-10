import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

imag = pygame.image.load("./飞机.jpg")

model = pygame.Rect(100, 500, 160, 120)

screen.blit(imag, (0,0))




while True:

    for event in pygame.event.get():

         # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏。。。")

            pygame.quit()
            exit()

    # hero_rect.y -= 1
    # if hero_rect.y <= 0:
    #     hero_rect.y = 700
    
    # screen.blit(imag, model)

    # pygame.display.update()

pygame.quit()