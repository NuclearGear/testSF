import requests
import json
import urllib3
urllib3.disable_warnings()
from datetime import datetime,timedelta


bids_products = []
def timeFormat(timeParam):
    return (datetime.strptime(timeParam.replace("+00:00", ".000Z"),'%Y-%m-%dT%H:%M:%S.%fZ') + timedelta(hours=8)).strftime("%Y-%m-%d")

def usdToRMB(price):
    return '%.2f' % ((price+14)*6.84 + 120)

for i in range(1,19):
    current_url = "https://stockx.com/api/customers/5350379/buying/current?sort=name&order=ASC&limit=20&page="+ str(i) +"&currency=USD"

    headers = {
        "cookie":"_pxhd=b1c33f58e23ec75e315678606b824238973c398a5c8a5401627d5b6bdb1c6259:bf696bd1-9e20-11e9-8683-bba9a3c97e33; __cfduid=d940d9d9ac597d06a1bfc7b32bb9e919c1562219909",
        "jwt-authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiaW9zIiwiYXBwX3ZlcnNpb24iOiI0LjAuMi4yMzM1NiIsImlzc3VlZF9hdCI6IjIwMTktMDctMDQgMDU6NTg6NDAiLCJjdXN0b21lcl9pZCI6IjUzNTAzNzkiLCJlbWFpbCI6IjY0NTc0ODcxMkBxcS5jb20iLCJjdXN0b21lcl91dWlkIjoiODBiMmE4NTEtMmUwMi0xMWU5LThkYjktMTJkZWI5MDllOTdjIiwiZmlyc3ROYW1lIjoic3VuIiwibGFzdE5hbWUiOiJsZWkiLCJnZHByX3N0YXR1cyI6IkFDQ0VQVEVEIiwiZGVmYXVsdF9jdXJyZW5jeSI6IlVTRCIsImxhbmd1YWdlIjoiZW4tVVMiLCJzaGlwX2J5X2RhdGUiOm51bGwsInZhY2F0aW9uX2RhdGUiOm51bGwsInByb2R1Y3RfY2F0ZWdvcnkiOiJzbmVha2VycyIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA4MzcyOTI5Mzg1MDg5NTIzMCIsImV4cCI6MTU2MjgyNDcyMCwiYXBpX2tleXMiOltdfQ.rHjz70c2QQJEOPrQkMTu-tV_1kkL53VYWSW0gOcCedo",
        "user-agent":"StockX/22055 CFNetwork/978.0.7 Darwin/18.6.0",
        "x-anonymous-id":"8accbad1-f5cf-4b7f-8b59-c5c4ba96f029",
        "app-version":"3.12.1.21765",
        "x-api-key":"99WtRZK6pS1Fqt8hXBfWq8BYQjErmwipa3a0hYxX"
    }

    response = requests.get(url=current_url,headers=headers,verify=False)
    current_dict = json.loads(response.text)
    for i in current_dict['PortfolioItems']:
        my_bid = i['amount']
        product_title = i['product']['title']
        product_retailPrice = i['product']['retailPrice']
        lowestAsk = i['product']['market']['lowestAsk']
        highestBid = i['product']['market']['highestBid']
        highestBidSize = i['product']['market']['highestBidSize']
        lastSale = i['product']['market']['lastSale']
        styleId = i['product']['styleId']
        expired = i['expiresAt']
        if styleId not in bids_products:
            bids_products.append(styleId)

        print(
            product_title,"\t",
            styleId,"\t",
            highestBidSize,"\t",
            my_bid,"\t",
            highestBid,"\t",
            usdToRMB(highestBid),"\t",
            "1" if my_bid >= highestBid else "0","\t",
            lowestAsk,"\t",
            usdToRMB(lowestAsk), "\t",
            timeFormat(expired),"\t",
        )

print(bids_products)


