import requests
from bs4 import BeautifulSoup
# script to ownload HTML files as needed
# just for testing. Can be used to download any page as an HTML document
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


# process the url to get the html text. write it to a file
def proc(tmp_soup):
	with open("tables-t8.html","w") as f:
		print("writing to file")
		f.write(tmp_soup.prettify())
# main code 

# get req
dist_req = reqeuest_url(baseurl)
# if get req is succesful
if dist_req != 0: 
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup)
