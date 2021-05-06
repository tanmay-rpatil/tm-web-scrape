#scrape reports2.toastmasters.org for 2 tables into CSV
import requests,csv,datetime
from bs4 import BeautifulSoup
# script to fill CSV files as needed
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
baseurl = "https://reports2.toastmasters.org/PrezExt20.cgi" # base link for download 
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work
source_link = "https://reports2.toastmasters.org/PrezExt20.cgi"

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
	d = '2021-04-22' #hardcoding for testing purposes
	print(d) #for debugging
	return d

# save the html table into a csv file
def table_to_csv(table_soup, fname, date):
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
		i = 0
		for row in list_of_rows:
			if (row[1]=="98"):
				with open("global_district_ranks.txt","a") as op_file2:
					if (fname.startswith("20")):
						op_file2.write("rank= "+row[0] +" precent= "+row[2]+"\n")
						print(("rank= "+row[0] +" precent= "+row[2]+"\n"))
					else:
						op_file2.write("rank= "+row[0] +" growth= "+row[2]+"\n")
						print(("rank= "+row[0] +" growth= "+row[2]+"\n"))
			if (i!=0):
				row.append(date)
				row.append(source_link)
			else:
				row.append("date")
				row.append("link")
			writer.writerow(row)
			i+=1
# process the url to get a param
def proc(tmp_soup,date):
	table1 = (tmp_soup.find_all("table"))[1]
	table2 = (tmp_soup.find_all("table"))[2]
	table_to_csv(table1,"20_plus_members_ranking",date)
	table_to_csv(table2,"club_growth_ranking",date)


# main code 
# get today's date
d = get_date()
# get req
dist_req = reqeuest_url(baseurl)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup,d)
