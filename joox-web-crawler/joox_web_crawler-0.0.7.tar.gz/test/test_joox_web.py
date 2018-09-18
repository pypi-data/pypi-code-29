import os
import sys
import io
import json
import argparse
from pprint import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir + '/../lib/')
#from JooxWeb import JooxWeb
from joox_web_crawler import JooxWeb

def loadArgumentParseModule(params = []):
    parser = argparse.ArgumentParser()
    if params:
        for item in params:
            if 'name' in item and 'default' in item and 'help' in item and 'required' in item:
                if 'choices' in item:
                    parser.add_argument('--' + item['name'] , default=item['default'], help=item['help'], required=item['required'], choices=item['choices'])
                else:
                    parser.add_argument('--' + item['name'] , default=item['default'], help=item['help'], required=item['required'])
            else:
                return False
    args = parser.parse_args()
    return args

args = loadArgumentParseModule([
{'name':'action', 'default':'get_song_info', 'help':'action to be tested', 'required':False, 'choices':['get_song_info', 'get_song_list', 'get_artists_page', 'get_artist_list']},
{'name':'param', 'default':False, 'help':'additional parameter', 'required':True},
])

#create JooxWeb Object
joox_web_object = JooxWeb()

if args.action == 'get_song_info':
    print('testing get_song_info')
    song_id = args.param
    print(song_id)
    song_info = joox_web_object.get_song_info_by_id(song_id)
    if not song_info:
        print('song id:[{0}] is not valid'.format(song_id))
        exit()
    pprint(song_info)
    song_list = joox_web_object.get_song_list_by_name(song_info['song_name'], song_info['singer_name'])
    if not song_list:
        print('song id:[{0}],[{1}] is not valid'.format(song_info['song_name'], song_info['singer_name']))
        exit()
    pprint(song_list)
    singer_type = joox_web_object.get_singer_type_by_songs(song_list)
    print('singer_type:{0}'.format(str(singer_type)))
    sys.stdout.flush()
    min_year = joox_web_object.get_song_age_by_songs(song_list, song_info['song_name'], 2)
    print('min_year:{0}'.format(min_year))
    song_age = JooxWeb.map_year_to_age(min_year)
    print('song_age:{0}'.format(song_age))

elif args.action == 'get_song_list':
    print('testing get_song_list')
    song_name = args.param
    song_list = joox_web_object.get_song_list_by_name(song_name, '')
elif args.action == 'get_artists_page':
    print('testing get_artists_page')
    path = args.param
    page_num = joox_web_object.get_artists_page_num(path)
    print(page_num)
    pass
elif args.action == 'get_artist_list':
    path = args.param
    artist_list = joox_web_object.get_artists(path, 1)
    pprint(artist_list)
    artist_list = joox_web_object.get_artists(path, 2)
    pprint(artist_list)
else:
    pass


