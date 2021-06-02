#scrape tm.org for 3 csvs mentioned in links
import requests,datetime,glob,csv
from bs4 import BeautifulSoup
# script to fill download CSV files as needed
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
distnum = 0 #default value. will be updated later
downurl = "http://dashboards.toastmasters.org/export.aspx?type=CSV&report=" # base link for download 
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work
source_link = "http://dashboards.toastmasters.org/District.aspx?id=98"
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

#get the current date in the format "yyyy-mm-dd" 
def get_date():
	date  = datetime.datetime.now()
	d = ""
	d += date.strftime("%Y") + "-" #get year in yyyy format
	d += date.strftime("%m") + "-" #get month in 0 padded format e.g. 02,03,10,11,12
	d += date.strftime("%d") #get date in 0 padded format e.g. 02,03,10,11,12
	# d = '2021-04-22' #hardcoding for testing purposes
	print(d) #for debugging
	return d

#get the district number
def get_distnum():
	with open("../dist-num.txt","r") as ip_file:
		return ( (ip_file.read()).strip() )

def download_csv(req, category):
	name = str(category)+ '.csv'
	csv_file = open(name, 'wb')
	csv_file.write(req.content)
	csv_file.close()

# process the url to get a param
def proc(tmp_soup, down_url, category):
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
			down_req = reqeuest_url(down_url,req)
			if (reqeuest_url!=0):
				print('trying download')
				download_csv(down_req, category)
		else:
			print('err tag conetents maybe wrong')
	else:
		print('err tag conetents maybe wrong')	

def add_date_source(date,source):
	lst = glob.glob("*.csv")
	for fname in lst:
		tmpFile = '../output/'+ fname[:-4]+"_performance.csv"
		with open(fname, "r") as file, open(tmpFile, "w") as outFile:
			reader = csv.reader(file, delimiter=',')
			writer = csv.writer(outFile, delimiter=',')
			header = next(reader)
			header.append("date")
			header.append("link")
			writer.writerow(header)
			for row in reader:
				row.append(date)
				row.append(source)
				writer.writerow(row)


# main code 
distnum = get_distnum()
baseurl = "http://dashboards.toastmasters.org/District.aspx?id=" # web page to get params for downlaod
# get req

dist_req = reqeuest_url(baseurl,distnum)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	# look for the csv export tag
	# id = "cpContent_TopControls1_ddlExport"
	proc(soup, downurl, "District")
	
# same with division now
baseurl = "http://dashboards.toastmasters.org/Division.aspx?id=" # web page to get params for downlaod
dist_req = reqeuest_url(baseurl,distnum)
if dist_req != 0: 
	soup = BeautifulSoup(dist_req.text, 'lxml')
	proc(soup, downurl, "Division")

# same with club
baseurl = "http://dashboards.toastmasters.org/Club.aspx?id=" # web page to get params for downlaod
dist_req = reqeuest_url(baseurl,distnum)
if dist_req != 0: 
	soup = BeautifulSoup(dist_req.text, 'lxml')
	proc(soup, downurl, "Club")

#add date and source to files.
add_date_source(get_date(),source_link)
