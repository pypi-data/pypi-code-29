import redis
import json

host = 'localhost'
port = 6379
db_i = 0
r = redis.StrictRedis(host=host, port=port, db=db_i) 

def add_to_job_requests(request):
    """
    job_request Queue
    """
    try:
        r.publish('JOB_REQUEST', json.dumps(request))
    except:
        print("Error adding request to the message queue!")

def get_data(id_, type_, path=None):
    """
    This API is responsible for fetching data from Redis Database
    :param id_: Connection ID
    :param path: Data Path
    :return: Response Data
    """
    raw_data = r.get(id_)
    if not raw_data:
        return {"success": False, "message": "DATA DOESN\'T EXIST"}
    try:
        data = json.loads(raw_data)
    except:
        return {"success": False, "message": "DATA DOESN\'T EXIST"}
    if path:
        if data[path]:
            if time.time() - data['path']['ts'] <= 0.2 :
                return {"success": True, "data": data['path']}
            else:
                return {"success": False, "message": "STALE"}
        else:
            return {"success": False, "message": "DATA DOESN\'T EXIST"}
    else:
        return data

