from functools import partial
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import zidonghua.Tkinter.Win_BuyGoods as Win_BuyGoods
import zidonghua.Tkinter.liucheng as liucheng


root = ttk.Window(themename='litera',)  # 使用 ttkbootstrap 创建窗口对象
root.geometry('600x600+100+100')
root.title('测试用例')
root.wm_attributes('-topmost', 1)


def Place_Order():
    top = ttk.Toplevel()
    top.geometry('600x600+100+100')
    top.title('下单')
    root.withdraw()
    username_str_var = ttk.StringVar()
    password_str_var = ttk.StringVar()
    projectname_str_var = ttk.StringVar()
    project_var = ttk.StringVar()
    item_id_var = ttk.StringVar()
    saleName_var = ttk.StringVar()
    contract_id_var = ttk.StringVar()
    requireInstall_var = ttk.StringVar()
    paymentType_var = ttk.StringVar()
    response_var = ttk.StringVar()
    ttk.Label(top, width=10).grid()
    ttk.Label(top, text='用户名：').grid(row=1, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=username_str_var).grid(row=1, column=2, sticky=ttk.W)
    ttk.Label(top, text='密码：').grid(row=2, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=password_str_var).grid(row=2, column=2, sticky=ttk.W)

    def get_project():
        mobile = username_str_var.get()
        password = password_str_var.get()
        projectnames = Win_BuyGoods.Win_User(mobile, password).Cha_Project()
        projectname = ','.join(projectnames)
        projectname_str_var.set(projectname)
        ttk.Entry(top, textvariable=projectname_str_var, width=150).grid(row=3, column=2, sticky=ttk.E)

    ttk.Button(top, text="获取项目信息", bootstyle=PRIMARY, command=get_project
               ).grid(row=3, column=1, sticky=ttk.W, pady=10)

    ttk.Label(top, text='选择的项目：').grid(row=4, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=project_var).grid(row=4, column=2, sticky=ttk.W)

    ttk.Label(top, text="加入购物车的商品id：多个商品请加',' ").grid(row=5, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=item_id_var, width=50).grid(row=5, column=2, sticky=ttk.W)

    def cha_hetong():
        mobile = username_str_var.get()
        password = password_str_var.get()
        projectname = project_var.get()
        itemIds = item_id_var.get()
        Win_BuyGoods.Win_User(mobile, password).jia_cart(itemIds, projectname)
        Win_BuyGoods.Win_User(mobile, password).Cha_Cart(projectname)
        result = Win_BuyGoods.Win_User(mobile, password).Cart_Submit(projectname)
        contractnames = []
        for i in range(len(result['result']['salesContract'])):
            contractnames.append(result['result']['salesContract'][i]['saleName'])
        saleName = ','.join(contractnames)
        saleName_var.set(saleName)
        ttk.Entry(top, textvariable=saleName_var, width=150).grid(row=6, column=2, sticky=ttk.E)

    ttk.Button(top, text="获取合同信息", bootstyle=PRIMARY, command=cha_hetong
               ).grid(row=6, column=1, sticky=ttk.W, pady=10)

    ttk.Label(top, text='选择的合同：').grid(row=7, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=contract_id_var).grid(row=7, column=2, sticky=ttk.W)

    ttk.Label(top, text='是否安装').grid(row=8, column=1, sticky=ttk.W, pady=10)
    ttk.Combobox(top, values=(True, False),
                textvariable=requireInstall_var).grid(row=8, column=2, sticky=ttk.W,pady=10)

    ttk.Label(top, text='付款方式').grid(row=9, column=1, sticky=ttk.W, pady=10)
    ttk.Combobox(top, values=('account', 'offline', 'online'),
                 textvariable=paymentType_var).grid(row=9, column=2,sticky=ttk.W)

    def xiadan():
        mobile = username_str_var.get()
        password = password_str_var.get()
        projectname = project_var.get()
        contractname = contract_id_var.get()
        requireInstall = requireInstall_var.get()
        paymentType = paymentType_var.get()
        result = Win_BuyGoods.Win_User(mobile, password).buyGoods(projectname, contractname, paymentType,
                                                                  requireInstall)
        response_var.set(result['result']['orderCodes'])
        ttk.Entry(top, textvariable=response_var, width=100).grid(row=10, column=2, sticky=ttk.E,pady=10)

    ttk.Button(top, text="下单，获取订单号", bootstyle=PRIMARY, command= xiadan
               ).grid(row=10, column=1, sticky=ttk.W, pady=10)
    def destroy():
        top.destroy()
        root.deiconify()
    ttk.Button(top, text='返回用例操作',command=destroy,bootstyle =SUCCESS).grid(row=11, column=1, padx=1, pady=1)

