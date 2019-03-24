import requests
from bs4 import BeautifulSoup
import base64

url = "http://www.jthjrb.com/portal/zh_CN/home/search/index.html"
parse ={'content':'<script>alert(1)</script>'}
r = requests.session()
resp = r.get(url,params=parse)
resp.encoding = "utf8"
headers = resp.headers
text = resp.text
soup =BeautifulSoup(text,'lxml')
print(text)
if '<script>alert(1)</script>' in text:
	print("XSS 存在")
else:
	print("XSS 不存在")


