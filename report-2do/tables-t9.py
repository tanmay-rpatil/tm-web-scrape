#scrape reports2.toastmasters.org for Dist 98 stats tables into CSV
import requests,csv,datetime
from bs4 import BeautifulSoup
# script to fill CSV files as needed
# modify first table to extract only text contents 
# done - get the next two tables as is tables[2] and tables[3] 
# done - get the next 4 tables as is 4,5,6,7
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
baseurl = "https://reports2.toastmasters.org/District.cgi?dist=" # base link for download at the end add distnum 
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work
name_list=["","","Club_goal","Area_goal","Distinguished_Division_goals","Distinguished_Area_goals","Clubs_need_coach","Top10_Edu_Award"]
source_link= "https://reports2.toastmasters.org/District.cgi?dist=98"
# the above list is the filename list

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

# save the html table into a csv file
def table_to_csv(table_soup, fname,date):
	fname = "../output/tmi/"+fname + ".csv"
	list_of_rows = []
	for row in table_soup.findAll("tr"):
		list_of_cells = []
		for cell in row.findAll(["th","td"]):
			text = cell.text
			list_of_cells.append(text.strip())
		list_of_rows.append(list_of_cells)
	with open(fname,"w") as op_file:
		writer = csv.writer(op_file)
		i=0
		for row in list_of_rows:
			if (i!=0):
				row.append(date)
				row.append(source_link)
			else:
				row.append("date")
				row.append("link")
			writer.writerow(row)
			i+=1
	
# process the url to get tables, and send to another function to generate files
def proc(tmp_soup,date):
	tables = tmp_soup.find_all("table")
	for i in range(len(tables)):
		if(i>1):
			table_to_csv(tables[i],name_list[i],date)
		if(i==0): #the special case to deal with
			print("filler")
			table_soup=tables[i]
			list_of_rows = []
			for row in table_soup.findAll("tr"):
				list_of_cells = []
				for cell in row.findAll(["th","td"]):
					text = (cell.text).strip()
					if(not text):
						continue
					else:
						list_of_cells.append(text)
				list_of_rows.append(list_of_cells)
			# this is the one table that has a differnt format, so dealt with it differently 
			with open("../output/tmi/District_goal_birds_eye.csv","w") as op_file:
				writer = csv.writer(op_file)
				i=0
				for row in list_of_rows:
					if (i!=0):
						row.append(date)
						row.append(source_link)
					else:
						row.append("date")
						row.append("link")
					writer.writerow(row)
					i+=1

# main code 
#get distnum from file
distnum = get_distnum()
print(distnum)
# get date
d = get_date()
# get req
dist_req = reqeuest_url(baseurl+distnum)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup,d)
