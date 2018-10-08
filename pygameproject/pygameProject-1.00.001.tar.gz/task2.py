import pygame
import sys,math,os
import random

pygame.init()
pygame.display.init()# 初始化display
# 设置窗口
screen=pygame.display.set_mode((480,768))
# 开始界面的图片
startImgs=[
    pygame.image.load("img_bg_level_5.jpg"),
    pygame.transform.scale(pygame.image.load("image/loading.png"),(480,480)),
    pygame.image.load("image/name.png"),
    pygame.image.load("image/icon72x72.png")
]
# 开始界面底部的照片
startBottomImgs=[ pygame.image.load("image/game_loading1.png"),
                  pygame.image.load("image/game_loading2.png"),
                  pygame.image.load("image/game_loading3.png")]
# 开始界面的类
class StartPanel:
    def __init__(self,startImgs,startBottomImgs,screen):
        self.startImgs = startImgs  # 开始界面用的图片
        self.startBottoms = startBottomImgs  # 开始界面底部用的三张图片
        self.screen = screen  # 屏幕窗口


        self.nameY=0# 浮动图片的sin()
        self.bottomIndex=0#底部图片 索引
        self.i=0# 计时
        self.isInRect=False # 鼠标是否在按钮里
    def Show(self):
        self.screen.blit(self.startImgs[0],(0,0))# 渲染背景
        self.screen.blit(self.startImgs[1],(0,150))#渲染 开始按钮
        # 渲染浮动标题
        self.nameY+=0.05
        self.screen.blit(self.startImgs[2],(25,100+80*math.sin(self.nameY)))
        self.screen.blit(self.startImgs[3],(210,350))# 渲染按钮
        #渲染底部三张图
        self.i+=1
        if self.bottomIndex==3:
            self.bottomIndex=0 #三张图 索引 0  1   2
        self.screen.blit(self.startBottoms[self.bottomIndex],(150,630))
        if self.i%17==0:  # 每隔17个画面 播放下一张
            self.bottomIndex += 1
            self.i=0
#  游戏背景类
class BackGround:

    def __init__(self,img,screen,speed):
        self.img1=img
        self.rect1=self.img1.get_rect()
        # print(1,self.rect1)

        self.img2=self.img1.copy() #复制图片
        self.rect2 = self.img2.get_rect()
        self.rect2.topleft=(0,-768)
        # print(2,self.rect2)
        self.screen=screen
        self.speed=speed
    def Move(self):
        #   矩形移动
        self.rect1=self.rect1.move(0,self.speed)
        self.rect2=self.rect2.move(0,self.speed)
        #  交替
        if self.rect1.y>760:
            self.rect1.y=self.rect2.y-768
        if self.rect2.y>760:
            self.rect2.y=self.rect1.y-768
        # 渲染图像
        self.screen.blit(self.img1,self.rect1)
        self.screen.blit(self.img2,self.rect2)

heroImgs=[
    pygame.image.load("image/hero1.png"),
    pygame.image.load("image/hero2.png")]
heroDeathImgs=[
    pygame.image.load("image/hero_blowup_n1.png"),
    pygame.image.load("image/hero_blowup_n2.png"),
    pygame.image.load("image/hero_blowup_n3.png"),
    pygame.image.load("image/hero_blowup_n4.png")]

# 主角类*************
class  Hero(pygame.sprite.Sprite):
    up=False
    down=False
    left=False
    right=False
    #属性；图片，屏幕，初始化位置，速度，血量，分数
    def __init__(self,imgs,pos,screen,speed,hp,score):
        self.imgs=imgs
        self.image=imgs[0]
        self.rect=self.image.get_rect()# 获得图片的矩形对象
        self.rect.topleft=pos# 设置初始位置
        self.pos=pos
        self.screen=screen
        self.speed = speed
        self.hp = hp
        self.score=score
        self.i=0
        self.imgDisply=True
        self.deathImgIndex = 0

        self.bulletSound = AllSounds.PlaySound(1, -1)
        self.bulletSound.set_volume(0)

    # 移动 碰撞 死亡
    def Move(self):
        global isPlay #全局变量
        #子弹音效声音
        if isPlay:
            self.bulletSound.set_volume(1)
        else:
            self.bulletSound.set_volume(0)
        if self.hp > 0:
            if Hero.down:
            # 移动
                self.rect=self.rect.move(0,self.speed)
            if Hero.up:
                self.rect = self.rect.move(0,-self.speed)
            if Hero.right:
                self.rect = self.rect.move(self.speed,0)
            if Hero.left:
                self.rect= self.rect.move(-self.speed,0)
            #约束 区间
            if self.rect.x<=0:
                self.rect.x=0
            if self.rect.x>=380:
                self.rect.x=380
            if self.rect.y<=0:
                self.rect.y=0
            if self.rect.y>=625:
                self.rect.y=625
            # 切换 喷气图片
            self.i+=1
            if self.i%7==0:
                self.i=0
                self.imgDisply = not self.imgDisply
            # 发射子弹
                Bullet(bulletImgs[1], self.rect.midtop, self.screen, 10)
            # 切换 喷气 图片
            if self.imgDisply:
                self.screen.blit(self.imgs[0], self.rect)
            else:
                self.screen.blit(self.imgs[1], self.rect)
            #  实时 检测 碰撞
            self.Collide()
        else:
            self.bulletSound.set_volume(0)
            # 播放死亡动画
            self.i += 1
            self.screen.blit(heroDeathImgs[self.deathImgIndex], self.rect)
            if self.i % 7 == 0:
                self.i = 0
                self.deathImgIndex += 1
                if self.deathImgIndex == len(heroDeathImgs):
                    self.deathImgIndex = 0
                    FontDisplay.Update(self.score)
                    self.score = 0  # 分数归零
                    self.hp = 3  # 血量还原
                    pygame.time.wait(200)
                    isPlay = False  # 游戏结束，回到开始界面

    def Death(self):
        pass
    def Collide(self):
        global isPlay
        temp = pygame.sprite.spritecollideany(self, enemyList, collided=pygame.sprite.collide_mask)
        if temp!= None:
            temp.hp = 0  # 敌机死亡
            self.hp -= 1  # 主角 减血
            if self.hp!= 0:
                self.rect.topleft = self.pos  # 主角还原初始位置

