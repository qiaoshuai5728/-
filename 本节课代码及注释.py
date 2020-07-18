import pygame
import pygame.event
import pygame.time
import pygame.image
import pygame.display
import pygame.mouse
import pygame.draw

import random


'''
初始化
***********************************************************************************************
'''
pygame.init()

'''
***********************************************************************************************
'''


'''
定义需要使用的变量或对象
***********************************************************************************************
'''
timer = pygame.time.Clock()                             # 创建一个时钟timer，用来后边设置FPS

xiaoche = pygame.image.load("小汽车.jpg")               # 载入小汽车的图片


xiaoche_gao = 171
xiaoche_chang = 250
screenx = 1000      # 窗口宽度
screeny = 500       # 窗口高度
keepgoing = True    # 游戏是否正常运行
x = 1               # 图片起始x轴位置
y = 1               # 图片起始y轴位置
speedx = 5          # 左右移动速度
speedy = 5          # 上下移动速度

screen = pygame.display.set_mode((screenx, screeny))    # 创建一个名为screen的窗口
'''
***********************************************************************************************
'''


'''
游戏循环
***********************************************************************************************
'''
while keepgoing:                                   # 游戏循环
    for event in pygame.event.get():                # 点击关闭按钮后关闭程序
        if event.type == pygame.QUIT:               # 如果点击事件等于关闭事件
            keepgoing = False                       # 通过改变keepgoing变量来跳出循环，结束游戏

    mouse_x, mouse_y = pygame.mouse.get_pos()       # 获取鼠标的坐标，存放到mouse_x和mouse_y中

    if y + xiaoche_gao >= 500 or y <= 0:                   # 判断是否碰到窗口下边缘和上边缘
        speedx = random.randint(-5, 5)               # 碰到上下边缘，左右速度随机改变
        speedy = -speedy                            # 碰到上下边缘，上下速度反方向改变

    if x + xiaoche_chang >= 1000 or x <= 0:                  # 判断是否碰到窗口右边缘和左边缘
        speedy = random.randint(-5, 5)               # 碰到左右边缘，上下速度随机改变
        speedx = -speedx                            # 碰到左右边缘，左右速度反方向改变

    if y + xiaoche_gao >= 500:                             # 判断是否碰到窗口的下边缘
        if mouse_x > x and mouse_x < x + xiaoche_chang:      # 判断鼠标的x轴位置是否在图片x轴内部
            print("正确")
        else:                                      # 否则
            keepgoing = False                       # 通过改变keepgoing变量来跳出循环，结束游戏

    screen.fill((255, 255, 255))                      # 绘制白色背景，遮盖小车移动的残留
    screen.blit(xiaoche, (x, y))                      # 绘制小车
    pygame.display.update()                         # 刷新屏幕

    x = x + speedx                                  # 控制小车左右移动
    y = y + speedy                                  # 控制小车上下移动

    timer.tick(60)                                  # FPS为60帧/秒

'''
***********************************************************************************************
'''
