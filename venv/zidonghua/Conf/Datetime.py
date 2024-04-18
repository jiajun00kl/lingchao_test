import time
import uuid

def timestamp():
    timestamp = int(time.time()) * 1000
    return timestamp
    print(timestamp)  #13位时间戳

def Uuid():
    uid1 = uuid.uuid4()
    uid2 = uuid.uuid1()
    return uid1

