#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/27 下午4:26
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

huobiResultInsert = " create_time,position_id,account_id,amount,canceled_at,created_at ,field_amount ,field_cash_amount ,field_fees,finished_at,id ,price,source ,state,symbol,type "
conf = cf.configer()

def insertHuobiResult(positionId ,okexResultJson):
    sql = "insert into huobi_result ("
    sql += huobiResultInsert
    sql += ") VALUES ('"+str(getTimeStamp())+"', "
    sql += "'"+str(positionId) + "' , "
    sql += "'"+str(okexResultJson[u'account-id']) + "' , "
    sql += "'" + str(okexResultJson[u'amount']) + "' , "
    sql += "'" + str(okexResultJson[u'canceled-at']) + "' , "
    sql += "'" + str(okexResultJson[u'created-at']) + "' , "
    sql += "'" + str(okexResultJson[u'field-amount']) + "' , "
    sql += "'" + str(okexResultJson[u'field-cash-amount']) + "' , "
    sql += "'" + str(okexResultJson[u'field-fees']) + "' , "
    sql += "'" + str(okexResultJson[u'finished-at']) + "' , "
    sql += "'" + str(okexResultJson[u'id']) + "' , "
    sql += "'" + str(okexResultJson[u'price']) + "' , "
    sql += "'" + str(okexResultJson[u'source']) + "' , "
    sql += "'" + str(okexResultJson[u'state']) + "' , "
    sql += "'" + str(okexResultJson[u'symbol']) + "' , "
    sql += "'" + str(okexResultJson[u'type']) + "' )"
    # 链接数据库
    db = mySql.Mysql(conf.getValueByKey("db", "ip"), int(conf.getValueByKey("db", "port")),
                     conf.getValueByKey("db", "userName"), conf.getValueByKey("db", "passwd"),
                     conf.getValueByKey("db", "dnName"))
    result = db.modifyDb(sql)
    db.closeDb()
    return result

