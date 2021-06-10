import pygame, random, sys, time

pygame.init()
screen = pygame.display.set_mode([1000, 400])
screen.fill((255, 255, 255))
radiusr = 0
arrradiusr = [0] * 10  # 圆的半径
arraddradiusr = [0] * 10  # 圆的半径增量
arrradiusbool = [False] * 10  # 圆是否存在   False代表该索引值下的圆不存在，True代表存在
arrradiusx = [0] * 10  # 圆的坐标x轴
arrradiusy = [0] * 10  # 圆的坐标y轴
RGBx = [0] * 10  # 颜色RGB值第一个值
RGBy = [0] * 10  # 颜色RGB值第二个值
RGBz = [0] * 10  # 颜色RGB值第三个值

while True:
    time.sleep(0.1)  # 0.1秒
    for event in pygame.event.get():  # 监听器
        if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
            num = arrradiusbool.index(False)   #获取圆不存在的索引值
            arrradiusbool[num] = True          #将该索引值的圆设置为存在
            arrradiusr[num] = 0                #该圆的半径设置为0
            arrradiusx[num], arrradiusy[num] = pygame.mouse.get_pos()        #获取鼠标坐标
            RGBx[num] = random.randint(0, 255)       #获取颜色值
            RGBy[num] = random.randint(0, 255)       #获取颜色值
            RGBz[num] = random.randint(0, 255)       #获取颜色值
            pygame.draw.circle(screen, pygame.Color(RGBx[num], RGBy[num], RGBz[num]),     #画圆
                               (arrradiusx[num], arrradiusy[num]), arrradiusr[num], 1)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(10):
        if arrradiusbool[i] == False:     #如果圆不存在则跳过循环
            pass
        else:
            if (arrradiusr[i] < random.randint(10, 50)):       #随机圆的大小
                arraddradiusr[i] = random.randint(0, 5)        #圆的随机半径增量
                arrradiusr[i] += arraddradiusr[i]
                pygame.draw.circle(screen, pygame.Color(RGBx[i], RGBy[i], RGBz[i]),     #画圆
                                   (arrradiusx[i], arrradiusy[i]), arrradiusr[i], 1)
            else:
                arrradiusbool[i] = False    #若圆已达到最大，这将该索引值的圆设置为不存在
    pygame.display.update()
