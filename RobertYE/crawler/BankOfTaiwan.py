import requests

url = "http://rate.bot.com.tw/xrt"

querystring = {"Lang":"zh-TW"}

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/64.0.3282.186 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://www.google.com.tw/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5",
    'cache-control': "no-cache",
    'postman-token': "8f921ae3-3009-857d-77f6-ed2a4514b602"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)