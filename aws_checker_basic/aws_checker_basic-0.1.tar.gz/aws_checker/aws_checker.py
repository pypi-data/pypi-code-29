import sys
import os
import boto3
import csv
import yaml
import logging
from botocore.exceptions import ClientError

ec2_name = ""
csv_extention = ".csv"
logging.basicConfig(level=logging.INFO)

def main():
    
    creds = get_config(config_path)
    get_ec2_instances_information(creds)
    get_s3_buckets(creds)
    get_route53_records(creds)


def get_config(config_path):
    try:
        with open(config_path, "r") as aws_config:
            config = yaml.load(aws_config)
            logging.info("Successfully read {} file".format(config_path))
    except IOError:
        logging.info("File {} not found".format(config_path))
        sys.exit(1)
    
    aws_key_id = config['aws_credentials']['aws_access_key_id']
    aws_secret_key = config['aws_credentials']['aws_secret_access_key']
    route_53_file_path = config['file_output_path']['route_53_path']
    route53_file_name = route_53_file_path + 'route53-records.csv'
    s3_bucket_file_path = config['file_output_path']['s3_bucket_path']
    s3_file_name = s3_bucket_file_path + "s3-buckets.csv"
    ec2_instance_file_path = config['file_output_path']['ec2_instance_path']
    return aws_key_id, aws_secret_key, route53_file_name, s3_file_name, ec2_instance_file_path


def get_route53_records(creds):
    
    aws_key_id = creds[0]
    aws_secret_key = creds[1]
    route53_file_name = creds[2]
    

    result = []

    if os.path.exists(route53_file_name):
        os.remove(route53_file_name)
        logging.info(
            "Previous file " + route53_file_name + " have been deleted")

    route53 = boto3.client(
        'route53',
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_secret_key)

    for i in route53.list_hosted_zones()['HostedZones']:
        result.append(i['Name'])  # Domain name
        if 'False' == i['Config']['PrivateZone']:  # Private zone
            result.append('Public')
        else:
            result.append('Private')
        result.append(i['ResourceRecordSetCount'])  # Record Set Count
        result.append(i['Config']['Comment'])  # Comment
        result.append(i['CallerReference'])  # Caller Reference
        result.append(i['Id'])  # Hosted zone

        with open(route53_file_name, "a") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(result)
        result = []

    logging.info("All route53 records has been taken")


def get_s3_buckets(creds):


    aws_key_id = creds[0]
    aws_secret_key = creds[1]
    s3_file_name = creds[3]


    result = []

    if os.path.exists(s3_file_name):
        os.remove(s3_file_name)
        logging.info(
            "Previous file " + s3_file_name + " have been deleted")

    s3 = boto3.resource(
        's3',
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_secret_key)

    for bucket in s3.buckets.all():
        result.append(bucket.creation_date)
        result.append(bucket.name)
        with open(s3_file_name, "a") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(result)
        result = []

    logging.info("All S3 has been checked")


def get_ec2_instances_information(creds):


    aws_key_id = creds[0]
    aws_secret_key = creds[1]
    ec2_instance_file_path = creds[4]


    session = boto3.Session(
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_secret_key,
        region_name='us-west-1')

    client = session.client('ec2')
    regions = [region['RegionName']
               for region in client.describe_regions()['Regions']]

    result = []

    for region in regions:

        if os.path.exists(ec2_instance_file_path + region + csv_extention):
            os.remove(ec2_instance_file_path + region + csv_extention)
            logging.info(
                "Previous file " + ec2_instance_file_path
                + region + csv_extention + " have been deleted")

        ec2 = boto3.resource(
            'ec2', region_name=region,
            aws_access_key_id=aws_key_id,
            aws_secret_access_key=aws_secret_key)

        try:
            for ec2 in ec2.instances.all():
                inst_id = ec2.id

                ec2 = boto3.resource(
                    'ec2', region_name=region,
                    aws_access_key_id=aws_key_id,
                    aws_secret_access_key=aws_secret_key)

                instance = ec2.Instance(inst_id)
                if bool(instance.tags):
                    for tags in instance.tags:
                        if tags["Key"] == 'Name':
                            ec2_name = tags["Value"]
                result.append(ec2_name)  # instance name
                result.append(" ")  # owner
                result.append(" ")  # purpose
                result.append(" ")  # ds domain
                result.append(instance.key_name)  # key_pair
                result.append(" ")  # comment
                result.append(instance.state["Name"])  # status
                result.append(instance.public_dns_name)  # public dns
                result.append(instance.public_ip_address)  # public ip
                result.append(inst_id)  # instance id
                result.append(instance.instance_type)  # instance type
                result.append(instance.image_id)  # image id
                result.append(instance.launch_time)  # launch time
                result.append("not implemented yet")  # availabe zone
                result.append(" ")  # tenancy
                result.append(instance.private_ip_address)  # private ip
                result.append(instance.private_dns_name)  # private dns

                with open(ec2_instance_file_path
                          + region + csv_extention, "a") as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerow(result)

                result = []
        except ClientError as e:
            logging.info(
                "Region {}".format(region)
                + e.response['Error']['Message'])

        logging.info("Region {} has been checked for \
                    EC2 correctly".format(region))


if __name__ == "__main__":
    sys.exit(main())
