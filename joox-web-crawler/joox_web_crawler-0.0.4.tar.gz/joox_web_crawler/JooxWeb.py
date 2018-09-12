import json
import time
import sys
import urllib.parse
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from .CurlLib import CurlLib

class JooxWeb(object):

    home_url = ''
    api_url = ''

    def __init__(self, home_url='http://www.joox.com/hk/zh_hk/', api_url='http://api-jooxtt.sanook.com/web-fcgi-bin/web_search?', conn_timeout=60, timeout=60, logger=None):
        self.home_url = home_url
        self.api_url = api_url
        self.curl_object = CurlLib(conn_timeout, timeout, logger)

    def set_home_url(self, home_url):
        self.home_url = home_url

    def set_api_url(self, api_url):
        self.api_url = api_url

    def get_artists_page_num(self, path):
        max_num = 1
        url = self.home_url + 'artists/' + path
        html_doc = self.curl_object.get(url)
        #parse data by bs4 
        soup = BeautifulSoup(html_doc, 'html.parser')
        items = soup.find(attrs={'class':'pagination'}).find_all('li')
        if not items:
            return 0
        for li in items:
            num = li.get_text()
            if num:
                try:
                    num = int(num)
                except:
                    num = 0
            else:
                num = 0
            max_num = max(num, max_num)
        return max_num

    def get_artists(self, path, page_num):
        artist_list = []
        if page_num == 0:
            return []
        url = self.home_url + 'artists/' + path
        if page_num and page_num > 1:
            url = url + '?page=' + str(page_num)
        print(url)
        html_doc = self.curl_object.get(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        items = soup.find_all(itemprop='name')
        if not items:
            return artist_list
        for item in items:
            #filter out something
            if '歌手' in item.get_text() or '樂隊組合' in item.get_text():
                pass
            else:
                artist_id = ''
                artist_name = item.get_text()
                href = item.find_parent('a', href=True).attrs['href']
                if href:
                    artist_id = href.split('/')[-1]
                if artist_id:
                    artist_list.append({'artist_name':artist_name,'artist_id':artist_id})
        return artist_list

    @staticmethod
    def map_year_to_age(year):
        year = int(year)
        if year >= 2010:
            return "10s"
        elif year >= 2000:
            return "00s"
        elif year >= 1990:
            return "90s"
        elif year >= 1980:
            return "80s"
        elif year >= 1970:
            return "70s"
        elif year >= 1960:
            return "60s"
        else:
            return "50s"

    def get_singer_type_by_songs(self, song_list):
        if not song_list:
            return False
        singer_type_list = []
        for song in song_list:
            singer_type_list.append(song['singer_type'])
        return max(singer_type_list,key=singer_type_list.count)

    def get_song_age_by_songs(self, song_list, orig_song_name, sleep_time=0, min_year=2018): 
        if not song_list:
            return False
        for song in song_list:
            song_info_hash = self.get_song_info_by_id(song['song_id'])
            if song_info_hash and 'release_date' in song_info_hash and 'year' in song_info_hash['release_date']:
                song_name = song_info_hash['song_name']
                #print('song_name:{0}, orig_song_name:{1}, similarity:{2}'.format(song_name, orig_song_name, str(SequenceMatcher(None, song_name, orig_song_name).ratio())))
                if song_name in orig_song_name or orig_song_name in song_name or SequenceMatcher(None, song_name, orig_song_name).ratio() > 0.7:
                    year = int(song_info_hash['release_date']['year'])
                    #print('min_year:{0}, year:{1}, song_name:{2}, singer_name:{3}'.format(min_year, year, song_info_hash['song_name'], song_info_hash['singer_name']))
                    sys.stdout.flush()
                    min_year = min(min_year, year)
                else:
                    pass
                    #print('song name did not match: {0}, {1}'.format(song_name, orig_song_name))
            time.sleep(sleep_time)
        return min_year

    def get_song_list_by_name(self, song_name, singer_name):
        song_list = []
        url = self.api_url + 'country=hk&lang=zh_TW&search_input=' + urllib.parse.quote_plus(song_name.encode('utf8')) + '%20' + urllib.parse.quote_plus(singer_name.encode('utf8')) + '&sin=0&ein=30'
        json_result = self.curl_object.get(url)
        result_hash = json.loads(json_result)
        if 'itemlist' not in result_hash:
            return False
        for item in result_hash['itemlist']:
            singer_type = item['singertype']
            song_id = item['songid']
            singer_id = item['singerid']
            song_list.append({'song_id':song_id, 'singer_type':singer_type, 'singer_id':singer_id})
        return song_list

    def get_song_info_by_id(self, song_id):
        song_info_hash = {}
        if not song_id:
            return False
        
        url = self.home_url + 'single/' + song_id
        html_doc = self.curl_object.get(url)
        #parse data by bs4 
        soup = BeautifulSoup(html_doc, 'html.parser') 
        #get song and album name
        span_map = []
        span_map.append('song_name')
        span_map.append('album_name')
        span_list = soup.find_all(itemprop='name')
        if span_list:
            for index, value in enumerate(span_list):
                print("{0}, {1}".format(index, value.decode_contents()))
                song_info_hash[span_map[index]] = value.decode_contents()
        else:
            return False

        #get singer name
        singer_name = soup.find(itemprop='byArtist').contents[0].decode_contents()
        song_info_hash['singer_name'] = singer_name
        
        #get release date
        release_date = soup.find(itemprop='albumRelease').decode_contents()
        release_date_list = list(reversed(release_date.split('-')))
        song_info_hash['release_date'] = {}
        song_info_hash['release_date']['year'] = release_date_list[0]
        song_info_hash['release_date']['month'] = release_date_list[1]
        song_info_hash['release_date']['day'] = release_date_list[2]
        return song_info_hash

