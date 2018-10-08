'''
version08：背景切换
wdj
'''

import pygame,random


#引入字体模块

pygame.init()
pygame.font.init()
game_font = pygame.font.SysFont("宋体",30,True)
pygame.display.set_caption("飞机大战")
#scene = pygame.display.set_mode([500,500])

#引入音乐模块
pygame.mixer.init()
pygame.mixer.music.load("./images/beijing_music02.mp3")
pygame.mixer.music.play()
sound1 = pygame.mixer.Sound("./images/bullet01.wav")
sound2 = pygame.mixer.Sound("./images/boom.wav")

#定义需要的常量
#分数
score = 0
#血量
HP = 5
SCREEN_SIZE = (500,834)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)

#爆炸
boom0 = 0
#z自定义一个事件
ENEMY_CREATE = pygame.USEREVENT

#创建游戏精灵类型
class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_path,speed = 8):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''
        通用移动
        :return:
        '''
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):
    '''背景精灵'''
    def __init__(self,prepare = False):
        super().__init__("./images/img_bg_6.png",speed = 2)

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]
    def update(self):
        #调用父类的update让其移动
        super().update()
        #判断位置
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class BackgroundSprite1(GameSprite):
    '''背景精灵'''
    def __init__(self,prepare = False):
        super().__init__("./images/img_bg_7.jpg",speed = 3)

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]
    def update(self):
        #调用父类的update让其移动
        super().update()
        #判断位置
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


#创建英雄精灵对象
class HeroSprite(GameSprite):

    def __init__(self):
        #初始化英雄飞机的图片，速度
        super().__init__("./images/hero12.png",speed = 8)
        #初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200

        self.bullets = pygame.sprite.Group()

    #边界判断
    def update(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    #飞机攻击
    def fire(self):
        #创建子弹对象
        bullet = BulletSprite01(self.rect.centerx - 14,self.rect.y-20,speed=-8)

        self.bullets.add(bullet)



#创建己方英雄子弹精灵对象
class BulletSprite01(GameSprite):
    def __init__(self,x,y,speed):
        super().__init__("./images/bullet11.png")
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        super().update()
        #边界判断
        if self.rect.y <= -self.rect.height:
            self.kill()

    def __del__(self):
        print("子弹对象已经销毁")





class EnemySprite(GameSprite):
    '''敌方飞机'''
    def __init__(self,image_path):
        #初始化敌方飞机的数据
        super().__init__(image_path,speed = random.randint(5,7))
        # super().__init__("./images/diji01.png",speed = random.randint(3,5))
        #初始化敌方飞机的位置
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

        self.bullets1 = pygame.sprite.Group()


    def update(self):
        #调用父类的方法直接运动
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.destory()
    #展示爆炸效果
    def destory(self):
        for image_path in ["./images/boom01.png","./images/boom02.png","./images/boom03.png",\
                           "./images/boom04.png","./images/boom05.png","./images/boom06.png",\
                           "./images/boom07.png","./images/boom08.png","./images/boom09.png",\
                           "./images/boom01.png","./images/boom02.png","./images/boom03.png"]:
            self.image = pygame.image.load(image_path)
            screen.blit(self.image,(self.rect.x,self.rect.y))
            pygame.display.update()
    print("展示爆炸效果")

    # 敌方飞机攻击
    def fire(self):
        # 创建子弹对象
        bullet1 = BulletSprite02(self.rect.centerx, self.rect.y,speed=20)

        self.bullets1.add(bullet1)

# 创建敌方子弹精灵对象
class BulletSprite02(GameSprite):
    def __init__(self, x, y, speed):
        super().__init__("./images/bullet13.png")
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

#初始化模块
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

#渲染背景
bg1 = BackgroundSprite()
bg2 = BackgroundSprite(prepare=True)

bg3 = BackgroundSprite1()
bg4 = BackgroundSprite1(prepare = True)
#bg2.rect.y = -SCREEN_SIZE[1]

#定义英雄飞机对象
hero = HeroSprite()

enemy =EnemySprite("./images/diji01.png")
enemy1 =EnemySprite("./images/diji02.png")
enemy2 =EnemySprite("./images/diji03.png")
enemy3 =EnemySprite("./images/diji04.png")


#添加到精灵组
resources = pygame.sprite.Group(bg1,bg2,hero)
resources1 = pygame.sprite.Group(bg3,bg4,hero)
#定义一个敌人飞机的精灵组对象
enemys = pygame.sprite.Group()
#间隔一定的时间，触发一次创建敌机的事件
pygame.time.set_timer(ENEMY_CREATE,2000)

#背景音乐
# pygame.mixer.music.play()

#首页
screen1 = pygame.display.set_mode((500,834),0,32)
menu_image = pygame.image.load("./images/menu00.png")
screen.blit(menu_image,(0,0))
pygame.display.update()
a =  False
while True:
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

        for event in event_list:
            # 如果当前事件是QUIT事件
            if event.type == pygame.QUIT:
                # 卸载所有pygame资源，退出程序
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and 245 <= event.pos[0] <= 280 and \
                    460 <= event.pos[1] <= 500:
                a = True
    if a == True:
        break


#定义一个时钟对象
clock = pygame.time.Clock()

#游戏场景循环
while True:

    #定义时钟的刷新帧，每秒循环多少次
    clock.tick(24)
    #监听所有的事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

        for event in event_list:
            #如果当前事件是QUIT事件
            if event.type == pygame.QUIT:
                #卸载所有pygame资源，退出程序
                pygame.quit()
                exit()

            if event.type == ENEMY_CREATE:
                print("创建一架敌机")
                enemy = EnemySprite("./images/diji01.png")
                enemy1 = EnemySprite("./images/diji02.png")
                enemys.add(enemy)
                enemys.add(enemy1)
                enemy.fire()
                enemy1.fire()


    key_down = pygame.key.get_pressed()

    if key_down[pygame.K_LEFT]:
        print("←←←←←←←←←左")
        hero.rect.x -= 8
    elif key_down[pygame.K_RIGHT]:
        print("右→→→→→→→→")
        hero.rect.x += 8
    elif key_down[pygame.K_DOWN]:
        print("下↓↓↓↓↓↓↓↓↓↓↓")
        hero.rect.y += 8
    elif key_down[pygame.K_UP]:
        print("上↑↑↑↑↑↑↑↑↑↑")
        hero.rect.y -= 8
    elif key_down[pygame.K_SPACE]:
        hero.fire()
        sound1.play()
        print("开火!!!!!!!!!!!!")



    # 碰撞检测
    pygame.sprite.groupcollide(hero.bullets, enemy.bullets1, True, True)
    if pygame.sprite.groupcollide(hero.bullets, enemys, True, True):
        #加入音乐，加入分数
        sound2.play()
        score += 100

        if score >= 1000:
            break

    c = pygame.sprite.spritecollide(hero,enemy.bullets1, True)
    if len(c) > 0:
        HP -= 1
        if HP < 0:
            hero.kill()
            pygame.quit()
            exit()

    #碰撞检测，飞机和飞机
    e = pygame.sprite.spritecollide(hero,enemys,True)
    if len(e) > 0:
        hero.kill()
        pygame.quit()
        exit()
    #精灵组渲染
    resources.update()
    resources.draw(screen)

    #字体渲染
    HP_text = game_font.render("HP:%s" % HP, True, [0, 255, 255])
    screen.blit(HP_text, (420, 5))
    score_text = game_font.render("SCORE:%s" % score, True, [255, 255, 0])
    screen.blit(score_text, (10, 5))

    #子弹精灵组渲染
    hero.bullets.update()
    hero.bullets.draw(screen)

    enemy.bullets1.update()
    enemy.bullets1.draw(screen)


    #渲染敌机精灵组中的所有飞机
    enemys.update()
    enemys.draw(screen)

    #窗口渲染展示
    pygame.display.update()

#第二关


# 游戏场景循环
while True:

    #播放声音




    # bg3 = BackgroundSprite1()
    # bg4 = BackgroundSprite1(prepare = True)
    # 定义时钟的刷新帧，每秒循环多少次
    clock.tick(30)

    # 监听所有的事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

        for event in event_list:
            # 如果当前事件是QUIT事件
            if event.type == pygame.QUIT:
                # 卸载所有pygame资源，退出程序
                pygame.quit()
                exit()

            if event.type == ENEMY_CREATE:
                print("创建一架敌机")
                enemy2 = EnemySprite("./images/diji03.png")
                enemy3 = EnemySprite("./images/diji04.png")
                enemys.add(enemy2)
                enemys.add(enemy3)
                enemy2.fire()
                enemy3.fire()

    key_down = pygame.key.get_pressed()

    if key_down[pygame.K_LEFT]:
        print("←←←←←←←←←左")
        hero.rect.x -= 10
    elif key_down[pygame.K_RIGHT]:
        print("右→→→→→→→→")
        hero.rect.x += 10
    elif key_down[pygame.K_DOWN]:
        print("下↓↓↓↓↓↓↓↓↓↓↓")
        hero.rect.y += 10
    elif key_down[pygame.K_UP]:
        print("上↑↑↑↑↑↑↑↑↑↑")
        hero.rect.y -= 10
    elif key_down[pygame.K_SPACE]:
        hero.fire()
        sound1.play()
        print("开火!!!!!!!!!!!!")

    # 碰撞检测
    if pygame.sprite.groupcollide(hero.bullets, enemys, True, True):
        sound2.play()
        score += 100
    #敌方子弹与我方英雄
    pygame.sprite.groupcollide(hero.bullets, enemy2.bullets1, True, True)
    pygame.sprite.groupcollide(hero.bullets, enemy3.bullets1, True, True)

    c = pygame.sprite.spritecollide(hero, enemy2.bullets1, True)
    if len(c) > 0:
        HP -= 1
        if HP < 0:
            hero.kill()
            pygame.quit()
            exit()
    d = pygame.sprite.spritecollide(hero, enemy3.bullets1, True)
    if len(d) > 0:
        HP -= 1
        if HP < 0:
            hero.kill()
            pygame.quit()
            exit()
    # 碰撞检测，飞机和飞机
    e = pygame.sprite.spritecollide(hero, enemys, True)
    if len(e) > 0:
        HP -= 1
        if HP < 0:
            hero.kill()
            pygame.quit()
            exit()
    # 精灵组渲染
    resources1.update()
    resources1.draw(screen)

    # 子弹精灵组渲染
    hero.bullets.update()
    hero.bullets.draw(screen)

    #渲染字体
    HP_text = game_font.render("HP:%s" % HP, True, [0, 255, 255])
    screen.blit(HP_text, (420, 5))
    score_text = game_font.render("SCORE:%s" % score, True, [255, 255, 255])
    screen.blit(score_text, (10, 5))

    enemy.bullets1.update()
    enemy.bullets1.draw(screen)
    enemy1.bullets1.update()
    enemy1.bullets1.draw(screen)
    enemy2.bullets1.update()
    enemy2.bullets1.draw(screen)
    enemy3.bullets1.update()
    enemy3.bullets1.draw(screen)

    # 渲染敌机精灵组中的所有飞机
    enemys.update()
    enemys.draw(screen)

    # 窗口渲染展示
    pygame.display.update()




