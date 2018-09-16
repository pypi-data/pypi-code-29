import json
import requests
import os

data_path = os.path.abspath(__file__)
data_path = os.path.split(data_path)[0]+'/data/'

def brands():
    '''返回所有汽车品牌'''

    f = open(data_path + "carbrands.json", encoding='utf-8')
    fileJson = json.load(f)
    return fileJson




def main():
    print(brands())

if __name__ == '__main__':
    main()
