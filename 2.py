import pygame
import pygame.display
import pygame.event
import pygame.image
import pygame.mixer_music
import pygame.mixer


# pygame库初始化
# ------------------------------------------------------------
pygame.init()       # 初始化
# ------------------------------------------------------------


# 载入需要使用到的图片
# ------------------------------------------------------------
background = pygame.image.load("background.png")        # 载入背景图片
player = pygame.image.load("player.png")                # 载入玩家图片
bullet = pygame.image.load("bullet.png")                # 载入子弹图片
enemy = pygame.image.load("enemy.png")                  # 载入敌人图片
ufo = pygame.image.load("ufo.png")                      # 载入标题图标
# ------------------------------------------------------------


# 载入及配置窗口
# ------------------------------------------------------------
screen = pygame.display.set_mode((800, 600))     # 载入一个和背景图片一样大的窗口
pygame.display.set_caption("大战外星人")         # 设置窗口标题为游戏名称
pygame.display.set_icon(ufo)                    # 设置游戏标题图标
# ------------------------------------------------------------


# 初始化所有需要的变量
# ------------------------------------------------------------
keepgoing = True                                    # 设置游戏循环的变量
playerX = 370                                       # 玩家角色图片的初始X轴坐标
playerY = 480                                       # 玩家角色图片的初始Y轴坐标
playerX_change = 0                                  # 玩家角色图片移动的速度或者理解为移动距离
enemyX = []                                         # 所有敌人的X轴坐标
enemyY = []                                         # 所有敌人的Y轴坐标
enemyX_change = []                                  # 所有敌人的X轴移动速度或理解为移动距离，用来控制左右移动
enemyY_change = []                                  # 所有敌人的Y轴移动速度或理解为移动距离，用来控制上下移动
num_of_enemies = 10                                 # 设置初始敌人飞船数量
bulletX = 0                                         # 子弹初始X轴位置
bulletY = 480                                       # 子弹初始Y轴位置
bulletX_change = 0                                  # 设置子弹X轴移动速度
bulletY_change = 10                                 # 设置子弹Y轴移动速度
bullet_state = "ready"                              # 子弹是否准备完毕
textX = 10                                          # 分数X轴坐标
testY = 10                                          # 分数Y轴坐标
score_value = 0                                     # 得分数值


# 载入背景音乐
# ------------------------------------------------------------
pygame.mixer_music.load("background.wav")    # 载入背景音乐
pygame.mixer_music.play(loops=-1)           # 设置背景音乐为循环播放


# 游戏循环
# ------------------------------------------------------------
while keepgoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False
