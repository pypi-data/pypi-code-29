#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/21 下午3:58
# @Author  : datachain

from qbase.common import mySql
from qbase.common import configer as cf
import time

def getTimeStamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

bitmexRow = " create_time,position_id,orderID,clOrdID,clOrdLinkID,account,symbol,side,simpleOrderQty,orderQty,price,displayQty,stopPx,pegOffsetValue,pegPriceType,currency,settlCurrency,ordType,timeInForce,execInst,contingencyType,exDestination,ordStatus,triggered,workingIndicator,ordRejReason,simpleLeavesQty,leavesQty,simpleCumQty,cumQty,avgPx,multiLegReportingType,text,transactTime,timestamp "
conf = cf.configer()

def insertBitmexResult(clOrdID, positionId, symbol, side ,orderQty):
    sql = "insert into bitmex_result (clOrdID, positionId, symbol, side ,orderQty) VALUES("
    sql += "'" + str(clOrdID) + "'"
    sql += "'" + str(positionId) + "'"
    sql += "'" + str(symbol) + "'"
    sql += "'" + str(side) + "'"
    sql += "'" + str(orderQty) + "'"
    sql += ")"

def updateBitmexResultByClOrderId(positionId ,bitmexResult):
    sql = "update bitmex_result set "
    sql += "create_time = '" + str(getTimeStamp())+"', "
    sql += "position_id = '" + str(positionId) + "' , "
    sql += "orderID = '" + str(bitmexResult[u'orderID']) + "', "
    sql += "clOrdLinkID = '" + str(bitmexResult[u'clOrdLinkID']) + "', "
    sql += "account = '" + str(bitmexResult[u'account']) + "', "
    sql += "symbol = '" + str(bitmexResult[u'symbol']) + "', "
    sql += "side = '" + str(bitmexResult[u'side']) + "', "
    sql += "simpleOrderQty = '" + str(bitmexResult[u'simpleOrderQty']) + "', "
    sql += "orderQty = '" + str(bitmexResult[u'orderQty']) + "', "
    sql += "price = '" + str(bitmexResult[u'price']) + "', "
    sql += "displayQty = '" + str(bitmexResult[u'displayQty']) + "', "
    sql += "stopPx = '" + str(bitmexResult[u'stopPx']) + "', "
    sql += "pegOffsetValue = '" + str(bitmexResult[u'pegOffsetValue']) + "', "
    sql += "pegPriceType = '" + str(bitmexResult[u'pegPriceType']) + "', "
    sql += "currency = '" + str(bitmexResult[u'currency']) + "', "
    sql += "settlCurrency = '" + str(bitmexResult[u'settlCurrency']) + "', "
    sql += "ordType = '" + str(bitmexResult[u'ordType']) + "', "
    sql += "timeInForce = '" + str(bitmexResult[u'timeInForce']) + "', "
    sql += "execInst = '" + str(bitmexResult[u'execInst']) + "', "
    sql += "contingencyType = '" + str(bitmexResult[u'contingencyType']) + "', "
    sql += "exDestination = '" + str(bitmexResult[u'exDestination']) + "', "
    sql += "ordStatus = '" + str(bitmexResult[u'ordStatus']) + "', "
    sql += "triggered = '" + str(bitmexResult[u'triggered']) + "', "
    sql += "workingIndicator = '" + str(bitmexResult[u'workingIndicator']) + "', "
    sql += "ordRejReason = '" + str(bitmexResult[u'ordRejReason']) + "', "
    sql += "simpleLeavesQty = '" + str(bitmexResult[u'simpleLeavesQty']) + "', "
    sql += "leavesQty = '" + str(bitmexResult[u'leavesQty']) + "', "
    sql += "simpleCumQty = '" + str(bitmexResult[u'simpleCumQty']) + "', "
    sql += "cumQty = '" + str(bitmexResult[u'cumQty']) + "', "
    sql += "avgPx = '" + str(bitmexResult[u'avgPx']) + "', "
    sql += "multiLegReportingType = '" + str(bitmexResult[u'multiLegReportingType']) + "', "
    sql += "text = '" + str(bitmexResult[u'text']) + "', "
    sql += "transactTime = '" + str(bitmexResult[u'transactTime']) + "', "
    sql += "timestamp = '" + str(bitmexResult[u'timestamp']) + "' "
    sql += "where clOrdID = '" + str(bitmexResult[u'clOrdID']) + "', "


    # 链接数据库
    db = mySql.Mysql(conf.getValueByKey("db", "ip"), int(conf.getValueByKey("db", "port")),
                     conf.getValueByKey("db", "userName"), conf.getValueByKey("db", "passwd"),
                     conf.getValueByKey("db", "dnName"))
    result = db.modifyDb(sql)
    db.closeDb()
    return result

