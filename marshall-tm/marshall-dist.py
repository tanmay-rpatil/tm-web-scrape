import requests, csv
from bs4 import BeautifulSoup

# headers, required link
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
link = "https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&mon=0"

r = requests.get(link, headers=h)

if	r.status_code != 200:
	print(str(r.status_code)+" error, exiting programme")
	exit()
else:
	print("parsing")

soup1 = BeautifulSoup(r.text,'lxml')


# print(r.headers)
# print(r)
with open('dist-98.csv', 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode
	f.write(r.content)
	# print(r)