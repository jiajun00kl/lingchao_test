import zidonghua.Common.Requests
import zidonghua.Interface.Login
import zidonghua.Conf.Settings


def get_cookies(identify):
    zidonghua.Interface.Login.data['identify'] = identify
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Conf.Settings.url + zidonghua.Interface.Login.api,
        json=zidonghua.Interface.Login.data).post()
    cookies = response.cookies.get_dict()
    return cookies
def login_cookies(mobile):
    zidonghua.Interface.Login.data1['mobile'] = mobile
    response = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Conf.Settings.url + zidonghua.Interface.Login.api1,
        json=zidonghua.Interface.Login.data1).post()
    cookies = response.cookies.get_dict()
    return cookies

def login(identify,password):
    identify = zidonghua.Interface.Login.data['identify']
    password = zidonghua.Interface.Login.data['password']
    response = zidonghua.Common.Requests.HttpUtil(
        url=zidonghua.Conf.Settings.url + zidonghua.Interface.Login.api,
        json=zidonghua.Interface.Login.data).post()
    return response.json()





