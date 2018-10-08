# 开始界面：
#       0：背景图片  image.load()
#       1：浮动标题   image.load() >screen.blit(img,【x，y+sin()】)>>
#       2. 开始按钮   image.load() >mouse  event
#       3.下部喷气飞机 [image.load()......] >>screen.blit(img[index],【x，y】)
#       4.背景音乐
# 游戏界面
#      0：背景 ： #属性： 图片，屏幕       方法：循环移动
#      1：主角 ： #属性： 图片，屏幕，速度，血量 ，分数  方法： 移动 ， 碰撞 ，  死亡
#      1.1：主角的子弹： #属性： 图片，屏幕，速度，  方法： 移动 ， 碰撞 ，
#      2：敌机 ：#属性： 图片，屏幕，速度，血量  方法： 移动 ， 碰撞 ，  死亡

import pygame
import os
import sys
import math
import random

pygame.init()                                   # 初始化 pygame
pygame.display.init()                           # 初始化 display
screen = pygame.display.set_mode((480, 700))    # 设置窗口
pygame.display.set_caption("愤怒的马里奥")        # 标题文字
icon = pygame.image.load("resources/star.png")  # 左上缩略图
pygame.display.set_icon(icon)                   # 渲染缩略图


# 开始界面:用到的图片
startImgs = [
    pygame.image.load("resources/image/background3.png"),
    pygame.transform.scale(pygame.image.load(
            "resources/image/loading.png"), (480, 480)),
    pygame.image.load("resources/image/name2.png"),
    pygame.image.load("resources/image/start_menu.png"),
    pygame.image.load("resources/image/background4.png"),

]
# 开始界面:底部8张图
startBottomImgs = [
    pygame.image.load("resources/image/1.png"),
    pygame.image.load("resources/image/2.png"),
    pygame.image.load("resources/image/3.png"),
    pygame.image.load("resources/image/4.png"),
    pygame.image.load("resources/image/5.png"),
    pygame.image.load("resources/image/6.png"),
    pygame.image.load("resources/image/7.png"),
    pygame.image.load("resources/image/8.png")
]

# 结束界面：用到的图片
overImgs = [
    pygame.image.load("resources/image/gameover2.png")
]


# ***开始界面类***
class StartPanel:
    def __init__(self, startImgs, startBottomImgs, screen):
        self.startImgs = startImgs            # 背景的资源
        self.startBottoms = startBottomImgs   # 8个动图
        self.screen = screen                  # 屏幕
        self.nameY = 0                        # 浮动图片的sin（）

        self.bottomIndex = 0                  # 底部图片,索引
        self.i = 0                            # 计时
        self.isInRect = False                 # 鼠标,是否在按钮里

    def Show(self):
        # 渲染背景
        self.screen.blit(self.startImgs[0],
                         (0, 0))
        # 渲染圆环
        self.screen.blit(self.startImgs[1],
                         (0, 120))
        # 渲染 浮动 标题
        self.nameY += 0.05
        self.screen.blit(self.startImgs[2],
             (150, 80+50*math.sin(self.nameY)))
        # 渲染按钮
        self.screen.blit(self.startImgs[3],
                         (165, 335))

        # 渲染 底部8张图
        self.i += 1

        if self.bottomIndex == 8:
            self.bottomIndex = 0            # 8张图 索引 0...7
        self.screen.blit(self.startBottoms[self.bottomIndex],
                         (220, 580))
        if self.i % 8 == 0:                # 每隔8个画面 下一张
            self.bottomIndex += 1
            self.i = 0

class OverPanel:
    def __init__(self,overImgs, screen):
        self.overImgs = overImgs
        self.screen = screen

    def ShowShow(self):
        # 渲染背景
        self.screen.blit(self.overImgs[0],
                         (0, 0))

# ***游戏背景类***
class BackGround:
    def __init__(self, img, screen, speed):
        self.img1 = img
        self.rect1 = self.img1.get_rect()
        # print(1, self.rect1)

        self.img2 = self.img1.copy()        # 复制出一张新的
        self.rect2 = self.img2.get_rect()
        self.rect2.topleft = (0, -700)
        # print(2, self.rect2)
        self.screen = screen
        self.speed = speed

    def Move(self):
        # 此时是矩形移动
        self.rect1 = self.rect1.move(0, self.speed)
        self.rect2 = self.rect2.move(0, self.speed)

        # 交替
        if self.rect1.y > 700:
            self.rect1.y = self.rect2.y-700
        if self.rect2.y > 700:
            self.rect2.y = self.rect1.y-700

        # 渲染 图像
        self.screen.blit(self.img1, self.rect1)
        self.screen.blit(self.img2, self.rect2)

