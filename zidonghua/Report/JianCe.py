import logging

import zidonghua.Common.Mysql_Con
from datetime import datetime


time = datetime.now().strftime('%Y-%m-%d')

def sele_p():
    zidonghua.Common.Mysql_Con.data= zidonghua.Conf.Read_yaml.read_yaml_all('config.yaml')['PRO']
    sql ="select * from contract_center_contract where contract_type='purchase_contract' and createdAt>'{}';".format('2024-6-18')
    purchase_contract = zidonghua.Common.Mysql_Con.sql_select(sql)
    # print(purchase_contract)
    for contract in purchase_contract:
        ContractContractPaymentIterm = contract['id']
        sql2 =("SELECT * FROM contract_center_contract_payment_condition "
               "WHERE contract_payment_iterm IN (SELECT id FROM contract_center_contract_payment_iterm"
               " WHERE ContractContractPaymentIterm='{}')".format(ContractContractPaymentIterm))
        payment_condition =zidonghua.Common.Mysql_Con.sql_select(sql2)
        if len(payment_condition) ==6 :
            print( "付款节点不为空,合同id为:'{}'".format(contract['id']))
        else:
            logging.error("付款节点为空,合同id为:'{}'".format(contract['id']) +"\n"+
                              "合同状态:'{}'".format(contract['status']))

sele_p()
