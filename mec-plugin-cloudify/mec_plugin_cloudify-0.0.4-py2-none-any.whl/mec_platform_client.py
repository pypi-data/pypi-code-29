# -*- coding: utf-8 -*-

"""
Copyright 2017-2018 Pantelis A. Frangoudis

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import httplib
import sys
import getopt
import json
import base64
import urlparse

host = '10.10.10.12'
port = 13000
apiurl = "/api/"

registrar_host = "127.0.0.1"
registrar_port = 80
registrar_service_catalogue_url = "/v1/services"

"""
Retrieves the service endpoint for the given service name
from the service catalogue.
"""
def get_service_endpoint(service_name):
  # get services from catalogue
  catalogue = exec_request(registrar_host, registrar_port, registrar_service_catalogue_url)

  # search for the service with the given service_name
  services = json.loads(catalogue)
  for s in services:
    # extract the service endpoint
    if s["NAME"] == service_name:
      method = s["METHOD"]
      info = urlparse.urlparse(s["_URL"])
      host = info.netloc.split(":")[0]
      if ":" in info.netloc:
        port = int(info.netloc.split(":")[1])
      else:
        port = 80
      return host,port,info.path,method
  return None
  
# Executes an HTTP requests and returns the body
def exec_request(host, port, url, method = None, body = None):
  headers = {"Content-Type":"application/json"}
  host = str(host)
  port = str(port)
  if not method:
    method = "GET"
    
  cnx = httplib.HTTPConnection(host, port)

  if body:
    cnx.request(method=method, url=url, body=json.dumps(body), headers=headers)
  else:
    cnx.request(method=method, url=url)
  
  r = cnx.getresponse()
  #print r.status, r.reason
  if r.status != 200:
    raise Exception(str(r.status) + " "+ str(r.reason))
  return r.read()
  
##########################################
##########################################

# Redirect traffic per URL
# Req body should include "type": 1, "url": host-name, "mec-ipaddr"
# data is of the format host-name:ipaddr
def redirect_by_name(data):
  tokens = data.split("|")
  name = tokens[0]
  mecip = tokens[1]
  mecmac = tokens[2]

  # get service endpoint
  host,port,url,method = get_service_endpoint("traffic/redir-by-name")

  # select any method other than delete
  md = "POST" # default
  for m in method:
    if m is not "DELETE":
      md = m
      break
  
  print "Request service mec traffic"
  print "[" + md + "]\t" + url
  print "------------------------"
  body = {
    "type": 1,
    "url": name,
    "mec-ipaddr": mecip,
    "mec-macaddr": mecmac
  }   
  response = exec_request(host, port, url, method=md, body=body)
  #print response
  return response

# data is in the format imsi|protocol|origip|port|mecaddr|mecmac
# protocol: 1 for tcp, 2 for udp, 0 for any
def redirect_by_traffic_type(data):
  tokens = data.split("|")
  body = {
    "type": 2,
    "ue_list": [tokens[0]],
    "transport": tokens[1],
    "service_ip": tokens[2],
    "mec_ipaddr": tokens[3],
    "mec_macaddr": tokens[4],
    "port": tokens[5]
  }

  # get service endpoint
  host,port,url,method = get_service_endpoint("traffic/redir-by-type")

  # select any method other than delete
  for m in method:
    if m is not "DELETE":
      md = m
      break

  print "Request redirection by traffic type [proto-ip-port]"
  print "[" + md + "]\t" + url
  print "------------------------"
  response = exec_request(host, port, url, method=md, body=body)
  print response
  return response

# This is supposed to be executed by the SGW
# Data are in the format IMSI|UE-IP|eNB-IP|teid (teid is in hex notation)
# (This one directly interacts with the MEC platform API)
def handle_data_plane(data):
  tokens = data.split("|")
  imsi = tokens[0]
  ueaddr = tokens[1]
  enbaddr = tokens[2]
  tunid = tokens[3]

  url = apiurl + "mp2/spgw" 

  print "Adding/Updating a UE (handle-data-plane req)"
  print "[POST]\t" + url
  print "-----------------------"

  body = {
    "imsi": imsi,
    "ue_ip": ueaddr,
    "enb_s1u_ip": enbaddr,
    "enb_s1u_teid": tunid
  }

  response = exec_request(host, port, url, method="POST", body=body)

  print response 

def reset_ovs():
  url = apiurl + "platform/traffic/reset" 

  print "Resetting OVS"
  print "[POST]\t" + url
  print "-----------------------"

  response = exec_request(host, port, url, method="POST")

  print response 

def delete_redirect_by_name(data):
  tokens = data.split("|")
  name = tokens[0]
  mecip = tokens[1]
  mecmac = tokens[2]

  # get service endpoint
  host,port,url,method = get_service_endpoint("traffic/redir-by-name")
  print host, port, url, method
  print "Remove redirection name (url)" 
  print "[DELETE]\t" + url
  print "------------------------"
  body = {
    "type": 1,
    "url": name,
    "mec-ipaddr": mecip,
    "mec-macaddr": mecmac
  }   
  response = exec_request(host, port, url, method="DELETE", body=body)
  #print response
  return response

def delete_redirect_by_traffic_type(data):
  tokens = data.split("|")
  body = {
    "type": 2,
    "ue_list": [tokens[0]],
    "transport": tokens[1],
    "service_ip": tokens[2],
    "mec_ipaddr": tokens[3],
    "mec_macaddr": tokens[4],
    "port": tokens[5]
  }

  # get service endpoint
  host,port,url,method = get_service_endpoint("traffic/redir-by-type")
  print "Remove redirection name (url)" 
  print "[DELETE]\t" + url
  print "------------------------"
  response = exec_request(host, port, url, method="DELETE", body=body)
  print response
  return response

action_handle_data_plane = False
action_traffic = False
action_redirect = False
action_reset = False
action_delete = False
action_test = False

what = ""

#-h: handle data plane
#-r: redirect by url
#-t: redirect based on protocol-port-ip for a specific IMSI
#-x X: delete X-type of service (r for redirectiion by name, t for redirection by traffic type)
#-d: data

# Examples
# python mec-platform-client.py -r -d "in.gr|192.168.0.200|52:54:00:12:34:bb"
# python mec-platform-client.py -h -d "208930100001114|172.16.0.2|10.10.10.1|0xca6fe0dd"
# python mec-platform-client.py -t -d "208930100001114|1|172.16.0.101|192.168.0.200|52:54:00:12:34:cc|80"
# python mec-platform-client.py -R
# python mec-platform-client.py -x r -d "in.gr|192.168.0.200|52:54:00:12:34:bb"
# python mec-platform-client.py -x t -d "208930100001114|1|172.16.0.101|192.168.0.200|52:54:00:12:34:cc|80"

myopts, args = getopt.getopt(sys.argv[1:], "ThtrRx:d:")
for o, a in myopts:
  if o == "-h":
    action_handle_data_plane = True
  elif o == "-t":
    action_traffic = True
  elif o == "-r":
    action_redirect = True
  elif o == "-d":    
    data = a
  elif o == "-R":
    action_reset = True
  elif o == "-x":
    action_delete = True
    what = a
  elif o == "-T":
    action_test = True

if action_handle_data_plane:
  handle_data_plane(data)

if action_traffic:
  redirect_by_traffic_type(data)

if action_redirect:
  redirect_by_name(data)

if action_reset:
  reset_ovs()

if action_delete:
  if what == "r":
    # delete redirect-by-URL 
    delete_redirect_by_name(data)
  elif what == "t":
    # delete redirect-by-traffic-type
    delete_redirect_by_traffic_type(data) 

if action_test:
  print get_service_endpoint("traffic/redir-by-name")

