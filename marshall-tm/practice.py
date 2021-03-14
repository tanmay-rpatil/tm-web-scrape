import requests
from bs4 import BeautifulSoup

h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
# baseUrl = "https://www.marshalls.org/tmtools/DCP_Hist.cgi"
baseUrl = "https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&mon=0"

#get data for district page given the int district number
def dist_page(num):
	print("getting the homepage")
	vals = {'club':'','dist':str(num),'div':'','area':'','mon':'0'}
	# r = requests.get(baseUrl,params=vals)
	r = requests.get(baseUrl, headers=h)
	
	print(r.url)
	if (r.status_code!=200):
		print("error: ",r.status_code)
	else:
		print("success: ",r.status_code)

dist_page(98)