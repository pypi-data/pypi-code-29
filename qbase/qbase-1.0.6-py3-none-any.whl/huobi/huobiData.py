#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-8-6 15:40:03
# @Author  : datachain

from io import StringIO
import websocket
import gzip
import json
import datetime
import time
import logging
from qbase.common import until
from qbase.common import mmaper
from qbase.common import configer as cf


conf = cf.configer()

ACCESS_KEY = conf.getValueByKey('huobi', 'access_key')
SECRET_KEY = conf.getValueByKey('huobi', 'secret_key')
ACCOUNT_ID = conf.getValueByKey('huobi', 'account_id')

klinFormat = {'id': 1234567890, 'open': 9999999999.9999999999, 'close': 9999999999.9999999999, 'low': 9999999999.9999999999, 'high': 9999999999.9999999999, 'amount': 9999999999.9999999999, 'vol': 9999999999.9999999999, 'count': 999999999999}

def klinDataCopy(res, des):
    des[u'id'] = res[u'id']
    des[u'open'] = res[u'open']
    des[u'close'] = res[u'close']
    des[u'low'] = res[u'low']
    des[u'high'] = res[u'high']
    des[u'amount'] = res[u'amount']
    des[u'vol'] = res[u'vol']
    des[u'count'] = res[u'count']