ttk.Button(root, text='1.点击进入下单', command= Place_Order,width=20).grid(row=1,column=1, pady=1)

def Run_Order():
    top = ttk.Toplevel()
    top.geometry('600x600+100+100')
    top.title('订单操作')
    root.withdraw()
    so_code_var =ttk.StringVar()
    getGoodsNum_var = ttk.StringVar()
    ttk.Label(top, text='请输入so需求单号').grid(row=1, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable= so_code_var).grid(row=1, column=2, sticky=ttk.W)
    def jiedan():
        so_code = so_code_var.get()
        result = liucheng.order(so_code).SupplierAcceptanceOrder()

    ttk.Button(top, text="供应商接单", bootstyle=PRIMARY, command= jiedan
               ).grid(row=2, column=3, sticky=ttk.W, pady=10)

    def dinghuo():
        getGoodsNum =getGoodsNum_var.get()
        so_code = so_code_var.get()
        result2 = liucheng.order(so_code).order_goods(getGoodsNum)


    ttk.Label(top, text='采购商订货数量').grid(row=3, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=getGoodsNum_var).grid(row=3, column=2, sticky=ttk.W)
    ttk.Button(top, text="采购商订货", bootstyle=PRIMARY, command=dinghuo
               ).grid(row=3, column=3, sticky=ttk.W, pady=10)
    def queren():
        so_code = so_code_var.get()
        result3 = liucheng.order(so_code).confirm_orders()

    ttk.Button(top, text="供应商确认订货", bootstyle=PRIMARY, command=queren
               ).grid(row=4, column=3, sticky=ttk.W, pady=10)

    def shenqing():
        so_code = so_code_var.get()
        result4 = liucheng.order(so_code).apply_shipment()

    ttk.Button(top, text="供应商申请发货", bootstyle=PRIMARY, command=shenqing
               ).grid(row=5, column=3, sticky=ttk.W, pady=10)

    def shenhe():
        so_code = so_code_var.get()
        result5 = liucheng.order(so_code).to_ship()
    ttk.Button(top, text="平台审核(高风提交OA)", bootstyle=PRIMARY, command=shenhe
                   ).grid(row=6, column=3, sticky=ttk.W, pady=10)
    def oa_shenhe():
        so_code = so_code_var.get()
        result6 = liucheng.order(so_code).oa_approver()

    ttk.Button(top, text="高风险OA审核通过)", bootstyle=PRIMARY, command=oa_shenhe
               ).grid(row=7, column=3, sticky=ttk.W, pady=10)

    def dao_yan():
        so_code = so_code_var.get()
        result7 = liucheng.order(so_code).order_accept()

    ttk.Button(top, text="到货验收)", bootstyle=PRIMARY, command= dao_yan
               ).grid(row=8, column=3, sticky=ttk.W, pady=10)

    def an_yan():
        so_code = so_code_var.get()
        result9 = liucheng.order(so_code).Install_accept()

    ttk.Button(top, text="安装验收)", bootstyle=PRIMARY, command=an_yan
               ).grid(row=9, column=3, sticky=ttk.W, pady=10)


    jiedian_var = ttk.StringVar()
    ttk.Label(top, text='选择直接完成节点',bootstyle =INFO).grid(row=12, column=1, sticky=ttk.W, pady=10)
    ttk.Combobox(top, values=('到发货审批', '发货完成','验收完成'),
                 textvariable=jiedian_var).grid(row=12, column=2, sticky=ttk.W)

    def jiedian_wancheng():
        jiedian = jiedian_var.get()
        so_code = so_code_var.get()
        getGoodsNum = getGoodsNum_var.get()
        if jiedian == '到发货审批':
            result = liucheng.order(so_code).SupplierAcceptanceOrder()
            result2 = liucheng.order(so_code).order_goods(getGoodsNum)
            result3 = liucheng.order(so_code).confirm_orders()
            result4 = liucheng.order(so_code).apply_shipment()
        elif jiedian == '发货完成':
            result = liucheng.order(so_code).SupplierAcceptanceOrder()
            result2 = liucheng.order(so_code).order_goods(getGoodsNum)
            result3 = liucheng.order(so_code).confirm_orders()
            result4 = liucheng.order(so_code).apply_shipment()
            result5 = liucheng.order(so_code).to_ship()
            result6 = liucheng.order(so_code).oa_approver()
        elif jiedian == '验收完成':
            result = liucheng.order(so_code).SupplierAcceptanceOrder()
            result2 = liucheng.order(so_code).order_goods(getGoodsNum)
            result3 = liucheng.order(so_code).confirm_orders()
            result4 = liucheng.order(so_code).apply_shipment()
            result5 = liucheng.order(so_code).to_ship()
            result6 = liucheng.order(so_code).oa_approver()
            result7 = liucheng.order(so_code).order_accept()
            result8 = liucheng.order(so_code).Install_accept()
        else:
            print('没有获取到节点')
    ttk.Button(top, text="确认完成节点",bootstyle =INFO, command=jiedian_wancheng
               ).grid(row=12, column=3, sticky=ttk.W, pady=10)
    def destroy():
        top.destroy()
        root.deiconify()
    ttk.Button(top, text='返回用例操作',command=destroy,
               bootstyle =SUCCESS).grid(row=15, column=1, padx=1, pady=1)
