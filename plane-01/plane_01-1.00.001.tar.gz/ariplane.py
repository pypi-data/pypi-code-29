import pygame
import sys,math,random,os
# 初始化
pygame.init()
pygame.display.init()

# 设置窗口
screen=pygame.display.set_mode((480,750))   # 窗口尺寸
pygame.display.set_caption("飞机大战") # 窗口标题
icon = pygame.image.load("Images\game_loading1.png")
pygame.display.set_icon(icon)   # 窗口图标

# 开始界面图片
startImges=[
    pygame.image.load(r"Images\img_bg_logo.jpg"),
    pygame.transform.scale(pygame.image.load("Images\loading.png"),(480,480)),
    pygame.image.load(r"Images\name.png"),
    pygame.image.load("Images\icon72x72.png")
]

# 开始界面底部三张图片
bottomImages=[
    pygame.image.load("Images\game_loading1.png"),
    pygame.image.load("Images\game_loading2.png"),
    pygame.image.load("Images\game_loading3.png"),
]

# 游戏背景图
backGroundImg=pygame.image.load(r"Images\bg_img_2.jpg")
bomImage=pygame.image.load(r"Images\bisha1.png")

# 英雄飞机图
heroImg=pygame.image.load("Images\hero.png")

# 子弹图片
bullets=[
    # pygame.image.load(r"Images\bullet1.png"),
    pygame.image.load(r"Images\bullet2.png"),
    pygame.image.load(r"Images\bullet3.png")
]

# 敌方飞机图
enemyImg1=[
    pygame.image.load("Images\enemy1.png"),
    pygame.image.load("Images\enemy2_down4.png")
]
enemyImg2=[
    pygame.image.load("Images\enemy2.png"),
    pygame.image.load("Images\enemy2_down1.png"),
    pygame.image.load("Images\enemy2_down2.png"),
    pygame.image.load("Images\enemy2_down3.png"),
    pygame.image.load("Images\enemy2_down4.png")
]

# 音效
sounds=[
    pygame.mixer.Sound("sounds/button.ogg"),
    pygame.mixer.Sound("sounds/bullet.wav"),
    pygame.mixer.Sound("sounds/enemy0_down.wav"),
    pygame.mixer.Sound("sounds/use_bomb.ogg"),
    pygame.mixer.Sound("sounds\game_over.ogg")
]


# 开始界面的类
class Start:
    def __init__(self,startImages,bottomImages,screen):
        self.startImages=startImages
        self.bottomImages=bottomImages
        self.screen=screen  # 屏幕

        self.nameY = 0 # 浮动标题的sin()
        self.bottomIndex = 0 # 底部图片的 索引
        self.i = 0 # 计时
        self.isInRect = False # 鼠标 是否在按钮里


    def Show(self):
        # 渲染背景
        self.screen.blit(self.startImages[0],(0,0))
        # 渲染圆环
        self.screen.blit(self.startImages[1],(0,150))
        # 渲染浮动标题
        self.nameY += 0.08
        self.screen.blit(self.startImages[2],(25,100+60*math.sin(self.nameY)))
        # 渲染按钮
        self.screen.blit(self.startImages[3],(210,350))

        # 渲染 底部三张图
        # self.bottomIndex += 1
        if self.bottomIndex == 3:
            self.bottomIndex = 0
        self.screen.blit(self.bottomImages[self.bottomIndex],(150,630))
        self.i += 1
        if self.i == 30:
            self.i=0
            self.bottomIndex += 1

# 游戏背景类
class BackGround:
    def __init__(self,image,screen,speed):
        self.image1 = image
        self.rect1 = self.image1.get_rect()

        self.image2 = self.image1.copy()
        self.rect2 = self.image2.get_rect()
        self.rect2.topleft = (0,-768)

        self.speed = speed
        self.screen = screen


    def Move(self):
        self.rect1 = self.rect1.move(0,self.speed)
        self.rect2 = self.rect2.move(0,self.speed)

        if self.rect1.y > 751:
            self.rect1.y = self.rect2.y - 768
        if self.rect2.y > 751:
            self.rect2.y = self.rect1.y - 768

        # 渲染背景
        self.screen.blit(self.image1,self.rect1)
        self.screen.blit(self.image2,self.rect2)

