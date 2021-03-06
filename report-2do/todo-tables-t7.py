#scrape reports2.toastmasters.org for Dist 98 stats tables into CSV
# give the argument for today
import requests,csv,datetime
from bs4 import BeautifulSoup
# script to fill CSV files as needed
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
baseurl = "https://reports2.toastmasters.org/D98/D98-" # base link add date in the format = " yyyy-mm-dd.html"
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work

# get value of district from "district-selection.txt"

#get req data 
def reqeuest_url(base):
	print("getting the page")
	r = requests.get(base, headers=h)
	print(r.url)
	if (r.status_code==404):
		print("error: ",r.status_code)
		# quit()
		return(404)
	elif (r.status_code!=200):
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
	d = '2021-04-22' #hardcoding for testing purposes
	return d

# save the html table into a csv file
def table_to_csv(table_soup, fname):
	fname = fname + ".csv"
	list_of_rows = []
	for row in table_soup.findAll("tr"):
		list_of_cells = []
		for cell in row.findAll(["th","td"]):
			text = cell.text
			list_of_cells.append(text.strip())
		list_of_rows.append(list_of_cells)
	with open(fname,"w") as op_file:
		writer = csv.writer(op_file)
		for row in list_of_rows:
			writer.writerow(row)

# process the url to get a param
def proc(tmp_soup):
	tables = tmp_soup.find_all("table")
	
	for i in range(len(tables)):
		if(i>1):
			table_to_csv(tables[i],name_list[i])


# main code 
d = get_date() #get today's date in the required format
d+=".html"
# get req
req_url=baseurl+d
dist_req = reqeuest_url(req_url)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup)
