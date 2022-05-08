import pygame

from sprite import *

pygame.init()

class PlaneGame(object):
    """飞机大战主游戏"""

    # 私有方法
    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        # 实例.方法
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建（私有方法需要以两个下划线开头）
        self.__creat_sprites()

        # 4.设置定时器事件  - 创建敌机  1s
        pygame.time.set_timer(pygame.USEREVENT, 1000)


    # 创建精灵组的方法
    def __creat_sprites(self):
        
        # 创建背景精灵(调用封装好的背景类Background)
        bg1 = Background("./战机.png")
        
        # 创建背景精灵组
        # 将背景精灵bg1（也可以传多个精灵）传递到精灵组内部
        # 在 __uodate__sprite 方法中让精灵组调用 updata 方法和 draw 方法
        self.back_group = pygame.sprite.Group(bg1)


        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
    

    # 事件监听的方法
    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                    # 调用静态方法
                     PlaneGame.__game_over()
                     pygame.quit()
                     print("退出游戏")
                     exit()
            
            # 创建敌机事件的监听
            elif event.type == CREAT_ENEMY_EVENT:
                print("敌机出场。。。")

                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

    

    # 碰撞检测的方法
    def __check_collide(self):
        pass


    # 更新/显示精灵组的方法
    def __update_sprate(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
    
    # 游戏结束的方法
    @staticmethod
    def __game_over():
        
        pass





    # 启动游戏的函数
    def start_game(self):
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PRE_SEC)

            # 2.事件监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新/绘制精灵组
            self.__update_sprate()

            # 5.更新显示
            pygame.display.update()

            
            pass
        print("游戏开始。。。")






if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()