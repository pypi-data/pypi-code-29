#!/usr/bin/python
#-*- coding:utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import os
import sys
import imageio
import datetime
class gif2txt():

    def __init__(self,file,save="",temp="",duration=0.1,clear=True,ascii_char=list("MNHQ$OC67+>!:-. "),debug=False):
        try:
            self.current_path = os.getcwd()
            self.file=file
            self.current_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            self.file_name=os.path.basename(self.file)
            self.save_path=save or self.current_path
            self.temp=str(temp or self.current_path)+'/temp/'+self.current_time
            self.duration=duration
            self.clear=clear
            self.ascii_char=ascii_char
            self.ascii_char_len=len(self.ascii_char)
            self.debug=debug
            if not os.path.exists(file):
                raise IOError
        except IOError:
            return sys.exit(-1)
        if self.debug:
            print(self.__dict__)

    def _pixel2char(self,r,g,b,alpha = 256):
        """
        通过像素信息返回特定的字符
        :param r: 像素的红色信息
        :param g: 像素的绿色信息
        :param b: 像素的蓝色信息
        :param alpha: 像素的透明杜信息
        :return: char or
        """
        if alpha==0:
            return
        gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit=(256.0+1)/self.ascii_char_len
        return self.ascii_char[int(gray/unit)]

    def _txt2png(self,file_name):
        """
        把图片转成字符串和颜色信息然后再转成图片（png）
        :param file_name:
        :return:
        """
        os.chdir(self.temp)
        img=Image.open(file_name).convert('RGB')
        raw_width=img.width
        raw_height=img.height
        width=int(raw_width/6)
        height=int(raw_height/15)
        img = img.resize((width, height), Image.NEAREST)#获取一个图片的调整大小之后的副本
        txt=''
        colors=[]
        for i in range(height):
            for j in range(width):
                pixel = img.getpixel((j, i)) #获取像素信息
                colors.append((pixel[0], pixel[1], pixel[2]))
                if (len(pixel) == 4):
                    txt += self._pixel2char(pixel[0], pixel[1], pixel[2], pixel[3])
                else:
                    txt += self._pixel2char(pixel[0], pixel[1], pixel[2])
            txt += '\n'
            colors.append((255, 255, 255))

        img_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255)) #创建一个图片
        dr = ImageDraw.Draw(img_txt)
        font = ImageFont.load_default().font
        x = y = 0
        font_w, font_h = font.getsize(txt[1])  # 获取字体的宽高
        font_h *= 1.37  # 调整后更佳
        for i in range(len(txt)):
            if (txt[i] == '\n'):
                x += font_h
                y = -font_w
            dr.text([y, x], txt[i], colors[i])
            y += font_w
        name = file_name.split('.')[0] + '-txt' + '.png'
        if self.debug:
            print(os.getcwd()+'/'+name)
        img_txt.save(name)

    def _gif2png(self):
        """
        gif 图片分割成png 图片
        :return:
        """
        img = Image.open(self.file)
        if not os.path.exists(self.temp):
            os.makedirs(self.temp)
        os.chdir(self.temp)
        try:
            while True:
                current = img.tell()
                name = self.file_name.split('.')[0] + '-' + str(current) + '.png'
                img.save(name)  # gif分割后保存的是索引颜色
                if self.debug:
                    print(os.getcwd()+'/'+name)
                self._txt2png(name)
                img.seek(current + 1)
        except:
            os.chdir(os.getcwd())

    def _png2gif(self):
        """
        png 图片转成GIF图片
        :return:
        """
        os.chdir(self.temp)
        dirs = os.listdir()
        images = []
        num = 0

        for d in dirs:
            if d.split('-')[-1] == 'txt.png':
                images.append(imageio.imread(d))
                num += 1

        os.chdir(self.save_path)
        imageio.mimsave(d.split('-')[0] +'_txt_'+ self.current_time+'.gif', images, duration=self.duration)

    def make(self):
        """
        执行入口
        :return:
        """
        self._gif2png()
        self._png2gif()