heroImgs = [
    pygame.image.load("resources/image/hero1.png"),
    pygame.image.load("resources/image/hero2.png"),
    pygame.image.load("resources/image/maliao.png")
]
heroDeathImgs = [
    pygame.image.load("resources/image/hero_blowup_n1.png"),
    pygame.image.load("resources/image/hero_blowup_n2.png"),
    pygame.image.load("resources/image/hero_blowup_n3.png"),
    pygame.image.load("resources/image/hero_blowup_n4.png")
]


# ***主角类***
class Hero(pygame.sprite.Sprite):
    up = False
    down = False
    left = False
    right = False

    # 属性： 图片，屏幕，速度，血量 ，分数,初始化位置
    def __init__(self, imgs, pos, screen, speed, hp, score) -> None:
        self.imgs = imgs
        self.image = imgs[0]
        self.rect = self.image.get_rect()       # 获得图片的矩形对象
        self.rect.topleft = pos                 # 设置初始位置
        self.pos = pos
        self.screen = screen
        self.speed = speed
        self.hp = hp
        self.score = score

        self.i = 0
        self.imgDisplay = True
        self.deathImgIndex = 0
        # self.bulletSound = AllSounds.PlaySound(1, -1)
        # self.bulletSound.set_volume(0)

    # 方法: 移动，碰撞，死亡
    def Move(self):
        global isPlay
        # 子弹音效声音
        # if isPlay:
        #     self.bulletSound.set_volume(1)
        # else:
        #     self.bulletSound.set_volume(0)

        if self.hp > 0:
            # 主角色移动
            if Hero.down:
                self.rect = self.rect.move(0, self.speed)
            if Hero.up:
                self.rect = self.rect.move(0, -self.speed)
            if Hero.right:
                self.rect = self.rect.move(self.speed, 0)
            if Hero.left:
                self.rect = self.rect.move(-self.speed, 0)

            # 约束区间
            if self.rect.x <= 0:
                self.rect.x = 0
            if self.rect.x >= 380:
                self.rect.x = 380
            if self.rect.y <= 0:
                self.rect.y = 0
            if self.rect.y >= 625:
                self.rect.y = 625

            # 切换喷气图片
            self.i += 1
            if self.i % 10 == 0:
                self.i = 0
                self.imgDisplay = not self.imgDisplay
                # 发射一颗子弹
                bullet_sound.play()
                Bullet(bulletImgs[1], self.rect.midtop, self.screen, 25)

            # 切换喷气图片
            if self.imgDisplay:
                self.screen.blit(self.imgs[2], self.rect)
            else:
                self.screen.blit(self.imgs[2], self.rect)

            # 实时监测 碰撞
            self.Collide()

        else:
            # self.bulletSound.set_volume(0)
            # 播放死亡动画
            self.i += 1
            self.screen.blit(heroDeathImgs[self.deathImgIndex], self.rect)
            if self.i % 7 == 0:
                self.i = 0
                self.deathImgIndex += 1
            if self.deathImgIndex == len(heroDeathImgs):
                self.deathImgIndex = 0
                # FontDisplay.Update(self.score)
                self.score = 0                  # 分数归零
                self.hp = 3                     # 血量还原
                pygame.time.wait(200)
                isPlay = False                  # 游戏结束，回到开始界面

    def Death(self):
        if self.score == 10:
            exit()
    def Collide(self):
        global isPlay
        temp = pygame.sprite.spritecollideany(self,
              enemyList, collided=pygame.sprite.collide_mask)
        if temp != None:
            temp.hp = 0                           # 敌机死亡
            self.hp -= 1                          # 主角减血
            if self.hp != 0:
                self.rect.topleft = self.pos      # 主角还原初始位置

# 子弹列表
bulletList = []
bulletImgs = [
    pygame.image.load("resources/image/bullet.png"),
    pygame.image.load("resources/image/bullet6.png"),
    pygame.image.load("resources/image/bullet2.png"),
    pygame.image.load("resources/image/bullet3.png")
]
# ***子弹类***
class Bullet(pygame.sprite.Sprite):
    # 属性： 图片，屏幕，速度，
    def __init__(self, image, pos, screen, speed):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = pos
        self.screen = screen
        self.speed = speed
        bulletList.append(self)    # 将自己添加到列表                 # 将自己添加到列表

    # 方法：移动，碰撞
    def Move(self):
        self.rect = self.rect.move(0, -self.speed)
        self.screen.blit(self.image, self.rect)

        # 超出画面 销毁子弹
        if self.rect.y < -50:
            if self in bulletList:
                bulletList.remove(self)
        # 移动时检测 碰撞
        self.Collide()

    # 子弹碰撞敌机
    def Collide(self):
        temp = pygame.sprite.spritecollideany(self,
              enemyList, collided=pygame.sprite.collide_mask)
        if temp != None:
            if self in bulletList:
                bulletList.remove(self)
            temp.hp -= 1
            # # 敌机死亡
            # if temp in enemyList:
            #     enemyList.remove(temp)

    # 所有的子弹移动
    @staticmethod
    def AllButtetMove():
        for i in bulletList:
            if i != None and isinstance(i, Bullet):
                i.Move()

