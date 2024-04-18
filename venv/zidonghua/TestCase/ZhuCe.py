import zidonghua.Common.Requests
import zidonghua.Interface.Register
import zidonghua.Conf.Settings

def zhuce(mobile):
    zidonghua.Interface.Register.data['mobile']= mobile
    zidonghua.Interface.Register.data['nickname']= '自动化创建test'+mobile[:3]+mobile[-2:]
    zidonghua.Interface.Register.data['email']= mobile+'@qq.com'
    response = zidonghua.Common.Requests.HttpUtil(
        url = zidonghua.Conf.Settings.url + zidonghua.Interface.Register.api,
        json=zidonghua.Interface.Register.data).post()
    return response.json()

if __name__ == '__main__':
    print(zhuce('13500000009'))

