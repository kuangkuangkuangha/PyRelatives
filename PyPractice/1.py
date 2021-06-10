#+++++++++++++++++++++++模块导入+++++++++++++++++++++++++++++++++++++++++++++++
# 导入模块
# Pygame是专为电子游戏设计的跨平台Python模块，包含图像、声音。允许实时电子游戏研发
#而无需被低级语言（如机器语言和汇编语言）束缚，所以用起来非常简单；
# 计算旋转角度的时候用到了math模块中的反正切函数；
# random主要用来生成随机数，引用randint
import pygame
import math
import random

#+++++++++++++++++++++初始化参数及设置+++++++++++++++++++++++++++++++++++++++++
# 初始化参数
MovementSpeed = 50              # 主角色移动速度
CannonballSpeed = 30            # 炮弹移动速度
CatSpeed = 7                    # 猫的移动速度（通过按键WSAD实现上下左右移动）
width, height = 1600, 900       # 游戏窗口大小
width1, height1 = 200, 95       # 主角色大小（像素值）
width2, height2 = 150, 123      # 猫的大小
TotalTime = 90                  # 设置游戏时间，以秒为单位

badtimer=100                    # 计数器：badtimer和badtimer1共同实现计数功能，控制猫出现的频率和时间
badtimer1=0

TotalHealthvalue=200            # 主角色初始生命值
healthvalue = TotalHealthvalue

# cats是一个嵌套的列表，每一个元素代表一个猫或者非猫角色，包含三个维度：前两个维度决定位置，最后一个维度标记角色种类
cats=[[640,100,0]]              # 初始元素指定了游戏开始时第一个猫出现的位置
acc=[0,0]                       # 炮弹计数（用来计算准确率），第一个元素是打中猫的数目，第二个是炮弹总数
cannonballs=[]                  # 炮弹列表，结构类似于cats，嵌套列表
HorizontalAxis, VerticalAxis = width1/2, height/2  # 主角色初始位置（主角色中心点的位置？）
playerpos=[HorizontalAxis, VerticalAxis]

keys = [False, False, False, False]                # 按键设置

#++++++++++++++++++游戏窗口初始化及素材导入+++++++++++++++++++++++++++++++++++++
# 初始化游戏窗口以及各种图片素材的导入
pygame.init()                        
screen=pygame.display.set_mode((width, height))
background = pygame.image.load("pic/background.png")          # 背景图片
badfish = pygame.image.load("pic/badfish.png")                # 主角色图片

cannonballimg1 = pygame.image.load("pic/cannonball1.png")     # 为了趣味性设置了五种不同的炮弹
cannonballimg2 = pygame.image.load("pic/cannonball2.png")
cannonballimg3 = pygame.image.load("pic/cannonball3.png")
cannonballimg4 = pygame.image.load("pic/cannonball4.png")
cannonballimg5 = pygame.image.load("pic/cannonball5.png")
cannonballimgs = [cannonballimg1,cannonballimg2,cannonballimg3,cannonballimg4,cannonballimg5]

catimg = pygame.image.load("pic/cat.png")                    # 猫的图片
pipishrimpimg = pygame.image.load("pic/pipishrimp.png")      # 皮皮虾
tortoiseimg = pygame.image.load("pic/tortoise.png")          # 乌龟
conchimg = pygame.image.load("pic/conch.png")                # 海螺
crabimg = pygame.image.load("pic/crab.png")                  # 螃蟹
fishimg = pygame.image.load("pic/fish.png")                  # 小鱼
animalimgs = [catimg, pipishrimpimg, tortoiseimg, conchimg, crabimg, fishimg]

healthbar = pygame.image.load("pic/healthbar.png")           # 健康值横条
healthimg = pygame.image.load("pic/health.png")

gameover = pygame.image.load("pic/gameover.png")             # 游戏结束判定输赢后显示的图片
youwin = pygame.image.load("pic/youwin.png")

