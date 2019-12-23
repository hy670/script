import requests
import time

formdata = {
    "content": "凉山"
}
url = "http://222.180.171.105/portal/search.do"
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
for i in range(0,1000):
    response = requests.post(url, data={"content":str(i)}, headers=headers)
    print(response.text)




