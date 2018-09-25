import boto3
import json
import os.path
import filecmp
import time
import logging
import sys
import yaml


from shutil import copyfile

def client_session(region):
    session = boto3.session.Session(region_name=region)
    ec2_client = session.client('ec2')
    return ec2_client


def get_nodes(client, name_filter):
    logging.info('Finding all EC2 instances using [%s] name filter', name_filter)

    custom_filter = [{
    'Name':'tag:Name',
    'Values': [name_filter]
    }]
    response = client.describe_instances(Filters=custom_filter)
    return response

def get_nodes_name(nodes):
    nodes_list = []
    for r in nodes['Reservations']:
        for i in r['Instances']:
            for tag in i['Tags']:
                if tag['Key'] == 'Name':
                    nodes_list.append(tag['Value'])
    return nodes_list

def get_nodes_ip(nodes):
    nodes_list = []
    for r in nodes['Reservations']:
        for i in r['Instances']:
            nodes_list.append(i['PrivateIpAddress'])
    return nodes_list

def format_sd_data(nods_list, role):
    logging.info('Formatting all the EC2 instances for [%s] role', role)
    sd_data = [
               {
                "targets": nods_list,
                "lables": {
                           "role": role,
                           }
                }
               ]
    return sd_data

def write_sd_tmp (data, path, file_name):
    save_path = os.path.join(path, file_name+".json")
    logging.info('Saving list of EC2 instances in the temporary location: [%s] ', save_path)
    with open(save_path, 'w') as outfile:
        json.dump(data, outfile)
    return save_path


def detect_changes (src_file, des_file):
    if os.path.isfile(src_file) and os.path.isfile(des_file):
        return filecmp.cmp(src_file, des_file)
    else:
        return False

def copy_sd_file(src_file, des_file):
    try:
        diff = detect_changes (src_file, des_file)
        if not diff:
            copyfile(src_file, des_file)
            logging.info('Nodes list changed, Updating the [%s] file', des_file)
        else:
            logging.info('Did not find any changes to the nodes list')
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:")

def sd_file_per_role(region, name_filter, target_type, role, tmp_dir, prometheus_target_dir):
    client = client_session(region)
    ec2_nodes = get_nodes(client, name_filter)
    if target_type == 'name':
        target_names = get_nodes_name(ec2_nodes)
    else:
        target_names = get_nodes_ip(ec2_nodes)
    data = format_sd_data (target_names, role)
    tmp_sd_file = write_sd_tmp(data, tmp_dir, role)
    prometheus_target_file = os.path.join(prometheus_target_dir, role+".json")
    copy_sd_file(tmp_sd_file, prometheus_target_file)

def main():
    while True:
        configfilepath = os.getenv('CONFIG_FILE', '/etc/aws_node_discovery.conf')

        try:
            with open(configfilepath, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)

            query_interval = cfg['interval']
            logfile = cfg['logfile']
            loglevel = logging.INFO
            tmp_dir = cfg['temp_directory']
            prometheus_target_dir = cfg['prometheus_target_directory']

            logging.basicConfig(filename=logfile,
                                level=loglevel,
                                format='%(asctime)s - %(levelname)s - %(message)s')

            logging.info('Starting AWS Node Discovery for Prometheus targets ...')
            while True:
                for role, params in cfg['targets'].iteritems():
                    sd_file_per_role(params['region'], params['filter'], params['type'], role , tmp_dir, prometheus_target_dir)
                time.sleep(query_interval)
        except:
            error = sys.exc_info()[0]
            logging.basicConfig(filename='/var/log/aws_node_discovery.logs',
                                level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')
            logging.critical('Got this error trying to load the [%s] config: [%s]', configfilepath, error)

if __name__ == '__main__':
    main()
