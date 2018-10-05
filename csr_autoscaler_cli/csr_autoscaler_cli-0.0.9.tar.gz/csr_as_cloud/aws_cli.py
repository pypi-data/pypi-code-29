import boto3
from botocore.client import Config
import json
from collections import OrderedDict
import os
import calendar
import ast
from datetime import datetime

endpoint_url = {
    "us-east-1": "https://s3.amazonaws.com",
    "us-east-2": "https://s3-us-east-2.amazonaws.com",
    "us-west-1": "https://s3-us-west-1.amazonaws.com",
    "us-west-2": "https://s3-us-west-2.amazonaws.com",
    "eu-west-1": "https://s3-eu-west-1.amazonaws.com",
    "eu-central-1": "https://s3-eu-central-1.amazonaws.com",
    "ap-northeast-1": "https://s3-ap-northeast-1.amazonaws.com",
    "ap-northeast-2": "https://s3-ap-northeast-2.amazonaws.com",
    "ap-south-1": "https://s3-ap-south-1.amazonaws.com",
    "ap-southeast-1": "https://s3-ap-southeast-1.amazonaws.com",
    "ap-southeast-2": "https://s3-ap-southeast-2.amazonaws.com",
    "sa-east-1": "https://s3-sa-east-1.amazonaws.com"
}

class cloud():
    def __init__(self):
        pass

        # CloudWatchEventName = "Every_60_Seconds"

    def setup_settings(self, args):
        print("We are setting %s" % args['<storage_name>'])
        self.settings = {}
        self.settings["cloud"] = "aws"
        self.settings["storage_name"] = args['<storage_name>']
        if args['<profile>'] is not None:
            self.settings['profile'] = args['<profile>']
        else:
            self.settings['profile'] = 'default'

        if args['<region>'] is None:
            self.region = os.getenv('AWS_DEFAULT_REGION', "us-east-1")
        else:
            self.region = args['<region>']

        self.settings['region'] = self.region

    def init_settings(self, settings):
        self.settings = settings
        session = boto3.Session(profile_name=self.settings['profile'], region_name=self.settings['region'])

        self.s3_client = session.client('s3', endpoint_url=endpoint_url[self.settings['region']], config=Config(
            s3={'addressing_style': 'virtual'}, signature_version='s3v4'))

        self.cw_event_client = session.client('events')
        self.cwlogs_client = session.client('logs')
        self.lambda_client = session.client('lambda')
        self.sns_resource = session.resource('sns')
        self.ec2_resource = session.resource('ec2')
        self.ec2_client = session.client('ec2')

    def download_file_json(self, bucket_name, filename):
        download_directory = "/tmp/"
        directory = "AutoScaler/"

        self.s3_client.download_file(
            bucket_name,
            directory +
            filename,
            download_directory +
            filename)
        with open(download_directory + filename) as json_data:
            return json.load(json_data, object_pairs_hook=OrderedDict)


    def upload_file_json(self, data, bucket_name, filename):
        directory = "AutoScaler/"
        download_directory = "/tmp/"
        with open(download_directory + filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        self.s3_client.upload_file(download_directory + filename,
                          bucket_name, directory + filename)

    def upload_file(self, bucket_name, filename):
        directory = "AutoScaler/"
        download_directory = "/tmp/"

        self.s3_client.upload_file(download_directory + filename,
                              bucket_name, directory + filename)




    def print_log_entries(self, group_name, minutes, log_time):
        all_streams = []

        # group = "Group Name: %s" % group_name.split("-", 1)[1]
        group = "Group Name: %s" % group_name
        print("*" * 60 + "%s" % group + "*" * 60)
        end_time = calendar.timegm(datetime.utcnow().utctimetuple()) * 1000
        start_time = end_time - int(minutes) * 60 * 1000

        stream_batch = self.cwlogs_client.describe_log_streams(logGroupName=group_name)
        all_streams += stream_batch['logStreams']
        while 'nextToken' in stream_batch:
            stream_batch = self.cwlogs_client.describe_log_streams(
                logGroupName=group_name, nextToken=stream_batch['nextToken'])
            all_streams += stream_batch['logStreams']
            print((len(all_streams)))

        stream_names = [stream['logStreamName'] for stream in all_streams]

        for stream in stream_names:
            logs_batch = cwlogs_client.get_log_events(
                logGroupName=group_name,
                logStreamName=stream,
                startTime=start_time,
                endTime=end_time)
            for event in logs_batch['events']:
                event_parts = event['message'].strip('\n').split("\t")
                if "RequestId" not in event_parts[0]:
                    if len(event_parts) > 2:
                        if log_time:
                            timelog = event_parts[1]
                        else:
                            timelog = ""
                        print(event_parts[0], "\t", timelog, event_parts[3])
                    else:
                        print(event_parts[0])
                else:
                    print(event['message'].strip('\n'))
            while 'nextToken' in logs_batch:
                logs_batch = self.cwlogs_client.get_log_events(
                    logGroupName=group_name,
                    logStreamName=stream,
                    nextToken=logs_batch['nextToken'],
                    startTime=start_time,
                    endTime=end_time)
                for event in logs_batch['events']:
                    event_parts = event['message'].strip('\n').split("\t")
                    if "RequestId" not in event_parts[0]:
                        if log_time:
                            timelog = event_parts[1]
                        else:
                            timelog = ""
                        print(event_parts[0], "\t", timelog, event_parts[3])
                    else:
                        print(event['message'].strip('\n'))


    def print_all_logs(self, stack_name, args):

        print("-" * 60 + "Stack Name: %s" % stack_name + "-" * 60)

        response = self.cwlogs_client.describe_log_groups(
            logGroupNamePrefix="/aws/lambda/" + stack_name,
        )
        if 'minutes' in args:
            minutes = args['minutes']
        else:
            minutes = 30

        if 'log_group' in args:
            group = args['log_group']
        else:
            group = "autoscaler"

        end_time = calendar.timegm(datetime.utcnow().utctimetuple())
        start_time = end_time - int(minutes) * 60
        print response['logGroups']
        for lg in response['logGroups']:
            log_group_name = lg['logGroupName']
            log_group = log_group_name
            print(group)
            print(log_group)
            if group is not None and group not in log_group:
                continue

            self.print_log_entries(
                log_group_name, int(
                    minutes), True)


    def print_spoke_logs(self, args, function_name):
        try:
            response = self.lambda_client.get_function(
                FunctionName=function_name
            )
            bucket_prefix = response['Configuration']['Environment']['Variables']['bucket_prefix']

            transit_config = ast.literal_eval(
                self.s3_client.get_object(
                    Bucket=self.settings["Bucket"],
                    Key=bucket_prefix +
                    "transit_vpc_config.txt")['Body'].read())

            arn = transit_config["SNS_SPOKE_ARN"]

            topic = self.sns_resource.Topic(arn)
            for subscription in topic.subscriptions.all():
                lambda_arn = subscription.attributes['Endpoint']
                function_split = lambda_arn.split("function:")
                print("function_split", function_split)
                if "spoke-broker" in function_split[1]:
                    stack_name_split = function_split[1].split("-spoke-broker")
                else:
                    stack_name_split = function_split[1].split("-AutoScalerStack")

                stack_name = stack_name_split[0]
                print_all_logs(stack_name, args)
            else:
                print("No Spokes are subscribed.")
        except Exception as e:
            print(e)
            pass