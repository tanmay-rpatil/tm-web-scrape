#scrape reports2.toastmasters.org for Dist 98 stats tables into CSV
import requests,csv
from bs4 import BeautifulSoup
# script to fill CSV files as needed
# modify first table to extract only text contents 
# done - get the next two tables as is tables[2] and tables[3] 
# done - get the next 4 tables as is 4,5,6,7
# remeber to activate venv when developing "source ./env/bin/activate"

#global vars
baseurl = "https://reports2.toastmasters.org/District.cgi?dist=98" # base link for download 
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"} # headers to make the req work
name_list=["","","club_goal","area_goal","disting_div_goals","disting_area_goals","clubs_need_coach","top10_edu_award"]
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

# get req
dist_req = reqeuest_url(baseurl)
# if get req is succesful
if dist_req != 0: 
	# print(all.headers)
	soup = BeautifulSoup(dist_req.text, 'lxml') #getting all the html content
	proc(soup)
