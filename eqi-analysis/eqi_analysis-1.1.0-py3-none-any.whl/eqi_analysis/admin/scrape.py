import ast
import base64
import json
import locale
import re
import time
import urllib
from datetime import datetime
from eqi_utils.data import view
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

from eqi_analysis.core.extension import EQIDF

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

TR_BASE_URL = r'https://www.reuters.wallst.com/reuters/enhancements/US/interactiveChart/chart.asp?symbol='
TR_HISTORY_PRX_URL = r'https://www.reuters.wallst.com/reuters/enhancements/US/interactiveChart/api.asp'
TR_TEMPLATE = r'{{"events":[{{"type":"events","name":"news","color":"e52600","symbol":"{symbol}","symbolType":"WSODIssue"}}],"WSODIssue":"{symbol}","RIC":"{ric}","company":{wsod},"duration":"{dur}","frequency":"{freq}","dMax":{dmax},"dMin":{dmin},"display":"mountain","scaling":"linear","reskin":true}}'


def fetch_price_ric(ric, freq='1month', dmin='undefined', dmax='undefined',
                    duration=7300):
    response = requests.get(TR_BASE_URL + ric)
    meta_soup = BeautifulSoup(response.text, features="lxml")
    raw_issue = meta_soup.find('script')
    if raw_issue is None:
        return None
    company_meta = ast.literal_eval(
        raw_issue.contents[0].replace("var issue = ", '').replace("null",
                                                                  "None")[:-1])
    input_params = TR_TEMPLATE.format(
        symbol=company_meta['WSODIssue']['Ticker'],
        wsod=company_meta['WSODCompany'],
        ric=company_meta['RIC']['Ticker'],
        freq=freq,
        dmin=dmin,
        dmax=dmax,
        dur=duration)
    payload = {
        "inputs": 'B64ENC' + base64.b64encode(str.encode(input_params)).decode(
            'utf-8')}
    history_price = requests.post(
        TR_HISTORY_PRX_URL,
        data=payload)
    price_soup = BeautifulSoup(history_price.text, features="lxml")
    price_json = json.loads(json.loads(
        price_soup.find('p').contents[0][:-2].replace('undefined',
                                                      '\"undefined\"'))[
                                'hoverData'])
    return to_ric_price(pd.DataFrame.from_dict(price_json))


def remove_cur(v):
    return re.match(r'\D+(\d+(.\d*)*)', v).group(1)


def to_decimal(v):
    return float(locale.atof(v))


def to_decimal_wo_cur(v):
    return float(locale.atof(remove_cur(v)))


def to_ric_price(price_df):
    price_df = price_df.copy()
    price_df['date'] = pd.to_datetime(price_df['date'])
    price_df['close'] = price_df['close'].apply(to_decimal_wo_cur)
    price_df['high'] = price_df['high'].apply(to_decimal_wo_cur)
    price_df['low'] = price_df['low'].apply(to_decimal_wo_cur)
    price_df['open'] = price_df['open'].apply(to_decimal_wo_cur)
    price_df['volume'] = price_df['volume'].apply(to_decimal)
    return price_df


