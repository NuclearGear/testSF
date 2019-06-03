import requests
import json
from datetime import datetime, timedelta

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "cookie": "__cfduid=d3ffda1cc8ad046bc7a33cf6295f850391555399572; cto_lwid=7e5a7a79-17e6-46fd-89c2-a61b574c5821; _ga=GA1.2.1920518057.1555399492; tracker_device=a9f6f14f-58c1-4f7b-952c-e7cf44bef642; _tl_duuid=04c4167e-fe37-4da2-a250-54d2bcbcb250; _pxvid=e98acc61-6018-11e9-af2b-df2cdcb34bdc; ajs_group_id=null; ajs_anonymous_id=%22eef27aca-e027-4ea5-a342-46c4278a56a1%22; rskxRunCookie=0; rCookie=v6rk8y2hqiaiv1sio3na; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _scid=94d07a5e-6758-4151-9c16-fdeebd9576f9; _fbp=fb.1.1557457428361.36672054; intercom-session-h1d8fvw9=S2dBalpDYzhWZEpQRU9rZGJhNjdaZzl1SzMvWEtQUlo0cFdLL2EyeER1dVlOeldoUTN2Q05Mbm44T1F3dHR5bi0tbWY4blNlbFQwbFB4YmU0YU9TR1Jwdz09--280a683bf38bbcb57f7c08fd81f821716e3011c8; _gid=GA1.2.196121075.1558686339; _tl_csid=65f9676f-8983-4b41-869a-eb92ac5d66fe; _gcl_au=1.1.179289086.1558686349; _tl_auid=5c617a93825e5a00141fc211; _tl_sid=5ce7aaeec1a9f80195f47b54; IR_gbd=stockx.com; _pxhd=18dfb41ace7a1b4b3a2e7191b5a1c5f35dcb0a315a297b9d4b0525f9788bc8c7:e98acc61-6018-11e9-af2b-df2cdcb34bdc; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_multi_edit_seen=true; stockx_bid_ask_spread_seen=true; _gat=1; lastRskxRun=1558687821311; _sp_ses.1a3e=*; is_gdpr=false; cookie_policy_accepted=true; stockx_selected_currency=USD; stockx_selected_locale=en_US; stockx_session=6043khkjw1ujik41558687917748; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1558687825%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSDr5YuX-rUYYXEkcjFVMtQBReavv7Xo00lKcIsaRpPq%26wd%3D%26eqid%3Df3b9377800039495000000065cdb8b3b%22%5D; _pk_ses.421.1a3e=*; IR_9060=1558687827158%7C0%7C1558686351765%7C%7C; IR_PI=333ed49e-7aac-11e9-9fc0-42010a246302%7C1558774227158; product_page_v2=watches%2Chandbags; show_watch_modal=true; show_bid_ask_spread=false; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_below_retail=true; mobile_nav_v2=true; multi_edit_option=decrease; _sp_id.1a3e=025120d0-5815-474d-8427-89fc9e4c58d3.1555399493.48.1558687829.1558512467.b33f40f3-8dde-41fa-b306-93eed5d38bcf; _pk_id.421.1a3e=8dd0763a84c4eaf8.1555399494.24.1558687829.1558687824.; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_n=JTJGc2lnbnVw; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l_h=aHR0cHMlM0ElMkYlMkZzdG9ja3guY29tJTJGc2lnbnVw; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l_t=U3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcw==; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l=JTdCJTIyaHJlZiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGc3RvY2t4LmNvbSUyRnNpZ251cCUyMiUyQyUyMmhhc2glMjIlM0ElMjIlMjIlMkMlMjJzZWFyY2glMjIlM0ElMjIlMjIlMkMlMjJob3N0JTIyJTNBJTIyc3RvY2t4LmNvbSUyMiUyQyUyMnByb3RvY29sJTIyJTNBJTIyaHR0cHMlM0ElMjIlMkMlMjJwYXRobmFtZSUyMiUzQSUyMiUyRnNpZ251cCUyMiUyQyUyMnRpdGxlJTIyJTNBJTIyU3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcyUyMiU3RA==; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_v_d=MjAxOS0wNS0yNFQwOCUzQTUwJTNBMjkuMDUwWg==",
    "referer": "https://stockx.com/buying",
    # "jwt-authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA1LTI0IDA4OjU3OjI5IiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3NTIyNDcxNjA5MTUyMTAxMiIsImV4cCI6MTU1OTI5MzA0OSwiYXBpX2tleXMiOltdfQ.2eHw3mCQ0unwD91tS3P-nM_miWfV_8H_SDjPMc5O5I0"
}

