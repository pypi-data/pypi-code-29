#coding:utf-8

import json


class payback():
    def __init__(self,filename='payback.json',**kwargs):
        self.context = context (filename, 'r',**kwargs)
        print(("话术加载完毕",self.context))
        '''
        self.dict = {
                     'hello':self.hello,
                     'nohear': self.nohear, 'default_next': self.current, 'yes': self.yes,
                     'answer_yes': self.answer_yes, 'answer_no': self.answer_no, 'payback_yes': self.payback_yes,
                     'payback_no': self.payback_no, 'unknow': self.unknow, 'other': self.other, 'bye': self.bye}
        '''
    def fetchNext(self,func):
       #print (("dict-v:",self.dict.keys()))
        return self.context.fetch(func)
    def fetchQA(self,qestionNum):
        return self.context.fetchQA(qestionNum)


class context():
    def __init__(self,filename,fype,**kwargs):
        self.dialogContexts=None
        self._end=False
        self.dialog=None
        self.qestion_annswer=None
        self.score=0
        self.attitude=['92','无还款诚意']
        self.timesCtrl={'nohear':0,'what':0,'an2':0}
        if kwargs:
            self.dialog =kwargs
            self.current_dn = self.dialog['flow']
            self.qestion_annswer = self.dialog['qestionAnnswers']
        else:
            if fype=='r':
                self.load (filename)
            else:
                self.current_dn = None
                self.save (filename)

    def load(self,fileName):
        with open (fileName, 'r') as load_f:
            print ( '读取json话术')
            self.dialog = json.load (load_f)
            self.current_dn=self.dialog['flow']
            #print (("flow:", self.current_dn))
            self.qestion_annswer=self.dialog['qestionAnnswers']
            #print (("qestionAnnswers:",self.qestion_annswer))

    def save(self,fileName):
        with open (fileName, 'w') as dump_f:
            print  ( '保存json话术')
            json.dump (self.current_dn,dump_f)

    '''
    def fetch(self,which='next'):
        #print "current:", self.current_dn,type(self.current_dn)
        temp = None
        if self.current_dn:
            if ( which=='yes'):
                if 'left' in self.current_dn:
                    temp=self.current_dn["left"]
                else:
                    if  'next' in self.current_dn:
                        temp=self.current_dn["next"]
            elif which=='no':
                if 'right' in self.current_dn:
                    temp=self.current_dn["right"]
                else:
                    if  'next' in self.current_dn:
                        temp=self.current_dn["next"]
            elif which == "next" and  'next' in self.current_dn:
                temp = self.current_dn["next"]
            elif which == "nohear":
                dcontexts =self.getDialogContexts()
                aisaysLen=len(dcontexts)
                if  aisaysLen>0:
                    return dcontexts[aisaysLen-1]["ai"]
            elif which=='bye':
                self.end=True
            else  :#如果无法识别就走next
                if 'next' in self.current_dn :
                    temp = self.current_dn["next"]
            if temp and (not ( "left" in temp or "right" in temp or "next" in temp)):
                self.end=True
        if  temp :
            self.current_dn=temp
        return  temp
    '''

    @property
    def  end(self):
        if   self.current_dn and  'isEnd' in self.current_dn:
            return  self.current_dn['isEnd'].lower()=='true' or self._end
        return  self._end

    def check_over_times(self,position):
        if position == 'nohear':
            if  self.timesCtrl[position]>2:#超过两次走主流,人没听清，重复上一句
                self.timesCtrl[position] = 0
                return  'next'
            else:
                self.timesCtrl['nohear'] += 1
                return  position
        elif  position == 'an2':
            if  self.timesCtrl[position]>2:#超过两次走结束,不好意思，您刚说什么啊
                return  'AN2end'
            else:
                self.timesCtrl['an2'] += 1
                return  position
        elif position == 'what':
            if self.timesCtrl[position] >2:#超过两次走结束,您说什么,我没听清楚,能再说一遍吗？
                return 'WHATend'
            else:
                self.timesCtrl['what'] += 1
                return  position
        elif position=='no':
            return  'right'
        elif position=='yes':
            return  'left'
        self.timesCtrl[position]=0
        return  position

    def get_sub_node(self,position):
        v_position=self.check_over_times(position)
        if  v_position =='nohear':
            dcontexts = self.getDialogContexts()
            aisaysLen = len(dcontexts)
            if aisaysLen > 0:
                tnode= dcontexts[aisaysLen - 1]["ai"]
            else:
                tnode=None
        else:
            tnode=self.current_dn[v_position] if v_position in self.current_dn else None
            if  (position=='yes' or   position=='no') and  tnode is  None:
                tnode = self.current_dn['next'] if 'next' in self.current_dn else None
        return tnode

    def  fetch(self,query='next'):
        queryR=None
        if  self.current_dn:#话术正确加载，当前节点明确
            if  query.lower()=='bye':
                self._end=True
            else:
                queryR = self.get_sub_node(query.lower())
        if  queryR :
            self.current_dn=queryR
         #话术未加载或者加载失败,或者通话要结束了,当前节点不明确
        return  queryR

    def fetchQA(self,qestionNum):
        if self.qestion_annswer and len(self.qestion_annswer) and qestionNum in self.qestion_annswer:
            return  self.qestion_annswer[qestionNum]
        return  None

    def appendDialogContext(self,aisay,mansay=""):
        if not self.dialogContexts:
            self.dialogContexts=[]
        self.score+=self.caculateScore (mansay)
        self.attitude=self.check_attitude(aisay)
        self.dialogContexts.append({"man":mansay,"ai":aisay})

    def check_attitude(self,ai):
       # print(type(ai),ai)
        if  'score' in ai :
            for k, v in ai["score"].items():
                if  k =='attitude':
                    return  v
        return  self.attitude

    '''
    评分应该取电脑上一句说的，因为人说的话是对电脑上一句的回答
    '''
    def caculateScore(self,man):
        if len(self.dialogContexts)>0 :
            ai=self.dialogContexts[-1]
            if "ai" in ai and "score" in ai["ai"]:
                for k,v in ai["ai"]["score"].items():
                    if k in man or man in k:
                        return  v
        return  0

    def getDialogContexts(self):
        if not self.dialogContexts:
            self.dialogContexts=[]
        return  self.dialogContexts

