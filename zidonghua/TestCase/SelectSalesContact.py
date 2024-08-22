import zidonghua.Common.Requests
import zidonghua.Interface.Select_Sales_Contact
import zidonghua.Common.Cookies


def select_contact(mobile,project_name):
    cookies = zidonghua.Common.Cookies.get_cookies(mobile)
    zidonghua.Interface.Select_Sales_Contact.data['searchValues']['project.name']['value'] = project_name
    response = zidonghua.Common.Requests.HttpUtil(
        url= zidonghua.Interface.Select_Sales_Contact.url,
        json=zidonghua.Interface.Select_Sales_Contact.data,cookies=cookies).post()
    return response.json()
# print(select_contact('18178952878','test1采购项目'))
