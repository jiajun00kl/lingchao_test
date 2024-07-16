import time
import uuid
import datetime

def timestamp():
    timestamp = int(time.time()) * 1000
    return timestamp
    print(timestamp)  #13位时间戳

def fan_timestamp(timestamp_ms):
    timestamp_s = timestamp_ms / 1000
    # 转换为datetime对象
    dt_object = datetime.datetime.fromtimestamp(timestamp_s)

    # 格式化输出年月日
    formatted_date = dt_object.strftime('%Y-%m-%d')

    return formatted_date
def time_13():
    now = datetime.datetime.now()
    if now.month ==2:
        month =now.month + 1
    else:
        month = now.month
    one_year_later =datetime.datetime(year=now.year + 1, month=month, day=now.day, hour=now.hour, minute=now.minute,
                             second=now.second,microsecond=now.microsecond)
    timestamp_seconds = now.timestamp()
    startdate = int(timestamp_seconds * 1000)
    enddate = int(one_year_later.timestamp() * 1000)
    return startdate ,enddate


def Uuid():
    uid1 = uuid.uuid4()
    uid2 = uuid.uuid1()
    return uid1