ttk.Button(root, text='2.订单正向流程操作', command=Run_Order,width=20).grid(row=2,column=1, pady=2)


def tuihuo():
    top = ttk.Toplevel()
    top.geometry('600x600+100+100')
    top.title('订单操作')
    root.withdraw()
    ordercode_var =ttk.StringVar()
    tuihuo_var =ttk.StringVar()
    deliverycode_var =ttk.StringVar()
    ttk.Label(top, text='请输入订单号').grid(row=1, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=ordercode_var).grid(row=1, column=2, sticky=ttk.W)

    def get_delivery():
        goodscode = ordercode_var.get()
        deliveryOrderInfos = liucheng.getdelivery(goodscode)
        code = ','.join(d['code'] for d in deliveryOrderInfos)
        deliverycode_var.set(code)
        ttk.Entry(top, textvariable=deliverycode_var,width=50).grid(row=2, column=2, sticky=ttk.W)

    ttk.Button(top, text="获取发货单号", bootstyle=PRIMARY, command=get_delivery
               ).grid(row=2, column=1, sticky=ttk.W, pady=10)

    delivery_order_var = ttk.StringVar()
    ttk.Label(top, text='请输入发货单号').grid(row=3, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=delivery_order_var).grid(row=3, column=2, sticky=ttk.W)
    iteminfo_var = ttk.StringVar()
    def get_reverseItem():
        goodscode = ordercode_var.get()
        delivery_order = delivery_order_var.get()
        result2 = liucheng.reverseItem(goodscode,delivery_order)
        list1 = []
        for i in range(len(result2)):
            dict = {}
            dict['itemId'] = result2[i]['itemId']
            dict['canReverseNum'] = result2[i]['canReverseNum']
            dict['reverseNum'] = result2[i]['reverseNum']
            list1.append(dict)
        iteminfo_var.set(list1)
        ttk.Entry(top, textvariable=iteminfo_var, width=100).grid(row=4, column=2, sticky=ttk.W)

    ttk.Button(top, text="获取退货商品信息", bootstyle=PRIMARY, command=get_reverseItem
               ).grid(row=4, column=1, sticky=ttk.W, pady=10)
    tuihuo_var = ttk.StringVar()
    tuinum_var = ttk.StringVar()
    ttk.Label(top, text='输入需退货商品(多个,分离)').grid(row=5, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=tuihuo_var).grid(row=5, column=2, sticky=ttk.W)
    ttk.Label(top, text='输入需退货商品数量(需对应)').grid(row=6, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=tuinum_var).grid(row=6, column=2, sticky=ttk.W)
    def tuihuo_shenqing():
        goodscode = ordercode_var.get()
        delivery_order = delivery_order_var.get()
        tuihuo= tuihuo_var.get()
        tuihuo_num = tuinum_var.get()
        liucheng.goods_rejected(goodscode, delivery_order,tuihuo,tuihuo_num)
        ketui_num.set(reverseNum)
        ttk.Entry(top, textvariable=ketui_num, width=150).grid(row=7, column=2, sticky=ttk.E)

    ttk.Button(top, text="确认退货", bootstyle=PRIMARY, command=tuihuo_shenqing
               ).grid(row=8, column=1, sticky=ttk.W, pady=10)
    def destroy():
        top.destroy()
        root.deiconify()
    ttk.Button(top, text='返回用例操作',command=destroy,
               bootstyle =SUCCESS).grid(row=10, column=1, padx=1, pady=1)


