import pygame
from sprite import *
# import sys

pygame.init()

screen = pygame.display.set_mode((700, 700))

# 只是单纯的加载图片
hero = pygame.image.load("./飞机.jpg")
bg = pygame.image.load("haha.png")

# 设置图片的左上顶点离坐标顶点的距离， 和该飞机图像的宽，高（就是加载出来的图像的宽高）
herorect = pygame.Rect(150, 500, 500 , 20)



# 创建敌机的精灵
enemy = GameSprite("./enemy.jpg")
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)



# 将图片投在屏幕上
# screen.blit(hero, (0,0))
# pygame.display.set_caption("弹弹弹，小游戏！")


# while True:
# pygame.display.update()
   # pass
#    for event in pygame.event.get():

#        if event.type == pygame.QUIT:
#            print("退出游戏。。。")
#         pygame.quit()

#     pass
clock = pygame.time.Clock()

while True:
     for event in pygame.event.get():

         # 判断用户是否点击了关闭按钮
         if event.type == pygame.QUIT:
            print("退出游戏。。。")

            pygame.quit()
            exit()

# 指定循环体内部的代码执行频率
     clock.tick(10)

      # 修改飞机的位置
     herorect.y -=1

      # 判断飞机的位置
     if herorect.y <= 0:
         herorect.y = 700

      # 调用 bilt 方法绘制背景
     screen.blit(bg, (0,0))
      # 绘制 飞机
     screen.blit(hero, herorect)




      #   让精灵组调用两个方法
      #   updata -让组中的所有精灵更新位置
     enemy_group.update()

   #   draw -在screen绘制所有的精灵
     enemy_group.draw(screen)




     pygame.display.update()


pygame.quit()