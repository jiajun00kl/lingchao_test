import zidonghua.Report.datasource
import zidonghua.Common.Cookies



def test1(mobile,url,data):
    cookies = zidonghua.Common.Cookies.login_cookies(mobile)
    headers ={'x-trantor-app':'parana_B2B%E8%BF%90%E8%90%A5%E6%9D%BF%E5%9D%97'}
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=url,
        json=data, cookies= cookies,headers=headers).post()
    return response1.json()

def run_test1():
    url= zidonghua.Report.datasource.url10
    data = zidonghua.Report.datasource.data102
    print(test1(mobile='18178952876',url=url,data=data))
    print(test1(mobile='18178952877',url=url,data=data))
    print(test1(mobile='18178952878',url=url,data=data))
    print(test1(mobile='13500000005',url=url,data=data))
    print(test1(mobile='18520611771',url=url,data=data))
    print(test1(mobile='18778786868',url=url,data=data))


def test2(mobile,password,url,data):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile=mobile,password=password)
    headers = {'x-trantor-app': 'parana_B2B%E8%BF%90%E8%90%A5%E6%9D%BF%E5%9D%97'}
    response1 = zidonghua.Common.Requests.HttpUtil(
        url=url,
        json=data, cookies=cookies, headers=headers).post()
    return response1.json()

def run_test2():
    url =zidonghua.Report.datasource.pro_url10
    data = zidonghua.Report.datasource.data102
    print(test1(mobile='16600000000',password='aA18779130155',url=url,data=data))
    print(test2(mobile='13728640121',password='qw13728640121',url=url,data=data))


if __name__ == '__main__':
    run_test1()








