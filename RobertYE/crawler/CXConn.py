import requests

url="http://www.cathaypacificcargo.com/ManageYourShipment/CheckFlightAvailability/tabid/114/orig/TPE/dest/HKG/date/" \
    "01Apr18/type/A/clientdate/2018-03-07/language/en-US/Default.aspx"

headers={
    'upgrade-inservure-requests':"1",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100"
                 " Safari/537.36",
    'referer':"http://www.cathaypacificcargo.com/",
    'accept-encoding':"gzip, defate",
    'accept-language':"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2,zh-CN;q=0.2",
    'cache-control':"no-cache"
}

response=requests.request("POST", url, headers=headers)

print(response.text)