BB_BASE_URL = 'https://www.bloomberg.com/markets2/api/history/{}/PX_LAST?timeframe=5_YEAR&period=monthly&volumePeriod=monthly'
headers = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
cookie: agent_id=9b2a7bcd-3379-46ac-ac13-0613f47226cd; session_id=ba00fe9c-c464-43df-8200-e216bcc7b90e; session_key=29ab7c34843099141344176725cce2ff6c1d14a6; bdfpc=004.0553189278.1530027441332; _ga=GA1.2.1005165036.1530027441; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=a7d1b61d-1ad1-47a1-971b-3d7ba2c49a4b2525; __uzmbj2=1530027441; __tbc=%7Bjzx%7Dt_3qvTkEkvt3AGEeiiNNgLOglopwhXSvmMxEJ7gRVMZJ4bWB-Yo5mjYmrCKwGfpooLeSuQfQLDDMWpWlCF6oPEeO3ZWGt3eC6h5-Aw6-SNS_3iCjA2VH-XWCN6u3F9_7jylU0Z664w9lha1BgkmqDg; __gads=ID=dde07271827c2570:T=1530027443:S=ALNI_Ma703_Uq77_k_-vty7kRPRzg-gEAg; __uzma=5d0351fb-fee8-ddc3-a799-e738703b4706; __uzmb=1530025439; __uzmc=993051380696; __uzmd=1530025440; __pat=-14400000; _user-status=anonymous; _user-ip=85.0.20.236; _user_newsletters=[]; _gid=GA1.2.1824033969.1535453057; pxvid=4f9602b0-aaaf-11e8-aee9-cd7bf8a53a26; _pxvid=4f9602b0-aaaf-11e8-aee9-cd7bf8a53a26; notice_behavior=none; bbAbVisits=; bb_geo_info={"country":"CH","region":"Europe"}|1536057859679; trc_cookie_storage=taboola%2520global%253Auser-id%3D8539050a-f7e4-4167-8675-c2bf522e65d1-tuct2231b86; __ncuid=316fee7e-128b-467a-8386-5967d14365ef; __uzmcj2=421141621023; __uzmdj2=1535454958; _parsely_visitor={%22id%22:%227c13c25c-43a9-4951-b735-b534658ea8a5%22%2C%22session_count%22:3%2C%22last_session_ts%22:1535455732972}; _litra_id.2a03=a-015y--e4e65fa4-d275-4164-871f-9f375993dded.1535453058.3.1535458920.1535455738.7d83fd5b-ae18-482f-8650-c1492eeb764a; SRV=JPX05; __pvi=%7B%22id%22%3A%22v-2018-08-28-14-49-47-869-BDM3oyhzECza5AYl-b8ac3b18566f24f4fd61c0b8e15d0ed9%22%2C%22domain%22%3A%22.bloomberg.com%22%2C%22time%22%3A1535460587870%7D; xbc=%7Bjzx%7DmC1EG7Vp2x-b744jJOaYuRHzyB_GTTJcJH0kGnaWtNfvZkwf82EME4MgRSNIqO5dRBg0YMNTMQKQvsktSlkbpATZ7QcvBXtBFih6rNVR7kDkSD9iIhvd3LA0JZAo_vglDhVd8jUYlHlDpKiRAZeiiL66u9MM0_eoZUra55QoO2NNjlV4eKTxqCL5HfZmZA8PxRTCAg1t-7Cjssgrjw9S2LBgJGHHS5T4Qa4aj1Xex4mYtvw1_EFt9-Z_AT2Xb710KS7OWpQy3xbDjsiAiOrQmQn8sM4Vl_BhkDRpFU-HZhOE1O06FB39GXem6FjDj6X9ELMvSinWjaZrJbrFZc3j4YnfvJossr1reGPEVCJQBGRQgm2gOYRKUtR-rwjMFKolJ1Xkkitj1Pav2374iIStZg; _px2=eyJ1IjoiZjQzNTdkYzAtYWFiYy0xMWU4LTkzMDEtM2IyOGM3YWU2N2EwIiwidiI6IjRmOTYwMmIwLWFhYWYtMTFlOC1hZWU5LWNkN2JmOGE1M2EyNiIsInQiOjE1MzU0NjExNDU1MjUsImgiOiI5YjlmMTk4NGZlMjljYmZkODc4NzFlZjA1MTkzN2RkYTg2NTI4ZDFlNzkyYTI3MGY0MWM3NTYxMjNjMjEzYjUyIn0=; _px3=788f2108be4e99042c2ff6cf6c11e72abaca2fa75f53c8c13b472691ece4b193:hVlHvxdb5jLy+QltsN8nQc7ry1V3zzchpyLBnlHF5sL9DwN8NNSYnTYYI9bKuqLUQvUK1I6AL+F0WtWGAYJubQ==:1000:OoLLYGkTxeh4IHAj0cgYEkzHHOw4jeQh9KcoGoDlPFAGY7ePrFzbCbx6rfHk/LVvh725ZQwQ34dsbzcm+370obUKQha/TieWl0gYURx9rKDl0pzB1qMtTuT6nYlGSeh90NupQxdPIBgMm3IMTv9vDCaewcuj2hEXb2Ya4eyS94E=; _pxde=7ce5be70c90a6425b8875189965eab18f548847e6606eb347e6954a24fd12b40:eyJ0aW1lc3RhbXAiOjE1MzU0NjA4NDU1MjgsImlwY19pZCI6W119
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
"""
header_full = {line[:line.find(': ')]: line[line.find(': ') + 2:] for line in
               headers.split('\n') if line}
header = {line[:line.find(': ')]: line[line.find(': ') + 2:] for line in
          headers.split('\n') if line and not line.startswith('cookie')}
cookie = {kv[:kv.find('=')]: kv[kv.find('=') + 1:] for kv in
          header_full['cookie'].split('; ')}


def fetch_price_bb(bbid, debug=False):
    bb_url_hot = BB_BASE_URL.format(urllib.parse.quote_plus(bbid))
    response = requests.get(bb_url_hot, headers=header, cookies=cookie)
    if debug:
        print(response.text)
    return pd.DataFrame.from_dict(json.loads(response.text)[0]['price'])


def fetch_price_bulk(tickers, fetch_func, save_as_one=True, prefix=''):
    if not save_as_one and not prefix:
        raise ValueError('prefix must be set if not in save_as_one mode')
    total_fetched = 0
    total_to_fetch = len(tickers)
    unfetched = []
    fetched_dfs = []
    start_time = time.time()
    for ticker in tickers:
        total_fetched += 1
        try:
            price_df = fetch_func(ticker)
        except Exception as e:
            print(e)
            price_df = None
        if price_df is None or len(price_df) == 0:
            print("Price data for {} is not found".format(ticker))
            unfetched.append(ticker)
            continue
        price_df['asset'] = ticker
        if save_as_one:
            fetched_dfs.append(price_df)
        else:
            view.save_view(price_df, 'price_{}_{}'.format(prefix, ticker))
        time.sleep(2)
        if total_fetched % 100 == 0:
            speed = total_fetched / (time.time() - start_time)
            to_fetch = total_to_fetch - total_fetched
            eta = to_fetch / speed
            print("total fetched {}, at speed {}/s, finishing in {}s".format(
                to_fetch, speed, eta))
    if unfetched:
        print("Unfetched tickers: {}".format(unfetched))
    if save_as_one:
        return pd.concat(fetched_dfs)
    else:
        return None


LIBOR_URL = r'http://www.fedprimerate.com/libor/libor_rates_history.htm'


def fetch_libor():
    libor_response = requests.get(LIBOR_URL)
    libor_soup = BeautifulSoup(libor_response.text, 'html.parser')
    libor_map = {}
    for tr in libor_soup.findAll('tr'):
        children = tr.findChildren('td')
        content = children[0].contents[0]
        date_str = re.match(r'.*(\b\w+ of \d{4}).*', str(content), re.I)

        def get_rate(node):
            try:
                return float(node.contents[0])
            except:
                return float(node.findChild('p').contents[0])

        if date_str is not None:
            libor_rate = [get_rate(r) for r in children[1:5]]
            libor_date = datetime.strptime(date_str.group(1), '%B of %Y')
            libor_map[libor_date] = libor_rate

    return pd.DataFrame.from_dict(libor_map, orient='index',
                                  columns=['1M', '3M', '6M', '12M']) / 100


def to_datetime(s):
    if s is None:
        return np.nan
    try:
        return datetime.strptime(str(s), "%Y-%m-%d %H:%M:%S").date()
    except ValueError:
        return np.nan


def fetch_msci(msci_idx_path):
    msci_df = pd.read_excel(msci_idx_path)
    return (msci_df.to_eqi()
            .e_rename({'Unnamed: 0': 'date', 'Unnamed: 1': 'price'})
            .e_set('date', 'date', to_datetime)
            .dropna()
            .e_set_index('date')
            .sort_index()
            .e_astype({'price': float})
            .to_pandas())
