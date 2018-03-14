import requests

url = "https://www.gamer.com.tw/index.php"

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/64.0.3282.186 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5",
    'cache-control': "no-cache",
    'postman-token': "338cc0b8-6745-981e-65fc-030cec6fac21"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)