login_url = "https://stockx.com/api/login"

email = "645748712@qq.com"
password = "sl5862798&1102"

data = {
    "email": email,
    "password": password,
}

session = requests.session()
login_response = session.post(url=login_url,data=data,headers=headers)
print("login_response:",login_response.status_code)

for pg in range(1, 2):
    history_url = "https://stockx.com/api/customers/5350379/buying/history?sort=matched_with_date&order=DESC&limit=20&page="+str(pg)+"&currency=USD"

    headers = {
        "cookie":"__cfduid=d3ffda1cc8ad046bc7a33cf6295f850391555399572; cto_lwid=7e5a7a79-17e6-46fd-89c2-a61b574c5821; _ga=GA1.2.1920518057.1555399492; tracker_device=a9f6f14f-58c1-4f7b-952c-e7cf44bef642; _tl_duuid=04c4167e-fe37-4da2-a250-54d2bcbcb250; _pxvid=e98acc61-6018-11e9-af2b-df2cdcb34bdc; ajs_group_id=null; ajs_anonymous_id=%22eef27aca-e027-4ea5-a342-46c4278a56a1%22; rskxRunCookie=0; rCookie=v6rk8y2hqiaiv1sio3na; ajs_user_id=%2280b2a851-2e02-11e9-8db9-12deb909e97c%22; _scid=94d07a5e-6758-4151-9c16-fdeebd9576f9; _fbp=fb.1.1557457428361.36672054; _pk_ref.421.1a3e=%5B%22%22%2C%22%22%2C1558509015%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSDr5YuX-rUYYXEkcjFVMtQBReavv7Xo00lKcIsaRpPq%26wd%3D%26eqid%3Df3b9377800039495000000065cdb8b3b%22%5D; intercom-session-h1d8fvw9=S2dBalpDYzhWZEpQRU9rZGJhNjdaZzl1SzMvWEtQUlo0cFdLL2EyeER1dVlOeldoUTN2Q05Mbm44T1F3dHR5bi0tbWY4blNlbFQwbFB4YmU0YU9TR1Jwdz09--280a683bf38bbcb57f7c08fd81f821716e3011c8; _pk_id.421.1a3e=8dd0763a84c4eaf8.1555399494.23.1558510625.1558496036.; _sp_id.1a3e=025120d0-5815-474d-8427-89fc9e4c58d3.1555399493.47.1558512467.1558496315.5739f8f7-ca34-4100-8b1f-08678cac92f9; _gid=GA1.2.196121075.1558686339; _tl_csid=65f9676f-8983-4b41-869a-eb92ac5d66fe; _gcl_au=1.1.179289086.1558686349; is_gdpr=false; _tl_auid=5c617a93825e5a00141fc211; _tl_sid=5ce7aaeec1a9f80195f47b54; IR_gbd=stockx.com; product_page_v2=watches%2Chandbags; show_watch_modal=true; show_bid_ask_spread=false; show_all_as_number=false; brand_tiles_version=v1; show_bid_education=%20; show_below_retail=true; mobile_nav_v2=true; multi_edit_option=decrease; cookie_policy_accepted=true; _pxhd=18dfb41ace7a1b4b3a2e7191b5a1c5f35dcb0a315a297b9d4b0525f9788bc8c7:e98acc61-6018-11e9-af2b-df2cdcb34bdc; stockx_user_logged_in=true; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA1LTI0IDA4OjI4OjEzIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3NTIwOTk5MDUzMzY1NTY0MiIsImV4cCI6MTU1OTI5MTI5MywiYXBpX2tleXMiOltdfQ.LmlH5TbRq6qrBw2WjEDKHTBu--1h5edr0HK5MU7Jmhc; _tl_uid=80b2a851-2e02-11e9-8db9-12deb909e97c; stockx_selected_currency=USD; stockx_selected_locale=en_US; lastRskxRun=1558686398349; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_n=JTJGYnV5aW5n; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l_h=aHR0cHMlM0ElMkYlMkZzdG9ja3guY29tJTJGYnV5aW5n; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l_t=U3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcw==; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_l=JTdCJTIyaHJlZiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGc3RvY2t4LmNvbSUyRmJ1eWluZyUyMiUyQyUyMmhhc2glMjIlM0ElMjIlMjIlMkMlMjJzZWFyY2glMjIlM0ElMjIlMjIlMkMlMjJob3N0JTIyJTNBJTIyc3RvY2t4LmNvbSUyMiUyQyUyMnByb3RvY29sJTIyJTNBJTIyaHR0cHMlM0ElMjIlMkMlMjJwYXRobmFtZSUyMiUzQSUyMiUyRmJ1eWluZyUyMiUyQyUyMnRpdGxlJTIyJTNBJTIyU3RvY2tYJTNBJTIwQnV5JTIwYW5kJTIwU2VsbCUyMFNuZWFrZXJzJTJDJTIwU3RyZWV0d2VhciUyQyUyMEhhbmRiYWdzJTJDJTIwV2F0Y2hlcyUyMiU3RA==; tl_sopts_65f9676f-8983-4b41-869a-eb92ac5d66fe_p_p_v_d=MjAxOS0wNS0yNFQwOCUzQTI2JTNBMzguMzU2Wg==; IR_9060=1558686351780%7C0%7C1558686351765%7C%7C; IR_PI=333ed49e-7aac-11e9-9fc0-42010a246302%7C1558772751780; stockx_multi_edit_seen=true; stockx_bid_ask_spread_seen=true",
        "jwt-authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdG9ja3guY29tIiwic3ViIjoic3RvY2t4LmNvbSIsImF1ZCI6IndlYiIsImFwcF9uYW1lIjoiSXJvbiIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpc3N1ZWRfYXQiOiIyMDE5LTA1LTI0IDA4OjI4OjEzIiwiY3VzdG9tZXJfaWQiOiI1MzUwMzc5IiwiZW1haWwiOiI2NDU3NDg3MTJAcXEuY29tIiwiY3VzdG9tZXJfdXVpZCI6IjgwYjJhODUxLTJlMDItMTFlOS04ZGI5LTEyZGViOTA5ZTk3YyIsImZpcnN0TmFtZSI6InN1biIsImxhc3ROYW1lIjoibGVpIiwiZ2Rwcl9zdGF0dXMiOiJBQ0NFUFRFRCIsImRlZmF1bHRfY3VycmVuY3kiOiJVU0QiLCJsYW5ndWFnZSI6ImVuLVVTIiwic2hpcF9ieV9kYXRlIjpudWxsLCJ2YWNhdGlvbl9kYXRlIjpudWxsLCJwcm9kdWN0X2NhdGVnb3J5Ijoic3RyZWV0d2VhciIsImlzX2FkbWluIjoiMCIsInNlc3Npb25faWQiOiIxMzA3NTIwOTk5MDUzMzY1NTY0MiIsImV4cCI6MTU1OTI5MTI5MywiYXBpX2tleXMiOltdfQ.LmlH5TbRq6qrBw2WjEDKHTBu--1h5edr0HK5MU7Jmhc",
        "referer": "https://stockx.com/buying",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    }

    history = session.get(url=history_url, headers=headers)
    history_content = history.text
    his_json = json.loads(history_content)

    # 页码方面
    # print(type(his_json['Pagination']))
    # limit = his_json['Pagination']['limit']
    # page = his_json['Pagination']['page']
    # total = his_json['Pagination']['total']
    # lastPage = his_json['Pagination']['lastPage']
    # currentPage = his_json['Pagination']['currentPage']
    # nextPage = his_json['Pagination']['nextPage']
    # prevPage = his_json['Pagination']['prevPage']
    # sort = his_json['Pagination']['sort']
    # order = his_json['Pagination']['order']

    # 内容方面
    print(his_json["PortfolioItems"])

    for i in range(len(his_json['PortfolioItems'])):
        content_dict = his_json['PortfolioItems'][i]

        time_1 = content_dict['matchedWithDate'].replace("+00:00", ".000Z")

        data_1 = datetime.strptime(time_1, '%Y-%m-%dT%H:%M:%S.%fZ')

        purchase_time = data_1 + timedelta(hours=8)

        purchase_time = purchase_time.strftime("%Y-%m-%d")

        print(content_dict['orderNumber'],"\t", content_dict['product']['title'],"\t",

              content_dict['product']['styleId'],"\t",

              content_dict['product']['shoeSize'],"\t", content_dict['localTotal'],"\t", purchase_time,"\t",

              content_dict['Tracking']['number'])