"""
获取火币交易
参数说明：
    symbol：交易对 如eosusdt
    interval:kLin间隔时间 如：2(两小时KLin)
    DataNUm：存储数据量   如：20 存储20个周期数据
"""
def getKLineDataFrommarket(symbol, interval, DataNum):
    #定义日志
    log = logging.getLogger()

    # init a mmap with write mode
    mmapSize = klinFormat.__sizeof__() * (DataNum + 1)
    mpW = mmaper.Mmaper('mmapData/' + symbol + '.dat', mmapSize, 'W')
    ws = ''
    nextWholeTime = 0 #下一个整点时间
    connectFlag = False   #False-not connected True-connected

    tmpResultData = {'id': 0, 'open': 0, 'close': 0, 'low': 0, 'high': 0, 'amount': 0, 'vol': 0, 'count': 0}        #推送数据临时缓存区
    lastMinResultData = {'id': 0, 'open': 0, 'close': 0, 'low': 0, 'high': 0, 'amount': 0, 'vol': 0, 'count': 0}    #1分钟KLin数据
    lastResultData = {'id': 0, 'open': 0, 'close': 0, 'low': 0, 'high': 0, 'amount': 0, 'vol': 0, 'count': 0}       #最后一个周期的临时数据
    resultData = []                                                                                                 #所有数据的列表

    while (1):
        #连接火币API
        if connectFlag == False:
            while (1):
                try:
                    ws = websocket.create_connection("wss://api.huobi.br.com/ws")
                    tradeStr='{"sub": "market.' + symbol + '.kline.1min","id": "id10"}'
                    log.info("connection time is " + str(datetime.datetime.now()))
                    ws.send(tradeStr)
                    break
                except Exception as e:
                    log.error('ws connect Exception is: %s' %e)
                    time.sleep(5)
            connectFlag = True
        try:
            compressData = ws.recv()
        except Exception as e:
            log.error("ws recv Exception is: %s" %e)
            logging.info("disconnection time is " + str(datetime.datetime.now()))
            connectFlag = False
            continue
        try:
            result = gzip.decompress(compressData).decode('utf-8')
        except TypeError:
            continue
        #处理数据代码
        if result[:7] == '{"ping"':
            try:
                ts = result[8:21]
                pong = '{"pong":' + ts + '}'
                ws.send(pong)
            except Exception as e:
                log.error("ws send pong Exception is: %s" % e)
                connectFlag = False
            continue
        else:
            try:
                #处理最新推送的数据
                result_json =json.loads(result)
                #判断推送的消息中tick是否存在
                if u'tick' in result_json:
                    #初始化缓存变量
                    if lastResultData[u'id'] == 0:
                        klinDataCopy(result_json[u'tick'], lastResultData)
                    if lastMinResultData[u'id'] == 0:
                        klinDataCopy(result_json[u'tick'], lastMinResultData)
                    if tmpResultData[u'id'] == 0:
                        klinDataCopy(result_json[u'tick'], tmpResultData)
                    # 首次将取下一个整点时间
                    if nextWholeTime == 0:
                        nextWholeTime = until.getWholeTime(result_json[u'tick'][u'id'], interval)
                    #判断数据重复推送，如果重复推送不处理
                    if tmpResultData != result_json[u'tick']:
                        #将推送数据缓存到临时缓存区
                        tmpResultData = result_json[u'tick']
                        # 如果没到整点处理上一个周期数据
                        if tmpResultData[u'id'] < nextWholeTime:
                            #判断是否是同一分钟的推送
                            if lastMinResultData[u'id'] == tmpResultData[u'id']:
                                #如果是一分钟，更新一分钟数据
                                lastMinResultData[u'close'] = tmpResultData[u'close']
                                lastMinResultData[u'low'] = min(lastMinResultData[u'low'], tmpResultData[u'low'])
                                lastMinResultData[u'high'] = max(lastMinResultData[u'high'], tmpResultData[u'high'])
                                lastMinResultData[u'amount'] = tmpResultData[u'amount']
                                lastMinResultData[u'vol'] = tmpResultData[u'vol']
                                lastMinResultData[u'count'] = tmpResultData[u'count']
                                #更新最后动态数据lastResultData
                                lastResultData[u'close'] = lastMinResultData[u'close']
                                lastResultData[u'low'] = min(lastResultData[u'low'], lastMinResultData[u'low'])
                                lastResultData[u'high'] = max(lastResultData[u'high'], lastMinResultData[u'high'])
                            else:
                                #更新最后动态数据lastResultData
                                #lastResultData[u'id'] = lastMinResultData[u'id']
                                lastResultData[u'amount'] += lastMinResultData[u'amount']
                                lastResultData[u'vol'] += lastMinResultData[u'vol']
                                lastResultData[u'count'] += lastMinResultData[u'count']
                                # 新的一分钟，全量刷新一分钟数据
                                lastMinResultData[u'id'] = tmpResultData[u'id']
                                lastMinResultData[u'open'] = tmpResultData[u'open']
                                lastMinResultData[u'close'] = tmpResultData[u'close']
                                lastMinResultData[u'low'] = tmpResultData[u'low']
                                lastMinResultData[u'high'] = tmpResultData[u'high']
                                lastMinResultData[u'amount'] = tmpResultData[u'amount']
                                lastMinResultData[u'vol'] = tmpResultData[u'vol']
                                lastMinResultData[u'count'] = tmpResultData[u'count']
                        #超过下一个整点，固定上一个周期KLin值，重新开始下一个周期
                        else:
                            log.info(lastResultData)
                            if len(resultData) < DataNum:
                                resultData.append(json.loads(json.dumps(lastResultData)))
                            else:
                                del resultData[0]
                                resultData.append(json.loads(json.dumps(lastResultData)))
                            #将本次的Klin数据放到到下一个周期
                            klinDataCopy(result_json[u'tick'], lastResultData)
                            klinDataCopy(result_json[u'tick'], lastMinResultData)
                            klinDataCopy(result_json[u'tick'], tmpResultData)
                            nextWholeTime = until.getWholeTime(lastResultData[u'id'], interval)
                        #刷新周后一个周期
                        if len(resultData) == 0:
                            resultData.append(json.loads(json.dumps(lastResultData)))
                        else:
                            resultData[len(resultData) - 1] = json.loads(json.dumps(lastResultData))
                        mpW.writeDataToMmap(json.dumps(resultData).ljust(mmapSize, '\x00').encode())
            except Exception as e:
                log.error("Data process Exception is: %s" % e)
                continue
    # close the map
    mpW.closeMmap()


def gzip_uncompress(c_data):
   buf = StringIO(c_data)
   f = gzip.GzipFile(mode = 'rb', fileobj = buf)
   try:
      r_data = f.read()
   finally:
      f.close()
   return r_data


