import requests, csv, markdownify,datetime
from bs4 import BeautifulSoup
# script to fill a csv files with valid html description on club, district etc ... levels

#global vars
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
baseUrl = "	https://reports2.toastmasters.org/ToDo.cgi?dist="
csv_name = "../output/tmi/D98_Area_To_Do.csv"
source_link = baseUrl
#fns
#get data for district page given the int district number
def dist_page(num):
	print("getting the homepage")
	# vals = {'club':'','dist':str(num),'div':'','area':'','mon':'0'}
	# r = requests.get(baseUrl,params=vals)
	actual = baseUrl + str(num)
	r = requests.get(actual, headers=h)
	
	print(r.url)
	if (r.status_code!=200):
		print("error: ",r.status_code)
		return 0
	else:
		print("success: ",r.status_code)
		return r

def add_csv(hd,data,distnum,date):
	tmp_lst=[]
	if (hd.startswith('District')):
		tmp_lst.append('District')
		tmp_lst.append(distnum)
		tmp_lst.append('')
		tmp_lst.append('')
		md_data = markdownify.markdownify(data)
		tmp_lst.append(md_data.strip())
	elif (hd.startswith('Division')):
		tmp_lst.append('Division')
		tmp_lst.append(distnum)
		tmp_lst.append(hd[-1:])
		tmp_lst.append('')
		md_data = markdownify.markdownify(data)
		tmp_lst.append(md_data.strip())
	elif (hd.startswith('Area')):
		tmp_lst.append('Area')
		tmp_lst.append(distnum)
		tmp_lst.append(hd[-2:-1])
		tmp_lst.append(hd[-1:])
		md_data = markdownify.markdownify(data)
		tmp_lst.append(md_data.strip())
	tmp_lst.append(date)
	tmp_lst.append(source_link)
	with open(csv_name,'a', newline='') as op_file:
		writer = csv.writer(op_file)
		writer.writerow(tmp_lst)

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
	with open("../dist-num.txt","r",newline='') as ip_file:
		return ( (ip_file.read()).strip() )


def proc(tmp_str,distnum,date):
	tmp_soup = BeautifulSoup(tmp_str, 'lxml')
	head = tmp_soup.find('h3')
	# tmp_lst.append(head)
	add_csv(head.string.strip(),tmp_str,distnum,date)


#main code 
distnum = get_distnum()
all = dist_page(distnum)
source_link += distnum
date = get_date()

collect = False
tmp_str=""

# write headings to an op file
titles = ['Segment','District','Division','Area','Info','date','link']
with open(csv_name, 'w', newline='') as op_file:
	writer = csv.writer(op_file)
	writer.writerow(titles)

if all != 0: 
	soup = BeautifulSoup(all.text, 'lxml') #getting all the html content
	with open("new.html","w") as f: #writing all the html to a file
		f.write(soup.prettify())

	with open("new.html", "r") as f:
		for line in f:
			if(line.strip()=="<hr/>"):
				collect = True
				# if str is not empy means we have a block of data.
				if (tmp_str):
					#process data here
					# print(tmp_str)
					proc(tmp_str,distnum,date)
				tmp_str=""

			if (collect):
				# print(line)
				tmp_str = tmp_str + line.strip()
				# print(tmp_str)
	