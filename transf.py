import requests
import json
import time
from lxml import etree

TotalCount = ""
TotalPage = ""

url = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?actionType=1&pidx=2&psize=10&day=180&pid=&wid=&orderno=&tuid=970346&time=1564630239163"
headers = {
    "Cookie":"_ga=GA1.2.1118471410.1543457100; UM_distinctid=16b1bacb655447-0efe347dea5af9-506d3d71-1aeaa0-16b1bacb6562fc; acw_tc=7a0e2b1715625661889874299ed8517f45eec9171e547a7c7cd1797505; _gid=GA1.2.691808177.1564544265; ASP.NET_SessionId=qjbpak55sb2teu453tdmgwqi; SESSION_COOKIE=10.104.2.214; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1564109993,1564378681,1564544265,1564626439; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1564626439; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1564109994,1564378681,1564544265,1564626439; Qs_lvt_271648=1563505205%2C1564109993%2C1564378681%2C1564544265%2C1564626439; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1564109998,1564378689,1564544274,1564626445; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1564630144; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1564630144; Qs_pv_271648=1134887599974917000%2C3801520556734190000%2C4397507205045277700%2C3437578153660680700%2C1813135252209329700",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
session = requests.session()
response = session.get(url=url,headers=headers).text
resultDicts = json.loads(response)
totalCount = resultDicts['TotalCount']
totalPage = int(resultDicts['TotalPage'])+1

for i in range(1,totalPage):
    url_one = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?actionType=1&pidx=" + str(i) +"&psize=10&day=180&pid=&wid=&orderno=&tuid=970346&time="+str(round(time.time()*1000))
    result_one_dicts = json.loads(session.get(url=url_one,headers=headers).text)
    for j in result_one_dicts['ResultList']:
        if j['OrderNo'].startswith('DD'):
            orderNo = j['OrderNo']
            url_one_details = "http://member.transrush.com/Member/parcelDetail.aspx?fromTab=sy&orderNo="+orderNo
            print(url_one_details)
            url_one_html = etree.HTML(session.get(url=url_one_details,headers=headers).text)
            # 转运中，待出库，
            transf_state = url_one_html.xpath("//*[@id='detail']/ul/li[1]/span[2]/strong/text()")[0]
            # 收件人
            transf_receiver = url_one_html.xpath("//dl[@class='address']/dd/ul/li[1]/span[@class='cont']/text()")[0]
            address = url_one_html.xpath("//dl[@class='address']/dd/ul/li[2]/span[@class='cont']/text()")[0]
            transf_receiver += transf_receiver + address[address.find("市")+1:address.find("市")+4]
            # 包裹信息
            transf_trackingNo = url_one_html.xpath("//ul[@class='clearfix']/li[3]/span[2]/text()")[0]
            # 运费
            transf_total_cost = url_one_html.xpath("//*[@id='detail']/dl[5]/dd/ul/li[4]/span[2]/text()")[0]
            # 转运路线
            transf_service_lines = url_one_html.xpath("//ul[@class='clearfix']/li[5]/span[2]/text()")[0]
            # 申报时间
            transf_declare_time = url_one_html.xpath("//ul[@class='clearfix']/li[6]/span[2]/text()")[0]
            # 国内派件信息
            transf_sendingNo = url_one_html.xpath("//ul[@class='clearfix']/li[4]/span[2]/text()")[0]
            # 转运仓
            transf_storeHouse = url_one_html.xpath("//ul[@class='clearfix']/li[2]/span[2]/text()")[0]
            # 备注
            transf_remark = url_one_html.xpath("//ul[@class='clearfix']/li[8]/span[2]/text()")[0]

            print(orderNo,transf_state,transf_receiver,transf_trackingNo,transf_total_cost,transf_service_lines,transf_declare_time,transf_sendingNo,transf_storeHouse,transf_remark)

            # 包裹详情
            # for i in url_one_html.xpath("//dl[@class='detail']/dd/table/tr"):
            #     if i.attrib != "":
            #         # 判断tr/td[1] rowspan属性
            #         if len(i.xpath("./td[1][@rowspan]")):
            #             # print(i.xpath("./td[1]/@title"Ωn)[0],i.xpath(".//span/text()")[0])
            #             rowspan = i.xpath("./td[1]/@rowspan")[0]
            #             if int(rowspan) > 1:
            #                 print(
            #                     zy_orderCreateTime,"\t",# 2019-05-30
            #                     str(i.xpath('./td[3]/@title')[0]),"\t",#SZ13 homage 1 eb 5.7
            #                     toStrStrip(order_tracking),"\t",#94055096999375084386gitgggggg94
            #                     toStrStrip(order_status),"\t",#待出库
            #                     toStrStrip(order_domestic),"\t",# 9737401138397(青岛邮政包裹)
            #                     toStrStrip(orderID),"\t",#DD190528281703
            #                     toStrStrip(order_total_cost),"\t",#￥134.00
            #                     order_address[order_address.find("市")+1:order_address.find("市")+4],"\t",#东城区
            #                     toStrStrip(order_transfer_depot),"\t",#美国波特兰（免税仓）
            #                     toStrStrip(order_service_lines),"\t",#关税补贴模式-鞋服关税补贴专线
            #                     toStrStrip(order_post_time).split(" ")[0]
            #                 )
            #                 # 获取第三个a标签后面的第N个标签："//a[@id='3']/following-sibling::*[N]"
            #                 for j in range(2, int(rowspan) + 1):
            #                     xpath_express = "./following-sibling::tr[" + str(j - 1) + "]"
            #                     row_conten = i.xpath(xpath_express)
            #                     for k in row_conten:
            #                         print(
            #                             zy_orderCreateTime,"\t",# 2019-05-30
            #                             str(k.xpath('./td[2]/@title')[0]),"\t",# SZ13 homage 1 eb 5.7
            #                             toStrStrip(order_tracking),"\t",# 94055096999375084386gitgggggg94
            #                             toStrStrip(order_status),"\t",# 待出库
            #                             toStrStrip(order_domestic),"\t",# 9737401138397(青岛邮政包裹)
            #                             toStrStrip(orderID),"\t",# DD190528281703
            #                             toStrStrip(order_total_cost),"\t",# ￥134.00
            #                             order_address[order_address.find("市") + 1:order_address.find("市") + 4],"\t",# 东城区
            #                             toStrStrip(order_transfer_depot),"\t",# 美国波特兰（免税仓）
            #                             toStrStrip(order_service_lines),"\t",# 关税补贴模式-鞋服关税补贴专线
            #                             toStrStrip(order_post_time).split(" ")[0]
            #                         )
            #             else:
            #                 print(
            #                     zy_orderCreateTime,"\t",# 2019-05-30
            #                     str(i.xpath('./td[3]/@title')[0]),"\t",# SZ13 homage 1 eb 5.7
            #                     toStrStrip(str(i.xpath('./td[1]/@title')[0])),"\t",# 94055096999375084386gitgggggg94
            #                     toStrStrip(order_status),"\t",# 待出库
            #                     toStrStrip(order_domestic),"\t",# 9737401138397(青岛邮政包裹)
            #                     toStrStrip(orderID),"\t",# DD190528281703
            #                     toStrStrip(order_total_cost),"\t",# ￥134.00
            #                     order_address[order_address.find("市") + 1:order_address.find("市") + 4],"\t",# 东城区
            #                     toStrStrip(order_transfer_depot),"\t",# 美国波特兰（免税仓）
            #                     toStrStrip(order_service_lines),"\t",# 关税补贴模式-鞋服关税补贴专线
            #                     toStrStrip(order_post_time).split(" ")[0]
            #                 )
