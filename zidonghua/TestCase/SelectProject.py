import zidonghua.Common.Requests
import zidonghua.Interface.Select_Project
import zidonghua.Common.Cookies

def select_project(mobile,project_name):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    zidonghua.Interface.Select_Project.data['searchValues']['name']['value'] = project_name
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Select_Project.url,
        json=zidonghua.Interface.Select_Project.data,cookies=cookies).post()
    return response.json()
# print(select_project('18178952878','test1采购项目'))


