import requests
import urllib3
urllib3.disable_warnings()
du_url = "https://m.poizon.com/menu/shopping?lastId=&limit=20&loginToken=d4300856%7C97955%7C9638895b480d6c48&mode=0&newSign=40bff5b1a74779c947f61bf6b78d165c&platform=iPhone&sign=cf13af0f8e2da3237480d4c45c5a71f3&signNo=&tabId=0&timestamp=1559110593383&token=JLIjsdLjfsdII%253D%257CMTQxODg3MDczNA%253D%253D%257C07aaal32795abdeff41cc9633329932195&uuid=B439DA6B-3DAE-4882-A982-357AEC7003F1&v=4.1.0"

headers = {
    "lastId":"",
    "limit":"20",
    "loginToken":"d4300856|97955|9638895b480d6c48",
    "mode":"0",
    "newSign":"40bff5b1a74779c947f61bf6b78d165c",
    "platform":"iPhone",
    "sign":"cf13af0f8e2da3237480d4c45c5a71f3",
    "signNo":"",
    "tabId":"0",
    "timestamp":"1559110593383",
    "token":"JLIjsdLjfsdII%3D%7CMTQxODg3MDczNA%3D%3D%7C07aaal32795abdeff41cc9633329932195",
    "uuid":"B439DA6B-3DAE-4882-A982-357AEC7003F1",
    "v":"4.1.0",
    "user-agent":"https://m.poizon.com/menu/shopping?lastId=&limit=20&loginToken=d4300856%7C97955%7C9638895b480d6c48&mode=0&newSign=89735cdb7093ae4606ade82742bbcd4a&platform=iPhone&sign=78e429c56cb2835673a852bc18287a3c&signNo=&tabId=0&timestamp=1559115531735&token=JLIjsdLjfsdII%253D%257CMTQxODg3MDczNA%253D%253D%257C07aaal32795abdeff41cc9633329932195&uuid=B439DA6B-3DAE-4882-A982-357AEC7003F1&v=4.1.0",
    "cookie":"CNZZDATA1272882183=695475915-1547168187-%7C1559094995; duToken=12943269%7C97955%7C1559022847%7C1d35b0ae6bbe3573; FSSBBIl1UgzbN7N80T=3PMHeuGTYJDDtcAeAVHuxXQkdVNzZbnm66v2dy5l62UsQhdJbyAOIt3HP33o5i.vpqhEf5_2mM6wHJgqluykIL9ZkImIiispzWhbY.89haS_D5Aqi4kwk0YsMn_RM0X75Gg5ivwjdxLxz6.Z2bd6fKipx2DVxh0fhFCb2qtS0rX3oP5XY5kn47RLkqRYRiQQZBmZeRexr0zcEnekRWOxUjEPCO.3yDpYWyVwUwiou0p7X7atmp7QnNDCyk3OG5yiy8GTE60YVwhRvF4JMt1cqK5YLDY6XRb5WPBf5vqNx.lVpEP_GeDZk0eUhD8Ziaczh4lVKYYoSFIxy0ZEd1Qea.Daq; FSSBBIl1UgzbN7N80S=Ylcluc2O9GYcU2wjVuHsjjBRXax0W8EL.nCyDEmcib.Bdgswb3yvJ7ZJfxc0AUOy; UM_distinctid=1683a75a3ef79-0c2ee0f94e68078-1b79162d-4a574-1683a75a3f03f9",
}

response = requests.get(url=du_url,headers=headers,verify=False)