api ='/api/user/web/login/identify'

data = {
    "isApp": False,
    "password": "a1234567",
    "identify": "18178952877"
}

api1 = "/api/user/web/login/login-by-sms-code"
data1 = {"mobile":"18178952877" , "smsCode": "111111", "isApp": False, "prefix": "86"}