# 英雄飞机类
class Hero(pygame.sprite.Sprite):

    up = False
    down = False
    left = False
    right = False

    def __init__(self,image,pos,screen,speed,hp,score):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = pos
        self.screen = screen
        self.speed = speed
        self.hp = hp
        self.score = score

    def Move(self):
        # 飞机渲染
        self.screen.blit(self.image,self.rect)
        # 移动
        if Hero.down:
            self.rect = self.rect.move(0,self.speed)
        if Hero.up:
            self.rect = self.rect.move(0,-self.speed)
        if Hero.right:
            self.rect = self.rect.move(self.speed,0)
        if Hero.left:
            self.rect = self.rect.move(-self.speed,0)
        # 游戏边界约束
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 360:
            self.rect.x = 360
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 671:
            self.rect.y = 671

        self.Collide()

    def bom(self):
        boom=BOM(bomImage,screen,self.rect)


    def fire(self):
        bullet=Bullet(bullets,(self.rect.centerx-20,self.rect.y),screen,4)
        bullet=Bullet(bullets,(self.rect.centerx+20,self.rect.y),screen,4)
        # print("开火》》》》")

    def Collide(self):
        global isplay
        temp = pygame.sprite.spritecollideany(self,enemyList,collided=pygame.sprite.collide_mask)
        if temp != None:
            if temp in enemyList:
                temp.hp = 0
                # enemyList.remove(temp) # 敌机销毁
            # pygame.time.wait(10)       # 延时100毫秒
            self.hp -= 1
            AllSounds.PlaySound(4)
            if self.hp != 0:
                self.rect.topleft = self.pos  # 碰撞返回初始位置
            if self.hp ==0:
                FontDisplay.Update(self.score)
                self.hp=5
                self.score=0
                isplay = False

    def death(self):
        pass
class BOM(pygame.sprite.Sprite):
    def __init__(self,image,screen,pos):
        self.image = image
        self.screen = screen
        self.pos = pos
    def bom(self):
        self.screen.blit(self.image,(0,0))

# Bom=BOM(bomImage,screen,(0,0)) #爆炸对象

# 子弹类
bulletList=[]
class Bullet(pygame.sprite.Sprite):
    def __init__(self,images,pos,screen,speed):
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.screen = screen
        self.speed = speed

        bulletList.append(self)

    def Move(self):
        # 移动
        self.rect = self.rect.move(0,-self.speed)
        # 渲染
        self.screen.blit(self.image,self.rect)

        # 销毁
        if self.rect.y < -50:
            if self in bulletList:
                bulletList.remove(self)

        # 检测碰撞
        self.Collide()

    @staticmethod
    def AllButtetMove():
        for i in bulletList:
            if i != None and isinstance(i,Bullet):
                i.Move()

    # 子弹碰撞敌机
    def Collide(self):
        temp = pygame.sprite.spritecollideany(self,enemyList,collided=pygame.sprite.collide_mask)
        if temp != None:
            if self in bulletList:
                bulletList.remove(self)
                # 敌机掉血
            temp.hp -= 1
            # if temp in enemyList:
            #     enemyList.remove(temp)

# 敌方飞机类
enemyList=[]
class Enemy(pygame.sprite.Sprite):
    EnemyIndex = 0  # 控制敌机产生时间

    def __init__(self,images,pos,screen,speed,hp,num):
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.screen = screen
        self.speed = speed
        self.hp = hp
        self.num = num

        self.i = 0   # 敌机销毁计时
        self.enemyImageIndex = 0
        enemyList.append(self)

    def Move(self):
        if self.hp > 0:
            # 移动
            self.rect = self.rect.move(0,self.speed)
            # 渲染敌机
            self.screen.blit(self.image,self.rect)

            if self.rect.y>=760:
                if self in enemyList:
                    enemyList.remove(self)
        else:
            self.death()

    def death(self):
        self.i += 1
        self.screen.blit(self.images[self.enemyImageIndex],self.rect.topleft)
        if self.i == 3:
            self.i = 0
            self.enemyImageIndex += 1
        if self in enemyList and self.enemyImageIndex == len(self.images):
            AllSounds.PlaySound(2)
            if self.num == "enemy1":
                hero.score += 10
            else:
                hero.score += 30
            enemyList.remove(self)
            # print(hero.score)



    @staticmethod
    def RandomEnemy(screen):
        Enemy.EnemyIndex += 1
        if Enemy.EnemyIndex == 40:
            Enemy.EnemyIndex = 0
            num=random.randint(0,100)
            # print(num)
            if num <= 70:
                Enemy(enemyImg1,(random.randint(0,423),-100),screen,4,3,'enemy1')
                # print("敌机一")
            else:
                Enemy(enemyImg2, (random.randint(0,378),-100),screen,3,6,'enemy2')
                # print("22222222")

    @staticmethod
    def AllEnemyMove():
        for i in enemyList:
            if i != None and isinstance(i,Enemy):
                i.Move()

