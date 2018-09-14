from slackclient import SlackClient
from swimlane import Swimlane
from swimlane.core.search import EQ, NOT_EQ, CONTAINS, EXCLUDES, GT, GTE, LT, LTE
import ConfigParser
import json
import os
import re


class Setup:
    def __init__(self, config_file, sw_config, sw_inputs, sw_user=None):
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(config_file)
        for k, v in sw_inputs.iteritems():
            #setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)
            setattr(self, k, v)
        for k, v in sw_config.iteritems():
            #setattr(self, re.sub(r'([a-z])([A-Z])', r'\1_\2', k).lower(), v)
            setattr(self, k, v)
        #for k, v in sw_user.iteritems():
        #   setattr(self, k, v)


    def mergeTwoDicts(self, x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z


class Records(Setup):
    def __init__(self, config_file, sw_config, sw_inputs, proxySet=False, slack=False):

        self.Config = ConfigParser.ConfigParser()
        self.Config.read(config_file)

        Setup.__init__(self, config_file, sw_config, sw_inputs)
        if slack:
            self.sc = SlackClient(self.slackToken)
        self.swimlane = Swimlane(self.swimlaneApiHost, self.swimlaneApiUser, self.swimlaneApiKey, verify_ssl=False)
        if proxySet:
            os.environ['HTTPS_PROXY'] = self.proxyUrl
        self.app = None
        self.appRaw = None
        self.recordData = None
        self.recordKeys = []
        self.records = None
        self.recordsFieldOnly = {}
        self.report = None
        self.slackApiResults = {}
        self.sw_config = sw_config
        self.sw_inputs = sw_inputs

    def getApp(self, appId):
        self.app = self.swimlane.apps.get(id=appId)

    def getAppRaw(self, appId):
        self.app = self.swimlane.apps.get(id=appId)
        self.appRaw = self.app._raw

    def getRecord(self, appId, recordId):
        self.getApp(appId)
        self.records = self.app.records.get(id=recordId)

    def getRecordKeys(self, records):
        keys = []
        for r in records:
            keys.append(r[0])
        self.recordKeys = keys

    def getReport(self, appId, reportName, filters=None, limit=50):
        self.getApp(appId)
        self.report = self.app.reports.build(reportName, limit=limit)
        if filters is not None:
            for f in filters:
                self.report.filter(f[0], f[1], f[2])

    def pullFieldsFromRecords(self, appId, recordId, fields=None):
        self.getRecord(appId, recordId)
        self.getRecordKeys(self.records)
        if fields:
            oldFields = self.records
            newFields = {}
            for f in fields:
                if f in self.recordKeys:
                    newFields[f] = oldFields[f]
            self.recordsFieldOnly = newFields
            return self.recordsFieldOnly
        else:
            return self.records

    def buildSwOutputs(self, integrationId, appId, recordId, includedFields, staticFields=None):
        self.pullFieldsFromRecords(appId, recordId, includedFields)
        if staticFields:
            self.recordData = self.mergeTwoDicts(self.mergeTwoDicts(self.mergeTwoDicts(self.sw_config, self.sw_inputs), self.recordsFieldOnly), staticFields)
        else:
            self.recordData = self.mergeTwoDicts(self.mergeTwoDicts(self.sw_config, self.sw_inputs), self.recordsFieldOnly)
        self.sendSlackMessage(self.formatSlackMessage(integrationId))
        return self. recordData

    def formatSlackMessage(self, integrationId):
        return self.Config.get('Slack', integrationId).format(self.ApplicationId, self.RecordId)

    def sendSlackMessage(self, message):
        self.setSlackChannel()
        slackChannel = self.recordData['Slack Channel']
        if self.recordData['Slack TS'] is not None:
            threadTs = self.recordData['Slack TS']
            self.slackApiResults = self.sc.api_call("chat.postMessage", channel=slackChannel, text=message, thread_ts=threadTs)
        else:
            self.slackApiResults = self.sc.api_call("chat.postMessage", channel=slackChannel, text=message)
            self.recordData['Slack TS'] = self.slackApiResults['message']['ts']

    def setSlackChannel(self):
        if self.recordData['Slack Channel'] is None:
            self.recordData['Slack Channel'] = self.Config.get('Slack', 'primaryChannel')
