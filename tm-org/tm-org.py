#scrape tm.org for 3 csvs mentioned in links
import requests, csv
from bs4 import BeautifulSoup
# script to fill download CSV files as needed
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work
baseurl = "http://dashboards.toastmasters.org/Division.aspx?id=" # web page to get params for downlaod
downurl = "http://dashboards.toastmasters.org/export.aspx?type=CSV&report=" # base link for download 
distnum = 98

#get data for district page given the int district number
def reqeuest_url(base,param):
	print("getting the page")
	# vals = {'club':'','dist':str(num),'div':'','area':'','mon':'0'}
	# r = requests.get(baseurl,params=vals)
	actual = base + str(param)
	r = requests.get(actual, headers=h)
	
	print(r.url)
	if (r.status_code!=200):
		print("error: ",r.status_code)
		quit()
		return 0
	else:
		print("success: ",r.status_code)
		return r

def download_csv(req):
	csv_file = open('downloaded.csv', 'wb')
	csv_file.write(req.content)
	csv_file.close()

# process the url to get a param
def proc(tmp_soup):
	tag = tmp_soup.find(id='cpContent_TopControls1_ddlExport')
	attr = tag.get('onchange')
	# print(attr)
	startindex = int(attr.find("'"))
	startindex+=1
	print(startindex)
	if (startindex!=-1):
		# print('found')	
		endindex = int(attr.find("'",startindex))
		if (endindex!=-1):
			req = attr[startindex:endindex]
			print(req)
			down_req = reqeuest_url(downurl,req)
			if (reqeuest_url!=0):
				print('trying download')
				download_csv(down_req)


		else:
			print('err tag conetents maybe wrong')
	else:
		print('err tag conetents maybe wrong')	

# main code 
# get req
all = reqeuest_url(baseurl,distnum)

# if get req is succesful
if all != 0: 
	# print(all.headers)
	soup = BeautifulSoup(all.text, 'lxml') #getting all the html content
	# look for the csv export tag
	# id = "cpContent_TopControls1_ddlExport"
	proc(soup)
	