ttk.Button(root, text='3.退货操作', command=tuihuo,width=20).grid(row=3,column=1, pady=2)

def pur_duizhang():
    top = ttk.Toplevel()
    top.geometry('600x600+100+100')
    top.title('订单操作')
    root.withdraw()
    so_code_var = ttk.StringVar()
    ttk.Label(top, text='请输入so需求单号').grid(row=1, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=so_code_var).grid(row=1, column=2, sticky=ttk.W)
    def so_jie():
        so_code = so_code_var.get()
        print(liucheng.settlement_orders(so_code))
    ttk.Button(top, text='1.供应商发起需求单结算', command=so_jie, width=20).grid(row=2, column=1, pady=1)
    def zhangdan_queren():
        so_code = so_code_var.get()
        print(liucheng.settlement_confirmation(so_code))
    ttk.Button(top, text='2.采购商对账单确认', command=zhangdan_queren, width=20).grid(row=3, column=1, pady=1)
    def sheng_duizhang():
        so_code = so_code_var.get()
        print(liucheng.sales_check(so_code))
    ttk.Button(top, text='3.平台销售结算对账单生成', command=sheng_duizhang, width=20).grid(row=4, column=1, pady=1)
    def caigou_queren():
        so_code = so_code_var.get()
        print(liucheng.TestConfirmSales(so_code))
    ttk.Button(top, text='4.采购商确认对账单', command=caigou_queren, width=20).grid(row=5, column=1, pady=1)
    def sheng_shoukuan():
        so_code = so_code_var.get()
        print(liucheng.generate_payment(so_code))
    ttk.Button(top, text='5.平台生成收款单', command=sheng_shoukuan, width=20).grid(row=6, column=1, pady=1)
    ttk.Label(top, text='关联流水去页面操作').grid(row=7, column=1, sticky=ttk.W, pady=10)
    def destroy():
        top.destroy()
        root.deiconify()
    ttk.Button(top, text='返回用例操作',command=destroy,
               bootstyle =SUCCESS).grid(row=8, column=1, padx=1, pady=1)
ttk.Button(root, text='4.采购商对账', command=pur_duizhang,width=20).grid(row=4,column=1, pady=2)

def sup_duizhang():
    top = ttk.Toplevel()
    top.geometry('600x600+100+100')
    top.title('订单操作')
    root.withdraw()
    so_code_var = ttk.StringVar()
    ttk.Label(top, text='请输入so需求单号').grid(row=1, column=1, sticky=ttk.W, pady=10)
    ttk.Entry(top, textvariable=so_code_var).grid(row=1, column=2, sticky=ttk.W)
    def purchase_settlement():
        so_code = so_code_var.get()
        print(liucheng.purchase_settlement(so_code))
    ttk.Button(top, text='1.平台发起采购结算', command=purchase_settlement,
               width=20).grid(row=2, column=1, pady=1)

    def destroy():
        top.destroy()
        root.deiconify()
    ttk.Button(top, text='返回用例操作',command=destroy,
               bootstyle =SUCCESS).grid(row=8, column=1, padx=1, pady=1)
ttk.Button(root, text='5.供应商对账', command=sup_duizhang,width=20).grid(row=5,column=1, pady=2)
root.mainloop()



