import zidonghua.Common.Requests
import zidonghua.Interface.Select_Project_Details
import zidonghua.Common.Cookies
import zidonghua.TestCase.SelectProject

def select_project_details(mobile,project_name):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    project = zidonghua.TestCase.SelectProject.select_project(mobile,project_name)
    zidonghua.Interface.Select_Project_Details.data['queryValues']['id']['value'] = (
        project)['res']['data'][0]['id']
    response = zidonghua.Common.Requests.HttpUtil(
        url=  zidonghua.Interface.Select_Project_Details.url,
        json= zidonghua.Interface.Select_Project_Details.data,cookies=cookies).post()
    return response.json()


# print(select_project_details('18178952878','test1采购项目')['res'])



