import pygame
import sys

pygame.init()

# 创建屏幕主窗口
screen = pygame.display.set_mode((700, 700))
# pygame.display.set_caption("demo测试")

# 引入一个图片

hero = pygame.image.load("./飞机.jpg")

# 将图片投在屏幕上
screen.blit(hero, (0,0))

# # 游戏退出模块
while True:
   pygame.display.update()
   pass

while True:
   for event in pygame.event.get():

         # 判断用户是否点击了关闭按钮
         if event.type == pygame.QUIT:
            print("退出游戏。。。")

            #pygame.display.update()
            sys.exit()

         # pygame.display.update()
         pygame.quit()

         
        


pygame.quit()