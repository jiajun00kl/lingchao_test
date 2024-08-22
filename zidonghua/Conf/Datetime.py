import time
import uuid
import datetime
import random
import string

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


def generate_random_n_digit_integer(n):
    # 确保n是一个正整数
    if n <= 0:
        raise ValueError("n must be a positive integer")

        # 计算起始值和结束值
    # 起始值是1后面跟n-1个0（即10**(n-1)）
    # 结束值是10后面跟n个0再减去1（即10**n - 1）
    start = 10 ** (n - 1)
    end = 10 ** n - 1

    # 生成随机整数
    random_int = random.randint(start, end)
    return random_int



def randomstring():
    pinyin_initials = 'bpmfdtnlgkhjqxzhchshrzcsyw'
    characters = (
        #    string.ascii_letters +
            string.digits +
            pinyin_initials
         #   + string.punctuation.replace("'", "").replace('"','')
    )
    random_string = ''.join(random.choice(characters) for i in range(10))
    return random_string


