#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/21 下午2:21
# @Author  : datachain

import logging
import json
import math
import time
from qbase.enum import enum
from qbase.dao import okexResultMapper, positionMapper, huobiResultMapper ,bitmexResultMapper
from qbase.huobi import huobiService
from qbase.okex import okcoinFutureAPI


log = logging.getLogger()

class Transation:
    log = None
    okexUrl = 'www.okb.com'

    def __init__(self):
        self.log = logging.getLogger()

    def huobiErrorFrozen(self,position , tradeType ,num):
        if tradeType == 1:
            position.baseCoinFrozen += num
        elif tradeType == 3:
            position.tradeCoinFrozen += num
        positionMapper.setPositionFroze(position)

    def huobiSpotServer(self, account, position, num, tradeType):

        huobisvr = huobiService.HuobiService(account.accessKey,account.secretKey,position.account).getHuobiService()

        amountNum = 0  # 交易数量
        trade = ''
        if tradeType == 1:
            #开多
            trade = 'buy-market'
            amountNum = position.baseCoin - position.baseCoinFrozen
            self.log.info('买入 %s  数量 %s 交易类型 : 开多 ' % (position.symbol, amountNum))
        elif tradeType == 3:
            #平多
            trade = 'sell-market'
            amountNum = position.tradeCoin - position.tradeCoinFrozen
            self.log.info('卖出 %s  数量 %s 交易类型 : 开多 ' % (position.symbol, amountNum))

        if amountNum <= 0:
            # 异常交易
            self.log.error('交易币数量不足  %s  %s' % (position.symbol, amountNum))
            return enum.TransactionResult.CoinNumFail.value
        # 当前交易币小于 交易量 则交易所有交易币
        if num >= amountNum:
            num = amountNum
        num = math.floor(num * 10000 ) / 10000
        try:
            resultJson = huobisvr.send_order(num, '', position.symbol, trade, '')
        except Exception as e:
            #记录
            self.huobiErrorFrozen(position,tradeType ,num)
            self.log.error("！！！！！！！！！！！！huobi交易抛出异常！！！！！！！！！！！！")
            self.log.error(e)
            return enum.TransactionResult.Fail.value

        if resultJson is None or resultJson[u'status'] == 'error':
            self.log.error("********************huobi交易失败********************")
            self.log.error(resultJson)
            return enum.TransactionResult.Fail.value
        self.log.info("huobi 交易结果")
        self.log.info(resultJson)
        orderId = resultJson[u'data']
        orderResultJson = ''
        i = 0
        while i < 5:
            time.sleep(0.1 * i)
            i += 1
            try:
                self.log.info('查询Huobi交易结果 第 %s 次 | 订单ID %s ' % (i, orderId))
                orderResultJson = huobisvr.order_info(orderId)
            except Exception as e:
                self.log.error("！！！！！！！！！！！！huobi查询订单异常！！！！！！！！！！！！")
                self.log.error(e)
                continue
            state = orderResultJson[u'data'][u'state']
            if state == 'filled':
                break
        if orderResultJson == '' or orderResultJson is None or state != 'filled':
            self.huobiErrorFrozen(position, tradeType, num)
            self.log.error("********************huobi查询订单失败********************")
            self.log.error(e)
            return enum.TransactionResult.Fail.value

        self.log.info(orderResultJson)
        orderDict = orderResultJson[u'data']
        huobiResultMapper.insertHuobiResult(position.id, orderDict)

        type = orderDict[u'type']
        amount = orderDict[u'amount']
        fieldAmount = orderDict[u'field-amount']
        fieldFees = orderDict[u'field-fees']
        fieldCashAmount = orderDict[u'field-cash-amount']
        if type == 'buy-market':
            position.baseCoin -= float(amount)
            position.tradeCoin += float(fieldAmount) - float(fieldFees)
        elif type == 'sell-market':
            position.baseCoin += float(fieldCashAmount) - float(fieldFees)
            position.tradeCoin -= float(amount)
        position.baseCoin = math.floor(position.baseCoin * 10000 ) / 10000
        position.tradeCoin = math.floor(position.tradeCoin * 10000) / 10000

        positionMapper.setPosition(position)
        return enum.TransactionResult.OK.value

    def okexFuturesPriceAvg(self,account,symbol ,tradeType):
        result = {"buyPriceAvg":0,"sellPriceAvg":0}
        if tradeType != 3 and tradeType != 4:
            return enum.TransactionResult.OK.value

        okcoinFuture = okcoinFutureAPI.OKCoinFuture(self.okexUrl, account.accessKey, account.secretKey)
        try:
            positionResult = okcoinFuture.future_position(symbol, 'quarter')
            # 不是全仓账号
            if not json.loads(positionResult)[u'result']:
                if json.loads(positionResult)[u'error_code'] == 20022:
                    positionResult = okcoinFuture.future_position_4fix(symbol, 'quarter', 10)
            okexPosition = json.loads(positionResult)
            result[u"buyPriceAvg"] = okexPosition[u'holding'][0][u'buy_price_avg']
            result[u"sellPriceAvg"] = okexPosition[u'holding'][0][u'sell_price_avg']
            ok = enum.TransactionResult.OK.value
            ok[u'data'] = result
            return ok
        except Exception as e:
            #记录
            self.log.error("！！！！！！！！！！！！查询仓位平均价异常！！！！！！！！！！！！")
            self.log.error(e)
            return enum.TransactionResult.Fail.value

    def okexErrorFrozen(self,position , tradeType ,num):
        if tradeType == 1 or tradeType == 2:
            if position.symbol == 'eos_usd' or position.symbol == 'eth_usd':
                position.baseCoinFrozen += num * 10
            elif position.symbol == 'btc_usd':
                position.baseCoinFrozen += num * 100
        elif tradeType == 3:
            position.tradeCoinFrozen += num
        elif tradeType == 4:
            position.nullCoinFrozen += num

        positionMapper.setPositionFroze(position)

    def okexFuturesServer(self, account, position, num, tradeType):
        """
        OKEx 期货交易
        :param account:
        :param position:
        :param num:
        :param tradeType:
        :return:
        """
        #tradeType 交易类型 1 开多 2开空  3 平多 4平空
        amountNum = 0 #交易数量
        resultData = {"buyPriceAvg": 0, "sellPriceAvg": 0, "orderId": ""}
        contractName = position.openContract

        if tradeType == 1 or tradeType == 2:
            if tradeType == 1:
                position.tradeContract = contractName
                trade = '开多'
            else:
                position.nullContract = contractName
                trade = '开空'

            if position.symbol == 'eos_usd' or position.symbol == 'eth_usd':
                amountNum = math.floor((position.baseCoin - position.baseCoinFrozen) / 10)
            elif position.symbol == 'btc_usd':
                amountNum = math.floor((position.baseCoin - position.baseCoinFrozen) / 100)
            self.log.info('买入 %s  数量 %s 交易类型 : %s ' % (position.symbol, amountNum, trade))
        elif tradeType == 3 or tradeType == 4:
            if tradeType == 3:
                trade = '平多'
                contractName = position.tradeContract
                amountNum = position.tradeCoin - position.tradeCoinFrozen
            else:
                trade = '平空'
                contractName = position.nullContract
                amountNum = position.nullCoin - position.nullCoinFrozen
            self.log.info('卖出 %s  数量 %s 交易类型 : %s ' % (position.symbol, amountNum, trade))

        if amountNum < 1:
            #异常交易
            self.log.error('交易币数量不足  %s  %s' %(position.symbol , amountNum))
            return enum.TransactionResult.CoinNumFail.value
        #当前交易币小于 交易量 则交易所有交易币
        if num >= amountNum:
            num = amountNum

        okcoinFuture = okcoinFutureAPI.OKCoinFuture(self.okexUrl, account.accessKey,account.secretKey )

        if tradeType == 3 or tradeType == 4:
            okexPriceAvgResult = self.okexFuturesPriceAvg(account, position.symbol, tradeType)
            if okexPriceAvgResult[u'code'] != 1000:
                return okexPriceAvgResult
            resultData[u"buyPriceAvg"] = okexPriceAvgResult[u'data'][u'buyPriceAvg']
            resultData[u"sellPriceAvg"] = okexPriceAvgResult[u'data'][u'sellPriceAvg']

        try:
            resultJson = okcoinFuture.future_trade(position.symbol, contractType='quarter', price='', amount=num,
                                                   tradeType=tradeType, matchPrice='1', leverRate='10')
        except Exception as e:
            #记录
            self.okexErrorFrozen(position,tradeType ,num)
            self.log.error("！！！！！！！！！！！！okex交易抛出异常！！！！！！！！！！！！")
            self.log.error(e)
            return enum.TransactionResult.Fail.value

        if resultJson == '' or resultJson is None :
            self.log.error("！！！！！！！！！！！！okex交易返回异常 result为空！！！！！！！！！！！！")
            self.okexErrorFrozen(position, tradeType, num)
            return enum.TransactionResult.Fail.value
        if not json.loads(resultJson)[u'result']:
            self.log.error("********************okex交易失败********************")
            self.log.error(resultJson)
            return enum.TransactionResult.Fail.value
        else:
            if json.loads(resultJson)[u'order_id'] == '':
                #记录
                self.log.error("！！！！！！！！！！！！okex交易返回异常 result中orderId为空！！！！！！！！！！！！")
                self.okexErrorFrozen(position, tradeType, num)
                return enum.TransactionResult.ResultOrderIdFail.value
            else:
                self.log.info(resultJson)
                resultOrder = enum.TransactionResult.OK.value

                resultData[u"orderId"] = json.loads(resultJson)[u"order_id"]
                resultOrder[u'data'] = resultData
                return resultOrder

    def okexResult(self,account , position ,mapData ,tradeType, num):
        okcoinFuture = okcoinFutureAPI.OKCoinFuture(self.okexUrl, account.accessKey,
                                                    account.secretKey)
        self.log.info('查询OKEx交易结果 订单ID %s' %mapData[u"orderId"])
        i = 0
        state = -10
        #循环5次 如果没有成功就撤单   如果撤单失败记录异常冻结
        while i < 5:
            time.sleep(0.3 * i)
            i += 1
            self.log.info('查询OKEx交易结果 第 %s 次 | 订单ID %s ' % (i, mapData[u"orderId"]))
            try:
                orderResultJson = okcoinFuture.future_orderinfo(position.symbol, contractType='quarter',
                                                                orderId=mapData[u"orderId"],
                                                                status="2", currentPage="1", pageLength="50")
                state = json.loads(orderResultJson)[u'orders'][0][u'status']
                if state == 2:
                    break
            except Exception as e:
                # 记录
                self.log.error("！！！！！！！！！！！！okex交易结果查询异常！！！！！！！！！！！！")
                self.log.error(e)

        self.log.info('查询交易结果  %s' % orderResultJson)

        isError = False
        if orderResultJson == '' or orderResultJson is None or state == 0 or state == 1:
            try:
                cancelResult = okcoinFuture.future_cancel(position.symbol, contractType='quarter', orderId=mapData[u"orderId"])
                if json.loads(cancelResult)[u'result'] or (not json.loads(cancelResult)[u'result'] and json.loads(cancelResult)[u'error_code'] == 20015):
                    self.log.info("********************okex交易撤单成功  订单ID %s ********************" % mapData[u"orderId"])
                    orderResultJson = okcoinFuture.future_orderinfo(position.symbol, contractType='quarter',
                                                                    orderId=mapData[u"orderId"],
                                                                    status="2", currentPage="1", pageLength="50")
                else:
                    self.okexErrorFrozen(position, tradeType, num)
                    self.log.error(cancelResult)
                    self.log.error("！！！！！！！！！！！！okex交易撤单失败！！！！！！！！！！！！")
                    isError = True
            except Exception as e:
                self.okexErrorFrozen(position, tradeType, num)
                self.log.error(e)
                self.log.error("！！！！！！！！！！！！okex交易撤单异常！！！！！！！！！！！！")
                isError = True

        if orderResultJson == '' or orderResultJson is None:
            self.okexErrorFrozen(position, tradeType, num)
            self.log.error(cancelResult)
            self.log.error("！！！！！！！！！！！！okex交易查询交易结果失败！！！！！！！！！！！！")
            return enum.TransactionResult.Fail.value

        resultJson = json.loads(orderResultJson)
        okexResultJson = resultJson[u'orders'][0]
        # 记录交易结果到表中
        okexResultMapper.insertOkexResult(position.id, okexResultJson)

        if isError :
            return enum.TransactionResult.Fail.value

        type = okexResultJson[u'type']

        dealPrice = int(okexResultJson[u'unit_amount'])
        #卖出/买入数量
        dealAmount = float(okexResultJson[u'deal_amount'])
        priceAvg = float(okexResultJson[u'price_avg'])
        fee = float(okexResultJson[u'fee'])

        #有交易成交更新仓位
        if dealAmount > 0:
            #扣除手续费
            position.baseCoin += fee

            if type == 1 or type == 2 :
                position.baseCoin -= dealAmount * dealPrice
                if type == 1:
                    position.tradeCoin += dealAmount
                else:
                    position.nullCoin += dealAmount
            elif type == 3 or type == 4 :
                if type == 3:
                    openPriceAvg = mapData[u'buyPriceAvg']  # 查仓位的结算基准价
                    profitCoin = dealPrice / openPriceAvg - dealPrice / priceAvg
                    position.tradeCoin -= dealAmount
                else :
                    openPriceAvg = mapData[u'sellPriceAvg']  # 查仓位的结算基准价
                    profitCoin = dealPrice / priceAvg - dealPrice / openPriceAvg
                    position.nullCoin -= dealAmount

                position.baseCoin += dealAmount * dealPrice + dealAmount * profitCoin * priceAvg

            positionMapper.setPosition(position)
        return enum.TransactionResult.OK.value

    def send(self, exchange, account, position, num, tradeType):
        """
        发送 买入/卖出 代币申请
        :param exchange: 交易所
        :param strategy: 策略
        :param symbol:  币种
        :param accountType: 交易账号类型
        :param isbuy:  买入/卖出表示 1买入 2卖出
        :param tradeType:   交易类型  okex 买入使用  1开多   2开空
        :return:
        """
        if type(exchange).__name__ != 'Exchange':
            raise RuntimeError('exchange must be an Exchange enum')

        self.log.info('-----------------------------------------------------------------')
        self.log.info(u"交易所 : %s " % exchange.value)
        self.log.info(u"交易用户 : %s " % account.accessKey)
        if position is None:
            self.log.info(" %s 没有可以交易的仓位" % account.accessKey)
            return enum.TransactionResult.NoCanPositionFail.value
        if exchange == enum.Exchange.HuoBi:
            return self.huobiSpotServer(account , position , num , tradeType)
        elif exchange == enum.Exchange.OKEx:
            okexServerResult = self.okexFuturesServer(account, position, num, tradeType)
            if okexServerResult[u'code'] != 1000:
                return okexServerResult

            self.okexResult(account, position, okexServerResult[u'data'], tradeType, num)
            return enum.TransactionResult.OK.value
        elif exchange == enum.Exchange.BitMex:
            bitmexServerResult = self.bitmexFuturesServer(account, position, num, tradeType)
            if bitmexServerResult[u'code'] != 1000:
                return bitmexServerResult