# 音效类
class AllSounds:
    @staticmethod
    def PlaySound(num,loop=0):
        sounds[num].play(loops=loop)
        return sounds[num]

# 字体类
class FontDisplay:
    history = 0 # 历史成绩

    def __init__(self,font,size,screen):
        self.font = font
        self.size = size
        self.screen = screen

    def Show(self,pos,strA):
        tempFont=pygame.font.Font(self.font,self.size) # 创建字体
        fontSurface=tempFont.render(strA,True,pygame.Color("black"))# 将文本转为 surface
        self.screen.blit(fontSurface,pos) # 渲染出来

    @staticmethod  # 创建外部文档
    def StartUpateHistory(path="score.txt"):
        if os.path.exists(path):
            with open(path,"r") as f_r:
                FontDisplay.history=int(f_r.read())
        else:
            with open(path,"w") as f_w:
                f_w.write("0")
                FontDisplay.history =0

    @staticmethod  # 更新历史成绩
    def Update(score,path="score.txt"):
        if score>FontDisplay.history:
            # 更新
            with open(path,"w") as f_w:
                f_w.write(str(score))


# 字体对象
fontDisplay=FontDisplay(r"font\feigungun.ttf",25,screen)


# 开始 界面的对象
Start=Start(startImges,bottomImages,screen)

# 背景音乐
pygame.mixer.music.load("sounds\game_music.mp3") # 加载音乐
pygame.mixer.music.play(-1)  # 循环播放
pygame.mixer.music.set_volume(0.5) # 音量调节

# 游戏背景对象
backGround = BackGround(backGroundImg,screen,2)

# 英雄飞机对象
hero=Hero(heroImg,(190,550),screen,5,5,0)

# 敌机对象
# ENEMY=Enemy(enemyImg1,(75,50),screen,1,2)

# 全局变量
isplay = False # 是否开始游戏
ismusic = True  # 是否暂停音乐

# 所有事件
def Event():
    global isplay,ismusic
    # 所有事件
    for event in pygame.event.get():  # 循环所有事件
        if event.type == pygame.QUIT:   # 退出事件
            pygame.quit()
            sys.exit()
        # 暂停音乐
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ismusic = not ismusic
                if ismusic:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()


        # 鼠标
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 判断鼠标位置 是否在按钮图片上
                Start.isInRect = pygame.Rect(210,350,72,72).collidepoint(pygame.mouse.get_pos())
                if Start.isInRect:
                    # print("开始游戏")
                    FontDisplay.StartUpateHistory()
                    enemyList.clear()
                    bulletList.clear()
                    isplay = True
        # 键盘
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isplay = False
            if event.key == pygame.K_j:
                hero.fire()
            if event.key == pygame.K_o: # 全部爆炸
                AllSounds.PlaySound(3)
                hero.bom()
                for i in enemyList:
                    i.hp = 0

        # 英雄飞机移动判断
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                Hero.up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Hero.down = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                Hero.left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                Hero.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                Hero.up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Hero.down = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                Hero.left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                Hero.right = False


# 主程序
def Main():
    global isplay
    while True:
        # 处理所有事件
        Event()
        # 画面渲染
        if isplay == False:
            Start.Show()
        else:
            # screen.fill(pygame.Color("red"))
            backGround.Move() # 进入的界面
            # 产生英雄
            hero.Move()
            # 子弹
            Bullet.AllButtetMove()
            # 产生敌机
            Enemy.RandomEnemy(screen)
            Enemy.AllEnemyMove()
            # 显示字体
            fontDisplay.Show((10,8),"血量：%s"%hero.hp)
            fontDisplay.Show((10,30),"分数：%s"%hero.score)
            fontDisplay.Show((10,55),"最高记录：%s"%FontDisplay.history)

        pygame.display.update()

#程序入口
if __name__ == "__main__":
    Main()
























