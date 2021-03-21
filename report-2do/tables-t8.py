#scrape reports2.toastmasters.org for 2 tables into CSV
import requests
from bs4 import BeautifulSoup
# script to fill CSV files as needed
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
baseurl = "https://reports2.toastmasters.org/PrezExt20.cgi" # base link for download 
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work

#get req data 
def reqeuest_url(base):
	print("getting the page")
	r = requests.get(base, headers=h)
	print(r.url)
	if (r.status_code!=200):
		print("error: ",r.stataus_code)
		quit()
		return 0
	else:
		print("success: ",r.status_code)
		return r


# process the url to get a param
def proc(tmp_soup):
	table1 = (tmp_soup.find_all("table"))[1]
	table2 = (tmp_soup.find_all("table"))[2]
	with open("tables-t8-table1.html","w") as f:
		print(table1)
		f.write(table1.prettify())

# main code 


# get req
dist_req = reqeuest_url(baseurl)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup)
