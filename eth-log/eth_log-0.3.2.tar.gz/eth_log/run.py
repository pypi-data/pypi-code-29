import unittest
import json
from eth_log.models.topic import Topic
from eth_log.models.topic_parser import TopicParser
from eth_log.models.eventlog import EventLog


json_str = """
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "beneficiary",
          "type": "address"
        },
        {
          "indexed": false,
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Payment",
      "type": "event"
    }
     """
json_obj = json.loads(json_str)
topic = Topic.from_json(json_obj)
topic_parser = TopicParser(topic)
test_log_json_str = """
{  "address": "0xd1ceeeeee83f8bcf3bedad437202b6154e9f5405",
  "topics": [
    "0xd4f43975feb89f48dd30cabbb32011045be187d1e11c8ea9faa43efc35282519",
    "0x00000000000000000000000001963046fd848cc436bd76b8917b287fb67af2f9"
  ],
  "data": "0x00000000000000000000000000000000000000000000000001a60ff877510000",
  "blockNumber": "0x5f2577",
  "logIndex": "0x74",
  "gasPrice": "0xb368f480",
  "gasUsed": "0x13871",
  "timeStamp": "0x5b86c260",
  "transactionHash": "0xc2146292fc3876145fc75af47a382ed23e94d8f9e8e6b7a3aca16ac6ee5373c8",
  "transactionIndex": "0x56"
}
"""
eventlog_obj = EventLog.from_etherscan_json(json.loads(test_log_json_str))       
eventlog_obj = topic_parser.parse(eventlog_obj)
print(eventlog_obj.event_name)
print(eventlog_obj.data[0].get('name'))
print(eventlog_obj.data[0].get('type'))
print(eventlog_obj.data[0].get('value'))
print(eventlog_obj.data[1].get('name'))
print(eventlog_obj.data[1].get('type'))
print(eventlog_obj.data[1].get('value'))

