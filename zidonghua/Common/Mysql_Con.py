import zidonghua.Conf.Read_yaml
import zidonghua.Conf.Mysql



data = zidonghua.Conf.Read_yaml.read_yaml_all('config.yaml')['uat']

# data = zidonghua.Conf.Read_yaml.read_yaml_all('config.yaml')['dev']
def sql_select(sql):
    con = zidonghua.Conf.Mysql.MysqlConnectCom(db=data['DB'],user=data['MYSQL_USERNAME'],
                     passwd=data['MYSQL_PASSWORD'],host=data['MYSQL_HOST'])
    con._connect_db()
    return con.select_operation(sql=sql)








