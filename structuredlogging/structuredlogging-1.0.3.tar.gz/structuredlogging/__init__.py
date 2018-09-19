import datetime
import json
import logging
import time
import uuid
import six

class StructuredLog(logging.Formatter):
    def format(self, record):
        super(StructuredLog, self).format(record)

        structured = {
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(),
            "metadata": {k: getattr(record, k) for k in ["filename", "funcName", "lineno", "module", "pathname", "process", "processName", "thread", "threadName"]},
            "level": record.levelname,
            "messageId": str(uuid.uuid4())
        }

        if isinstance(record.msg, dict):
            structured.update(record.msg)
        elif isinstance(record.msg, six.string_types):
            structured.update({
                "messageTemplate": record.msg
            })

            if isinstance(record.args, dict):
                structured["message"] = record.msg.format(**record.args)
            else:
                structured["message"] = record.message
        else:
            structured.update({
                "message": record.msg
            })
        
        return json.dumps(structured)