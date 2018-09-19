#-*-coding:utf-8-*-
import requests

class Jseq():

    def __init__(self,url,cookies):
        self.url=url
        self.cookies  =cookies
        self.s = requests.session()

    def get_json(self,result,tags):
        for i in tags[:-1]:
            result=result[i]
        return result.get(tags[-1])
    
    def j_dict(self,start,end,tag1,tagsa,tagsb):
        mydict={}
        errs=[]
        if start==end==0:
            try:
                resp=self.s.get(self.url,cookies=self.cookies)
                jsondata = resp.json()
                for result in jsondata[tag1]:
                    mydict[result.get(tagsa)]=result.get(tagsb)
            except Exception as e:
                errs.append(e)
            return mydict,errs
        for i in range(start,end+1):
            url=self.url+str(i)
            try:
                resp=self.s.get(url,cookies=self.cookies)
                jsondata = resp.json()
                for result in jsondata[tag1]:
                    mydict[self.get_json(result,tagsa)]=self.get_json(result,tagsb)
            except Exception as e:
                errs.append("page"+str(i))
        return mydict,errs
    
    def j_list(self,start,end,tag1,*tags):
        mylist=[]
        errs=[]
        if start==end==0:
            try:
                resp=self.s.get(self.url,cookies=self.cookies)
                jsondata = resp.json()
                for result in jsondata[tag1]:
                    mylist.append(result.get(tags))
            except Exception as e:
                errs.append(e)
            return mylist,errs
        for i in range(start,end+1):
            url=self.url+str(i)
            try:
                resp=self.s.get(url,cookies=self.cookies)
                jsondata = resp.json()
                for result in jsondata[tag1]:
                    mylist.append(self.get_json(result,tags))
            except Exception as e:
                errs.append("page"+str(i))
        return mylist,errs

