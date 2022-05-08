import pygame
import random

# 屏幕大小的常量
# x=0, y=0, 屏幕宽480， 高700
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 设置帧率
FRAME_PRE_SEC = 60
# 创建敌机事件常量
CREAT_ENEMY_EVENT = pygame.USEREVENT

# 创建游戏精灵类
class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self, image_name, speed = 1):
        
        # 调用父类的初始化方法
        super().__init__()
        
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


# 创建一个类Background, 继承了父类（GameSprite）
class Background(GameSprite):
    """游戏背景精灵"""

# 为啥要设置背景，？ 
# 答：继承父类提供的方法，不能满足子类的需求：
    # 1.派生一个子类
    # 2.在子类中针对特有的需求，重写父类的方法，并进行扩展


    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断图像是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

        pass

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./敌机.png")

        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)

        # 3.指定敌机的初始随机位置(垂直方向)
        self.rect.bottom = 0

        # max_x = SCREEN_RECT.width - self.rect.width

        self.rect.x = random.randint(0, 1000)

    def update(self):

        # 1.调用父类方法，保持垂直方向的飞行
        super().update()

        # 2.判断是否飞出屏幕，如果是，需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕，需要从精灵组中删除。。。")


# 定义一个类（传入继承的父类）
    # 1.里面有一个固定的__init__方法，可以通过self...进行一些属性（自己想点啥就点啥）定义
    # 2.还可以自行加入一些其他的方法，如update（）

