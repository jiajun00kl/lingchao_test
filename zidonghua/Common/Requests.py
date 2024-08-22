import requests
import json

class HttpUtil:
    def __init__(self, url, headers=None, cookies=None, params=None, json=None, auth=None,verify =None):
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.params = params
        self.json = json
        self.auth = auth
        self.verify = verify

    def get(self):
        try:
            result = requests.get(self.url, cookies=self.cookies, params=self.params)
            return result.json()
        except Exception as e:
            print("get请求错误: %s" % e)

    def post(self):
        try:
            result = requests.post(self.url, headers=self.headers, cookies=self.cookies,
                                   json= self.json,auth=self.auth)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)

    def put(self):
        try:
            result = requests.put(self.url, headers=self.headers,
                                  cookies=self.cookies, params=self.params, data=self.data)
            result.json()
        except Exception as e:
            print("post请求错误: %s" % e)

    def delete(self):
        try:
            result = requests.delete(self.url, headers=self.headers, cookies=self.cookies, params=self.params)
            result.json()
        except Exception as e:
            print("post请求错误: %s" % e)

