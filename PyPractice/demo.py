import pygame

pygame.init()

# 定义一个英雄模型
# hero_rect = pygame.Rect(100, 500, 160 , 120)
# print("英雄坐标 %d %d" % (hero_rect.x, hero_rect.y))
# print("英雄大小 %d %d" % (hero_rect.width, hero_rect.height))
# print("英雄大小 %d %d" % (hero_rect.size))

# 创建屏幕主窗口
screen = pygame.display.set_mode((700, 700))
# pygame.display.set_caption("demo测试")

# 引入一个图片
# bg = pygame.image.load("./未命名文件.png")
hero = pygame.image.load("./飞机.jpg")

# 将图片投在屏幕上
screen.blit(hero, (0,0))

# 更新显示，将之前绘制好的结果一次性投在屏幕上（可以想象成ps中的图层，一张盖着一张）


while True:
# # 设置屏幕刷新帧率，即每隔60秒刷新移动一下所有图像的位置
#     clock.tick(60)

# # 让英雄移动，当英雄飞出屏幕时，从另一边出来
#     hero_rect.y -= 1
#     if hero_rect.y <= 0:
#         hero_rect.y = 700

# # 绘制背景图片, 将图片显示在窗口的哪个位置
#     screen.blit(bg, (20,20))

# # 绘制英雄图片, 将英雄模型赋值给英雄图片
#     screen.blit(hero , hero_rect)
    # pygame.display.update()
    pass


# 游戏退出模块
while True:
     for event in pygame.event.get():

         # 判断用户是否点击了关闭按钮
         if event.type == pygame.QUIT:
            print("退出游戏。。。")

         pygame.quit()

         exit()



# 飞机动画模块
while True:
    # 指定循环体内部的代码执行频率
    clock.tick(60)

    # 修改飞机的位置
    hero_rect.y -=1

    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 调用 bilt 方法绘制图像
    screen.blit(bg, (0,0))
    screen.blit(hero, hero_rect)

    pygame.display.update()



pygame.quit()