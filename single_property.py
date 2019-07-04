import requests
import json
import datetime
requests.urllib3.disable_warnings()

styleId = "575441-015"
single_url = "https://gateway.stockx.com/api/v2/search?facets=%5B%22product_category%22%5D&page=0&query="+styleId+"&currency=USD"
headers = {
    "cookie":"_pxhd=da3658a16d44b6dbd867a581029b61957889041e9810ccdbd1f9441f243cdea4:0347ff51-8734-11e9-b05f-1f5b0595868d; __cfduid=dfc7e838f2ae1e8f8763e8f0f174d3ea31559699307",
    "jwt-authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiaW9zIiwiYXBwX3ZlcnNpb24iOiIzLjEyLjEuMjE3NjUiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA0IDA2OjU5OjQ1IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA4MzEzNzk5MjMwODgzMjg4OCIsImV4cCI6MTU2MDIzNjM4NSwiYXBpX2tleXMiOltdfQ.xqZgCtibknu0rG4GRe3Flc2nUg8vvzA_WvU_cZQhifE",
    "user-agent":"StockX/21765 CFNetwork/978.0.7 Darwin/18.6.0",
    "x-anonymous-id":"8accbad1-f5cf-4b7f-8b59-c5c4ba96f029",
    "app-version":"3.12.1.21765",
    "x-api-key":"99WtRZK6pS1Fqt8hXBfWq8BYQjErmwipa3a0hYxX"
}
objectID = ''
session = requests.session()

def get_url_content(url,session):
    print(session.get(url=url,headers=headers,verify=False).text)
    return session.get(url=url,headers=headers,verify=False).text

# 2019-06-04T17:03:20+00:00--->2019-06-05
def format_time(time):
    time_temp = datetime.datetime.strptime(time.replace("+00:00",".000Z"),"%Y-%m-%dT%H:%M:%S.%fZ")
    deal_time = time_temp + datetime.timedelta(hours=8)
    return deal_time.strftime("%Y-%m-%d")

def usdToRMB(price):
    return '%.2f' % ((price+14)*6.84 + 120)


for i in json.loads(get_url_content(single_url,session))['hits']:
    if i['style_id'] == styleId:
        objectID = i['objectID']

detail_url = "https://gateway.stockx.com/api/v2/products/"+objectID+"?includes=market,360&currency=USD"
detail_dict = json.loads(get_url_content(detail_url,session))
for k,v in detail_dict['Product']['children'].items():
    shoeSize = v['shoeSize']
    highestBid = v['market']['highestBid']
    lowestAsk = v['market']['lowestAsk']
    print(
        styleId,"\t",
        shoeSize,"\t",
        highestBid,"\t",
        usdToRMB(highestBid),"\t",
        lowestAsk,"\t",
        usdToRMB(lowestAsk)
    )

