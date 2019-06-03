import requests
import time
from lxml import etree
import json

login_url = "http://passport.transrush.com/Login.aspx"

headers = {
    "Cookie": "_ga=GA1.2.1118471410.1543457100; ASP.NET_SessionId=1ptiod3rmah3xm55wcw22zbi; SESSION_COOKIE=10.104.2.215; Qs_lvt_271648=1558667595%2C1558940795%2C1559094987%2C1559182321%2C1559537430; _gid=GA1.2.1561361238.1559537431; Hm_lvt_5f97b18de3423180375703d5f0196b0c=1559094987,1559182323,1559182537,1559537432; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1559537432; Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1559094987,1559182323,1559182537,1559537432; UM_distinctid=16b1bacb655447-0efe347dea5af9-506d3d71-1aeaa0-16b1bacb6562fc; User::UserID=Y243F3i2u034Q3k0C0z1q1Z2M0u060L0; User::UserCode=r3H0I2Y3B281J02021i0p360m1A1T0C0; User::EMail=r0C3h252U1z2M3L212u3h2f2o362V1K0q3M303e2y2o004C0a0C0B1n1a3A1r3V2; User::TUserID=970346; User::TrueName=%e5%ad%99%e9%9b%b7; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; User::Mobile=33e1F0o2Y3n3v1C1H0b150d033R364e3; TransrushUserInfo=vnU1l7WyoC25oJCcZekcLJHWYB3gCy1M9zxpA1E1l5MCHvp+Vt9CBIupJyf/r/3AbxGGVdPzeMLHdgjJgLSZRKfhV5hW7GZYJ4xlCrziaIJSlG/1EibfGfe/HG6GfaJwcA2O2EQC/y9FIUo8ksGS1KWOkuvwMBXVtmGh+hl+iBdO6220ZQJQmVmJAAXoWRwrRNzZob3kMw47ZB1UPFACBmxB5/ympDxI; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1558940795,1559095020,1559182540,1559537435; acw_tc=2a51041915595417491942798ec707d7386388d57b85d18fd9ea836a05; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1559542700; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1559542700; Qs_pv_271648=1709891864176000300%2C3145039315561948700%2C4095880868987471000%2C319298075625734200%2C547973747949857150; _gat=1",
    "Referer": "http://passport.transrush.com/Login.aspx",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

session = requests.session()
res = session.get(url=login_url,headers=headers)

all_url = "http://member.transrush.com/Ajax/AjaxTransportInfo.aspx?actionType=1&pidx=1&psize=10&day=180&pid=&wid=&orderno=&tuid=970346&time=1559549108802"



def product_detail(orderNo):
    order_url = "http://member.transrush.com/Member/parcelDetail.aspx?fromTab=dqs&orderNo=" + orderNo
    product_html = etree.HTML(session.get(url=order_url, headers=headers).text)
    trs_list = product_html.xpath("//dl[@class='detail']/dd/table/tr")
    order_status = product_html.xpath("//*[@id='detail']/ul/li[1]/span[2]/strong/text()")[0].strip()
    order_address = product_html.xpath("//*[@id='detail']/dl[1]/dd/ul/li[2]/span[2]/text()")[0].strip()
    order_track_No = product_html.xpath("//*[@id='detail']/dl[2]/dd/ul/li[3]/span[2]/text()")[0].strip()
    order_address = product_html.xpath("//*[@id='detail']/dl[2]/dd/ul/li[4]/span[2]/text()")[0].strip()
    order_time = product_html.xpath("//*[@id='detail']/dl[2]/dd/ul/li[6]/span[2]/text()")[0].strip()
    order_price = product_html.xpath("//*[@id='detail']/dl[2]/dd/ul/li[7]/span[2]/text()")[0].strip()

    # order_details = product_html.xpath("//*[@id='detail']/dl[2]/dd/ul[@class='clearfix']/li")
    # for d in range(1,7):
    #     print(order_details[d].xpath("./span[2]/text()")[0].strip())

    for i in trs_list:
        if i.attrib != "":
            print(order_time,orderNo,order_status,order_track_No,i.xpath("./td[3]/@title")[0],order_address,order_price,)


# product_name(mulit_html)
res_all = session.get(url=all_url,headers=headers).text
res_all_dict = json.loads(res_all)
order_list = res_all_dict['ResultList']
for i in range(len(order_list)):
    orderNo = order_list[i]['OrderNo']
    if orderNo.startswith('DD'):
        product_detail(orderNo)


