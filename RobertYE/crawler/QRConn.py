import requests

url = "http://www.qrcargo.com/enquireFlightSchedules"

payload = "{\"origin\":\"KGL\",\"destination\":\"DOH\",\"effectiveFromStr\":\"01-Apr-2018\"," \
          "\"listofOperationTypesStr\":\"PAX,FRT,TRK\"}"
headers = {
    'accept': "*/*",
    'origin': "http://www.qrcargo.com",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/64.0.3282.186 Safari/537.36",
    'content-type': "application/json",
    'referer': "http://www.qrcargo.com/flightschedules?origin=TPE&destination=LXR&effectiveFromStr=02-Mar-2018",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5",
    'cookie': "__utmz=76335189.1517211795.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); "
              "BIGipServerqrcargo-webportal-pool=1244994476.20480.0000; __utmc=76335189;"
              " __utma=76335189.337953971.1513755964.1519976243.1520216193.7;"
              " __utmz=76335189.1517211795.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided);"
              " __utmc=76335189; __utma=76335189.337953971.1513755964.1519976243.1520216193.7; __utmt=1;"
              " __utmb=76335189.3.10.1520216193",
    'cache-control': "no-cache",
    'postman-token': "23e58124-1bac-78cf-afd4-f6d9db05f503"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)