# 子弹列表
bulletList=[]
bulletImgs=[
    pygame.image.load("image/p-f01.png"),
    pygame.image.load("image/p-f02.png"),
    pygame.image.load("image/p-f03.png")
]
# 子弹类
class Bullet(pygame.sprite.Sprite):
    # 属性： 图片，屏幕，速度，
    def __init__(self,image,pos,screen,speed):
        self.image=image
        self.rect=image.get_rect()
        self.rect.center=pos
        self.screen=screen
        self.speed=speed
        bulletList.append(self) #将自己添加到列表

    #方法： 移动 ， 碰撞 ，
    def Move(self):
        self.rect=self.rect.move(0,-self.speed)
        self.screen.blit(self.image,self.rect)

        #超出画面 销毁子弹
        if self.rect.y<-50:
            if self in bulletList:
                bulletList.remove(self)
        #移动时检测 碰撞
        self.Collide()
    #子弹碰撞敌机
    def Collide(self):
        temp=pygame.sprite.spritecollideany(self,enemyList,collided=pygame.sprite.collide_mask)
        if temp!=None:
            if self in bulletList:
                bulletList.remove(self)
            temp.hp-=1
            #敌机死亡
            # if temp in enemyList:
            #     enemyList.remove(temp)
    # 所有子弹 移动
    @staticmethod
    def AllButtetMove():
        for i in bulletList:
            if i != None and isinstance(i, Bullet):
                i.Move()
# 敌机图片
enemy1=[
    pygame.image.load("image/enemy0.png"),
    pygame.image.load("image/enemy0_down1.png"),
    pygame.image.load("image/enemy0_down2.png"),
    pygame.image.load("image/enemy0_down3.png"),
    pygame.image.load("image/enemy0_down4.png"),
]
enemy2=[
    pygame.image.load("image/enemy1.png"),
    pygame.image.load("image/enemy1_down1.png"),
    pygame.image.load("image/enemy1_down2.png"),
    pygame.image.load("image/enemy1_down3.png"),
    pygame.image.load("image/enemy1_down4.png"),

]
enemy3=[
    pygame.image.load("image/enemy2.png"),
    pygame.image.load("image/enemy2_down1.png"),
    pygame.image.load("image/enemy2_down2.png"),
    pygame.image.load("image/enemy2_down3.png"),
    pygame.image.load("image/enemy2_down4.png"),
    pygame.image.load("image/enemy2_down5.png"),
    pygame.image.load("image/enemy2_down6.png")]
# 敌机类
enemyList=[]
class Enemy(pygame.sprite.Sprite):
    CreateIndex = 0 #用于产生敌机的变量


    # 属性： 图片，屏幕，速度，血量,标签
    def __init__(self,imgs,pos,screen,speed,hp,tag):
        self.imgs=imgs
        self.image=imgs[0]
        self.rect=self.image.get_rect()
        self.rect.topleft=pos
        self.screen=screen
        self.speed=speed
        self.hp=hp
        self.tag=tag

        self.i=0 #计时 7帧播放一个画面
        self.imgsIndex=0
        enemyList.append(self) #将对象自己 放入列表

    def __str__(self):
        return  "敌机"

    # 方法： 移动 ， 碰撞 ，  死亡
    def Move(self):
        if self.hp>0:
            self.rect = self.rect.move(0, self.speed)
            self.screen.blit(self.image, self.rect)

            # 超过画面销毁敌机
            if self.rect.y >= 760:
                if self in enemyList:
                    enemyList.remove(self)
        else:
            self.Death()

    def Collide(self):
        pass
    def Death(self):
        #播放死亡动画
        self.i+=1
        self.screen.blit(self.imgs[self.imgsIndex], self.rect)
        if self.i%2==0:
            self.i=0
            self.imgsIndex+=1
            # 不能立马消失
            if self in enemyList and self.imgsIndex==len(self.imgs):
                # AllSounds.PlaySound(2)
                if self.tag=="enemy1":
                    hero.score+=1
                elif self.tag=="enemy2":
                    hero.score += 3
                else:
                    hero.score += 10
                enemyList.remove(self)






    @staticmethod
    def RandomCreateEnemy(screen):

        Enemy.CreateIndex+=1
        if Enemy.CreateIndex%18==0:
            Enemy.CreateIndex=0
            randNum=random.randint(1,100)
            if randNum<=70:
                Enemy(enemy1,(random.randint(0,429),-250),screen,7,1,"enemy1")
            elif randNum<=90:
                Enemy(enemy2, (random.randint(0, 411), -250), screen, 5, 3, "enemy2")
            else:
                Enemy(enemy3, (random.randint(0,315), -250), screen, 1, 10, "enemy3")

    @staticmethod
    def AllEnemyMove():
        for i in enemyList:
            if i!=None and isinstance(i,Enemy):
                i.Move()