# 敌机图片
enemy1 = [
    pygame.image.load("resources/image/enemy0.png"),
    pygame.image.load("resources/image/enemy0_down1.png"),
    pygame.image.load("resources/image/enemy0_down2.png"),
    pygame.image.load("resources/image/enemy0_down3.png"),
    pygame.image.load("resources/image/enemy0_down4.png")
]
enemy2 = [
    pygame.image.load("resources/image/enemy1.png"),
    pygame.image.load("resources/image/enemy1_down1.png"),
    pygame.image.load("resources/image/enemy1_down2.png"),
    pygame.image.load("resources/image/enemy1_down3.png"),
    pygame.image.load("resources/image/enemy1_down4.png")

]
enemy3 = [
    pygame.image.load("resources/image/enemy2.png"),
    pygame.image.load("resources/image/enemy2_down1.png"),
    pygame.image.load("resources/image/enemy2_down2.png"),
    pygame.image.load("resources/image/enemy2_down3.png"),
    pygame.image.load("resources/image/enemy2_down4.png"),
    pygame.image.load("resources/image/enemy2_down5.png"),
    pygame.image.load("resources/image/enemy2_down6.png")
]


# ***敌机类***
enemyList = []
class Enemy(pygame.sprite.Sprite):
    CreateIndex = 0                 # 用于产生敌机的变量

    # 属性:图片，屏幕，速度，血量, 标签
    def __init__(self, imgs, pos, screen, speed, hp, tag):
        self.imgs = imgs
        self.image = imgs[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.screen = screen
        self.speed = speed
        self.hp = hp
        self.tag = tag

        self.i = 0                  # 计时。7帧播放一个画面
        self.imgsIndex = 0
        enemyList.append(self)      # 将对象自己 放入列表

    def __str__(self):
        return "敌机"

    # 方法：移动,碰撞,死亡
    def Move(self):
        if self.hp > 0:
            self.rect = self.rect.move(0, self.speed)
            self.screen.blit(self.image, self.rect)

            # 超过画面销毁敌机
            if self.rect.y >= 700:
                if self in enemyList:
                    enemyList.remove(self)
        else:
            self.Death()

    def Collide(self):
        pass
    def Death(self):
        # 播放死亡动画
        self.i += 1
        self.screen.blit(self.imgs[self.imgsIndex], self.rect)
        if self.i % 2 == 0:
            self.i = 0
            self.imgsIndex += 1
            # 不能立马消失
            if self in enemyList and self.imgsIndex == len(self.imgs):
                AllSounds.PlaySound(2)
                if self.tag == "enemy1":
                    hero.score += 1
                elif self.tag == "enemy2":
                    hero.score += 3
                else:
                    hero.score += 10
                enemyList.remove(self)

    @staticmethod
    def RandomCreateEnemy(screen):

        Enemy.CreateIndex += 1
        if Enemy.CreateIndex % 30 == 0:     # 控制飞机产生数量
            Enemy.CreateIndex = 0
            randNum=random.randint(1, 100)
            if randNum <= 70:
                Enemy(enemy1, (random.randint(0, 429), -250), screen, 3, 1, "enemy1")
            elif randNum <= 90:
                Enemy(enemy2, (random.randint(0, 411), -250), screen, 2, 3, "enemy2")
            else:
                Enemy(enemy3, (random.randint(0, 315), -250), screen, 1, 10, "enemy3")

    @staticmethod
    def AllEnemyMove():
        for i in enemyList:
            if i != None and isinstance(i, Enemy):
                i.Move()

sounds = [
    pygame.mixer.Sound("resources/sound/button.ogg"),
    pygame.mixer.Sound("resources/sound/bullet.wav"),
    pygame.mixer.Sound("resources/sound/enemy0_down.wav"),
    pygame.mixer.Sound("resources/sound/use_bomb.ogg")
]

# 音效类
class AllSounds:
    @staticmethod
    def PlaySound(num, loop=0):
        sounds[num].play(loops=loop)
        return sounds[num]

# 字体显示
class FontDisplay:
    history = 0                                             # 历史成绩

    def __init__(self, font, size, screen):
        self.font = font
        self.size = size
        self.screen = screen

    def Show(self, pos, strA):
        tempFont = pygame.font.Font(self.font, self.size)   # 创建字体
        fontSurface = tempFont.render(strA,
                    True, pygame.Color("black"))            # 将文本转为 surface
        self.screen.blit(fontSurface, pos)                  # 渲染出来

    @staticmethod
    def StartUpateHistory(path="score.txt"):                # 每次开始都知道 历史成绩
        if os.path.exists(path):
            with open(path, "r") as f_r:
                FontDisplay.history = int(f_r.read())
        else:
            with open(path, "w") as f_w:
                f_w.write("0")
                FontDisplay.history = 0

    @staticmethod
    def Update(score, path="score.txt"):                    # 更新历史成绩
        if score > FontDisplay.history:
            # 更新
            with open(path, "w") as f_w:
                f_w.write(str(score))


# 创建字体对象
fontDisplay=FontDisplay("resources/font/Marker Felt.ttf",
                        25, screen)

# 创建英雄对象
hero = Hero(heroImgs, (200, 500), screen, 10, 3, 0)

# 游戏背景对象
backGround = BackGround(startImgs[4], screen, 1)

# 开始界面的对象
startPanel = StartPanel(startImgs, startBottomImgs, screen)
# 结束界面的对象
overPanel = OverPanel(overImgs, screen)

# 背景音乐
pygame.mixer.music.load("resources/sound/kaomianjin.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

bullet_sound = pygame.mixer.Sound(
    'resources/sound/bullet.wav')       # 子弹音效
bullet_sound.set_volume(0.9)

# 全局变量,是否开始游戏
isPlay = False
imgDisplay = False

# 添加时间控制
clock = pygame.time.Clock()

def Event():
    global isPlay  # 全局变量 isPlay
    # 所有的事件
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 鼠标事件：开始按钮
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 判断 鼠标位置 是否在 按钮里面
                startPanel.isInRect = \
                pygame.Rect(210, 350, 72, 72).collidepoint(pygame.mouse.get_pos())
                if startPanel.isInRect:
                    print("开始游戏")
                    # FontDisplay.StartUpateHistory()
                    enemyList.clear()
                    bulletList.clear()
                    hero.rect.topleft = (200, 500)
                    isPlay = True
                # isPlay = True

        # 键盘事件：英雄移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                enemyList.clear()
                bulletList.clear()
                hero.rect.topleft = (200, 500)
                hero.hp = 3
                hero.score = 0
                isPlay = False
            if event.key == pygame.K_SPACE:
                # 全屏爆炸
                hero.score -= 20
                for i in enemyList:
                    AllSounds.PlaySound(3)
                    i.hp = 0


            if event.key == pygame.K_ESCAPE:
                isPlay = False
            if event.key == pygame.K_UP:
                Hero.up = True
            if event.key == pygame.K_DOWN:
                Hero.down = True
            if event.key == pygame.K_LEFT:
                Hero.left = True
            if event.key == pygame.K_RIGHT:
                Hero.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Hero.up = False
            if event.key == pygame.K_DOWN:
                Hero.down = False
            if event.key == pygame.K_LEFT:
                Hero.left = False
            if event.key == pygame.K_RIGHT:
                Hero.right = False

            # 键盘事件-游戏播放暂停
            if event.key == pygame.K_s:
                print("按下了s键，触发事件")
                # 表示游戏继续与暂停是一组相反关系
                isPlay = not isPlay
                if isPlay:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()


def Main():
    global isPlay       # 全局变量 isPlay
    while True:
        # 处理所有事件
        Event()

        # 开始画面渲染
        if isPlay == False:
            startPanel.Show()       # 开始界面
            # overPanel.ShowShow()    # 结束界面
        else:
            screen.fill(pygame.__color_constructor(0, 255, 0, 0))
            # 背景移动
            backGround.Move()
            # 产生英雄
            hero.Move()
            # 移动所有子弹
            Bullet.AllButtetMove()
            # 产生敌机并移动
            Enemy.RandomCreateEnemy(screen)
            Enemy.AllEnemyMove()

            # 显示字体
            fontDisplay.Show((430, 5),
                             "HP:%s" % hero.hp)
            fontDisplay.Show((10, 5),
                             "Score:%s" % hero.score)
            # fontDisplay.Show((0, 30),
            #                  "History:%s" % FontDisplay.history)

        # 刷新游戏页面
        pygame.display.update()

        # 设置时间帧频
        clock.tick(60)
        print(hero.score)

# 程序的入口点
if __name__ == '__main__':
    Main()
