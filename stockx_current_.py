import requests
import json

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context()

current_url = "https://gateway.stockx.com/api/v2/customers/5350379/buying/current?page=1&order=DESC&limit=40&sort=created_at"

headers = {
    "cookie":"_ga=GA1.2.1819472297.1550000794; __cfduid=db05afbdfa09b3bab34afb9ef271b9e241557704168; _fbp=fb.1.1550835181611.1525308145; rCookie=gyt4qag1v8svqpsl8x4dq; lastRskxRun=1550835259807; rskxRunCookie=0; ajs_group_id=null; ajs_user_id=null; _tl_duuid=aadbffb4-b62e-4e4a-968a-c31a0a86ee1c; _sp_id.1a3e=3be67d7c-6e86-4b63-96d6-0004ec025106.1550000794.2.1550835178.1550000804.f5ee764e-b4a1-408e-9c5a-376d1eed5bdf; intercom-id-h1d8fvw9=02d402de-70b5-4526-ab28-4fe60fd9ef40; ajs_anonymous_id=%22dd3d5190-6657-4ffe-8cbb-2cf18b594cdd%22; cto_lwid=ce2b5704-b25f-4853-811f-897535814153",
    "jwt-authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiaW9zIiwiYXBwX3ZlcnNpb24iOiIzLjEyLjEuMjE3NjUiLCJpc3N1ZWRfYXQiOiIyMDE5LTA2LTA0IDA2OjU5OjQ1IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA4MzEzNzk5MjMwODgzMjg4OCIsImV4cCI6MTU2MDIzNjM4NSwiYXBpX2tleXMiOltdfQ.xqZgCtibknu0rG4GRe3Flc2nUg8vvzA_WvU_cZQhifE",
    "user-agent":"StockX/21765 CFNetwork/978.0.7 Darwin/18.6.0",
    "x-anonymous-id":"8accbad1-f5cf-4b7f-8b59-c5c4ba96f029",
    "app-version":"3.12.1.21765",
    "x-api-key":"99WtRZK6pS1Fqt8hXBfWq8BYQjErmwipa3a0hYxX"

}

response = requests.get(url=current_url,headers=headers,verify=False)
# print(response.text)
current_dict = json.loads(response.text)
for i in current_dict['PortfolioItems']:
    my_bid = i['amount']
    product_title = i['product']['title']
    product_retailPrice = i['product']['retailPrice']
    lowestAsk = i['product']['market']['lowestAsk']
    highestBid = i['product']['market']['highestBid']
    highestBidSize = i['product']['market']['highestBidSize']
    lastSale = i['product']['market']['lastSale']
    # print(my_bid,lowestAsk)
    if int(my_bid) < int(highestBid):
        print(product_title,highestBidSize,"我的出价:",my_bid)


    #"lowestAsk":325,
    #"highestBid":198,
    #"highestBidSize":"7",
    #"lastSale":239,