sounds=[
    pygame.mixer.Sound("sound/button.ogg"),
    pygame.mixer.Sound("sound/bullet.wav"),
    pygame.mixer.Sound("sound/enemy0_down.wav"),
    pygame.mixer.Sound("sound/use_bomb.ogg")
]
# 音效类d
class AllSounds:
    @staticmethod
    def PlaySound(num,loop=0):
        sounds[num].play(loops=loop)
        return sounds[num]
# 字体显示
class FontDisplay:
    history=0 #历史成绩


    def __init__(self,font,size,screen):
        self.font=font
        self.size=size
        self.screen=screen

    def Show(self,pos,strA):
        tempFont=pygame.font.Font(self.font,self.size) #创建字体
        fontSurface=tempFont.render(strA,True,pygame.Color("black"))#将文本转为 surface
        self.screen.blit(fontSurface,pos) #渲染出来

    @staticmethod
    def StartUpateHistory(path="score.txt"): #每次开始都知道 历史成绩
        if os.path.exists(path):
            with open(path,"r") as f_r:
                FontDisplay.history=int(f_r.read())
        else:
            with open(path,"w") as f_w:
                f_w.write("0")
                FontDisplay.history =0



    @staticmethod
    def Update(score,path="score.txt"): #更新历史成绩
        if score>FontDisplay.history:
            #更新
            with open(path,"w") as f_w:
                f_w.write(str(score))
#创建字体对象
fontDisplay=FontDisplay("MarkerFelt.ttf",25,screen)


# 创建英雄对象
hero=Hero(heroImgs,(200,600),screen,10,3,0)
# 游戏背景对象
backGround=BackGround(startImgs[0],screen,3)



# 开始界面的对象
startPanel = StartPanel(startImgs, startBottomImgs, screen)
#全局变量   是否开始游戏
isPlay=False
#添加时间控制
clock=pygame.time.Clock()

def Event():
    global isPlay  # 全局变量 isPlay
    # 所有的事件
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 鼠标
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 判断 鼠标位置 是否 在 按钮里面
                startPanel.isInRect = pygame.Rect(210,350,72,72).collidepoint(pygame.mouse.get_pos())
                if startPanel.isInRect:
                    print("开始游戏")
                    isPlay = True
        #  键盘
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
                for i in enemyList:
                    AllSounds.PlaySound(3)
                    i.hp = 0
            if event.key == pygame.K_w:
                Hero.up = True
            if event.key == pygame.K_s:
                Hero.down = True
            if event.key == pygame.K_a:
                Hero.left = True
            if event.key == pygame.K_d:
                Hero.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Hero.up = False
            if event.key == pygame.K_s:
                Hero.down = False
            if event.key == pygame.K_a:
                Hero.left = False
            if event.key == pygame.K_d:
                Hero.right = False

# t=Enemy(enemy1,(200,100),screen,10,10,1)
def Main():
    global  isPlay #全局变量  isPlay
    while True:
        # 处理所有事件
        Event()


        # 开始画面渲染
        if isPlay == False:
            startPanel.Show()
        else:

            # 背景 移动
            backGround.Move()
            # 产生英雄
            hero.Move()
            # 移动所有子弹
            Bullet.AllButtetMove()
            # 产生敌机并移动
            # t.move()
            Enemy.RandomCreateEnemy(screen)
            Enemy.AllEnemyMove()

            # 显示字体
            fontDisplay.Show((10, 10), "HP:%s" % hero.hp)
            fontDisplay.Show((10, 35), "Score:%s" % hero.score)
            fontDisplay.Show((10, 65), "History:%s" % FontDisplay.history)

        pygame.display.update()
        # 设置时间帧频
        clock.tick(60)

        print(hero.score)

#  加载音乐
pygame.mixer.music.load("Richard - 爱的纪念.mp3")
pygame.mixer.music.play()
# 程序的入口点
if __name__ == '__main__':
    Main()










