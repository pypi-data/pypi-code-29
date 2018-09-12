#!/local/bin/env python3
# -*- coding:utf8 -*-
# Fangbinbin

import jenkins
class UseJenkin:
    '''连接指定的Jenkins服务器'''
    def __init__(self,Url,UserName=None,Password=None):
        self.Server = jenkins.Jenkins(Url,username=UserName,password=Password)
    def Version(self):
        return self.Server.get_version()

    def CreateJob(self,JobName):
        pass

    def GetJobInfo(self,JobName):
        ResultInfo = self.Server.get_job_info(JobName)
        return ResultInfo

    def CopyJob(self,SourceJobName,DestJobName):
        self.Server.copy_job(SourceJobName,DestJobName)
        self.Server.disable_job(DestJobName)

    def GetJobKeyValue(self,JobName,KeyName):
        #print(self.Server.get_job_config(JobName))
        if KeyName == 'LastBuildNum':
            LastBuildNum = self.Server.get_job_info(JobName)['lastBuild']['number']
            return LastBuildNum
        elif KeyName == 'NextBuildNum':
            NextBuildNum = self.Server.get_job_info(JobName)['nextBuildNumber']
            return NextBuildNum
        elif KeyName == 'ParameterInfo':
            PropertyInfo = self.Server.get_job_info(JobName)['property']
            ParameterInfo = {}
            for i in PropertyInfo:
                if 'parameterDefinitions' in i:
                    #print(i['parameterDefinitions'])
                    for j in i['parameterDefinitions']:
                        info = j['defaultParameterValue']
                        ParameterInfo[info['name']] = info['value']
                        if 'choices' in j and info['value'] == '-P production clean package':
                            ParameterInfo[info['name']] = '-P production clean package -DskipTests'
            return ParameterInfo
        conf = self.Server.get_job_info(JobName).get("actions")[0]
        KeyValue = ""
        if conf == {}:
            return None
        for cf in conf.get("parameterDefinitions"):
            if (cf.get("name")) == KeyName:
                KeyValue = cf.get('defaultParameterValue').get("value")
                break
        return KeyValue

    def UpdateGit(self,Giturl,JobName):
        jobxml = self.Server.get_job_config(JobName)
        sourceGitUrl = self.GetJobKeyValue(JobName,"GIT_URL")
        newGitJobXml = jobxml.replace(sourceGitUrl,Giturl,1)
        self.Server.reconfig_job(JobName,newGitJobXml)

    def CreateView(self,ViewName):
        pass
    def ViewInfo(self,ViewName):
        '''获取指定视图信息'''
        ViewInfo = self.Server.get_jobs(view_name=ViewName)
        return ViewInfo
    def ViewAddJob(self,ViewName,JobName):
        '''添加Job到指定视图'''
        print("开始在视图%s中添加Job%s"%(ViewName,JobName))
        ViewXml = self.Server.get_view_config(ViewName)
        NewViewXml = ViewXml.replace('    <comparator class="hudson.util.CaseInsensitiveComparator"/>','    <comparator class="hudson.util.CaseInsensitiveComparator"/>\n    <string>%s</string>' %JobName,1)
        #print(ViewXml)
        self.Server.reconfig_view(ViewName,NewViewXml)
        print("在视图%s 中添加Job：%s 成功！" %(ViewName,JobName))

    def BuildJob(self,JobName,parameters=None):
        '''构建Job'''
        self.Server.build_job(JobName,parameters=parameters)
    def BuilfInfo(self,JobName,BuildNum):
        '''获取指定构建信息'''
        BuildJobInfo = self.Server.get_build_info(JobName,BuildNum)
        return BuildJobInfo


if __name__ == "__main__":
    pass