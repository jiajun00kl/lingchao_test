import yaml
import os


parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
yaml_directory = os.getcwd().replace('Conf','Config')

def read_yaml_all(file_yaml):
    yaml_path = os.path.join(r"D:\lingchao project\PycharmProjects\pythonProject\.venv\zidonghua\Config",
                             file_yaml)
    try:
        # 打开文件
        with open(yaml_path,"r",encoding = "utf-8") as f:
            data = yaml.load(f, Loader = yaml.FullLoader )
            return data
    except :
        try:
            # 打开文件
            with open(yaml_path, "r", encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.UnsafeLoader)
                return data
        except:
            return None



def read_yaml(n,k,file_yaml):
    yaml_path = os.path.join(r"D:\lingchao project\PycharmProjects\pythonProject\.venv\zidonghua\Config",
                             file_yaml)
    # 打开文件
    with open(yaml_path,"r",encoding="utf-8") as f:
        data = yaml.load(f,Loader= yaml.FullLoader)
        try:
            #判断传入的n是否在存在
            if n in data.keys():
                return data[n][k]
            else:
                print(f"n：{n}不存在")
        except Exception as e :
            print(f"key值{e}不存在")


def write_key_yaml(key,data,file_yaml):  # key:value 覆盖写入
    yaml_path = os.path.join(r"D:\lingchao project\PycharmProjects\pythonProject\.venv\zidonghua\Config",
                             file_yaml)
    try:
        with open(yaml_path, 'w',encoding="utf-8") as f:
            dict_temp = {}
            dict_temp[key] = data
            yaml.dump(dict_temp, f,allow_unicode = True )
        return ('写入成功')
    except Exception as e :
        return e


def repair_data(key, data,file_yaml):    # 追加写入
    yaml_path = os.path.join(r"D:\lingchao project\PycharmProjects\pythonProject\.venv\zidonghua\Config",
                             file_yaml)
    with open(yaml_path, encoding='utf-8') as f:
        dict_temp = yaml.load(f, Loader=yaml.FullLoader)
        try:
            dict_temp[key] = data
        except:
            if not dict_temp:
                dict_temp = {}
            dict_temp.update({key:data})
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(dict_temp, f, allow_unicode=True)


def write_yaml(data, file_yaml): #  覆盖写入
        yaml_path = os.path.join(r"D:\lingchao project\PycharmProjects\pythonProject\.venv\zidonghua\Config",
                             file_yaml)
        with open(yaml_path, 'w',encoding="utf-8") as f:
            yaml.dump(data, f,allow_unicode=True)