#+++++++++++++++++++游戏运行主体+++++++++++++++++++++++++++++++++++++++++++++++
exitcode = 0   # 输赢判定标志
running = 1    # 循环启动子
# 主循环
while running: 
    badtimer-=1
    screen.fill(0)                        # 在重新绘制之前清除屏幕
    screen.blit(background, (0,0))        # 绘制屏幕窗口背景
    # 处理主角色旋转
    position = pygame.mouse.get_pos()     # 获取鼠标位置
    angle = math.atan2( position[1]-playerpos[1], position[0]-playerpos[0] )    # 计算旋转角度
    playerrot = pygame.transform.rotate(badfish, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)     # 重新计算主角色位置
    screen.blit(playerrot, playerpos1)   # 将旋转后主角色显示在屏幕上
    
    # 炮弹
    for cannonball in cannonballs:
        index=0
        # 炮弹移动速度（横轴和纵轴上两个分量）
        velx=math.cos(cannonball[0])*CannonballSpeed
        vely=math.sin(cannonball[0])*CannonballSpeed
        cannonball[1]+=velx
        cannonball[2]+=vely   
        # 控制炮弹在一定范围（基本等同于游戏窗口的范围）内，出了这个限定范围就会被删除
        if cannonball[1]<-width1 or cannonball[1]>width or cannonball[2]<-height1 or cannonball[2]>height:
            cannonballs.pop(index)
    # 获得转向后的图片并显示
    for cannonball in cannonballs:
        cannonballimg = cannonballimgs[ cannonball[3] ]     # 当前炮弹样式（炮弹生成的时候决定的）
        cannonball1 = pygame.transform.rotate(cannonballimg, 360-cannonball[0]*57.29)
        screen.blit(cannonball1, (cannonball[1], cannonball[2]))
    
    # 添加猫
    if badtimer==0:
        mark = random.randint(0,19)  
        if mark > 5:    # 以一定的概率（四分之一）出现非猫角色，角色出现的种类随机
            mark = 0    # 标记角色种类（猫或者非猫中的某一种）
        cats.append([width, random.randint(0,height-height2), mark])
        # badtimer和badtimer1联合控制添加猫的时间和频率，一开始出现速度逐渐增加，最后稳定到一定的水平，间接控制游戏难度逐渐增大
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
            
    index=0
    for cat in cats:
        if cat[0]<-width2:              # 猫移动到屏幕边界外后删除
            cats.pop(index)
        if cat[2] != 0:
            MoveSpeed = CatSpeed*1.3    # 控制非猫角色移动速度为猫的1.3倍
        else:
            MoveSpeed = CatSpeed
        # 猫（横向往左）移动，速度为MoveSpeed，这时候没有真正移动，等到运行到更新显示到屏幕的时候，眼睛看到移动  
        cat[0]-=MoveSpeed
        # 漏网之猫（降低你的生命值）
        catrect=pygame.Rect(catimg.get_rect())    # 获取猫（或者非猫角色）当前的位置
        catrect.top=cat[1]
        catrect.left=cat[0]
        if catrect.left<-width2:                  # 猫移动到屏幕边界外后删除
            if cat[2]==0:                         # 如果是漏网之猫，则随机减掉一些生命值（5到20之间，改变该出设置可以调节游戏难度）
                healthvalue -= random.randint(5,20)
            cats.pop(index)
        # kill猫
        index1=0    # 炮弹计数
        # 调节碰撞的精度（尽可能从游戏窗口看到炮弹和猫接触后再判断为碰撞并删除炮弹和猫，提升游戏体验）
        Acc_Left = catrect.left+20
        Acc_Top = catrect.top+20
        Acc_Width = catrect.width-40
        Acc_Height = catrect.height-40
        CatrectAdj = pygame.Rect(Acc_Left,Acc_Top,Acc_Width,Acc_Height)    # 调整后的猫的位置，不影响游戏窗口显示猫出现的位置，只用来判断
        # 处理碰撞，删除猫和炮弹，天正精确度
        for cannonball in cannonballs:
            ballrect=pygame.Rect(cannonballimg.get_rect())
            ballrect.left=cannonball[1]
            ballrect.top=cannonball[2]
            if CatrectAdj.colliderect(ballrect):
                if cat[2]==0:     # 如果打中的是一只猫，则精确度加1，如果打中的是非猫角色，则直接删除，精确度按未打中计算
                    acc[0]+=1
                cats.pop(index)
                cannonballs.pop(index1)
            index1+=1
        # 处理直接碰撞到猫（主角色吃到食物，增加生命值，删除食物）
        if CatrectAdj.colliderect( pygame.Rect(playerpos[0]-50,playerpos[1]-50,80,80) ):
            if cat[2]==0:    # 如果碰到猫（被猫咬了），大幅度减少生命值（降为现有生命值的二分之一）
                healthvalue //= 2
            else:# 如果不是猫，请去吃了它，并随机增加3-8个生命值，生命值已满的时候，不再增加
                if TotalHealthvalue-healthvalue < 8:
                    healthvalue = TotalHealthvalue
                else:
                    healthvalue+=random.randint(3,8)
            cats.pop(index)
            
        # 下一只猫
        index+=1
        for cat in cats:
            img = animalimgs[cat[2]]
            screen.blit(img, cat[0:2]) # 显示到游戏窗口中
            
    # 显示游戏剩余时间
    font = pygame.font.Font(None, 30)                      # 设置字号
    Time_Left = TotalTime-pygame.time.get_ticks()//1000    # 剩余时间，以秒为单位
    # 设置显示的内容（中文显示容易出现异常，没有过多研究）
    survivedtext = font.render( "Time Left: " + str(Time_Left) + "s", True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[width-250,12]                       # 设置显示位置
    screen.blit(survivedtext, textRect)
     
    # 显示生命值
    screen.blit(healthbar, (width-220,10))                # 红色底条的位置
    for health1 in range(healthvalue):
        screen.blit(healthimg, (health1+width-217,13))    #绿色顶条的位置及滑动显示
    font = pygame.font.Font(None, 30)                     # 设置字号
    if healthvalue<0:                                     # 避免进度条显示负值
        healthvalue=0
    survivedtext = font.render( str(healthvalue) + '/' + str(TotalHealthvalue), True, (0,0,0))# 设置显示的内容
    textRect = survivedtext.get_rect()
    textRect.topright=[width-25,12]                       # 设置显示位置
    screen.blit(survivedtext, textRect)
    
    # 更新显示到屏幕（前面很多的控制，都是通过这一步才最终表现到游戏窗口中）
    pygame.display.flip()
    
    # 获取键盘或鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:    # 点击游戏窗口红叉就退出
            pygame.quit()
            exit(0)
        # 获取键盘事件，按下或者松开，按了什么键
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        # 鼠标事件，增加炮弹
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()    # 获取鼠标位置
            acc[1]+=1                          # 炮弹总数+1
            cannonballs.append( [ math.atan2(position[1]-(playerpos1[1]+width1/2),position[0]-(playerpos1[0]+height1/2)), playerpos1[0]+width1/2, playerpos1[1]+height1/2, random.randint(0,4) ] )
    # 控制主角色移动（限制移动范围）
    if keys[0] and playerpos[1]-height1/2>=MovementSpeed:                   # W
        playerpos[1]-=MovementSpeed
    elif keys[2] and height-playerpos[1]-height1/2>=MovementSpeed:          # S
        playerpos[1]+=MovementSpeed
    if keys[1] and playerpos[0]-width1/2>=MovementSpeed:                    # A
        playerpos[0]-=MovementSpeed
    elif keys[3] and width*0.15-playerpos[0]-width1/2 >= -MovementSpeed:    # D
        playerpos[0]+=MovementSpeed
        
    # 判断输赢
    if pygame.time.get_ticks()>=TotalTime*1000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:    # 计算精确度
        accuracy='%.2f%%' % (acc[0]*1.0/acc[1]*100)
    else:
        accuracy='%.2f%%' % 0
        
#++++++++++++++++++游戏结束后需要干的事儿+++++++++++++++++++++++++++++++++++++++
# 显示输赢
if exitcode==0:    # 输掉游戏
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    text = font.render("Accuracy: "+accuracy, True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:              # 赢了游戏
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    text = font.render("Accuracy: "+accuracy, True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
    
# 等待关闭游戏窗口（点红叉）
while 1:
    for event in pygame.event.get():
        # 点击窗口红叉就退出
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()