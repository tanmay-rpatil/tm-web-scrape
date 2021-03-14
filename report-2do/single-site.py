import requests, csv
from bs4 import BeautifulSoup
# script to fill a csv files with valid html description on club, district etc ... levels

#global vars
h = {'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}
baseUrl = "	https://reports2.toastmasters.org/ToDo.cgi?dist="
distnum = 98

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

def add_csv(hd,data):
	tmp_lst=[]
	if (hd.startswith('District')):
		tmp_lst.append('District')
		tmp_lst.append(distnum)
		tmp_lst.append('')
		tmp_lst.append('')
		tmp_lst.append(data.strip())
	elif (hd.startswith('Division')):
		tmp_lst.append('Division')
		tmp_lst.append(distnum)
		tmp_lst.append(hd[-1:])
		tmp_lst.append('')
		tmp_lst.append(data.strip())
	elif (hd.startswith('Area')):
		tmp_lst.append('Area')
		tmp_lst.append(distnum)
		tmp_lst.append(hd[-2:-1])
		tmp_lst.append(hd[-1:])
		tmp_lst.append(data.strip())
	with open('output.csv','a') as op_file:
		writer = csv.writer(op_file)
		writer.writerow(tmp_lst)
		
def proc(tmp_str):
	tmp_soup = BeautifulSoup(tmp_str, 'lxml')
	head = tmp_soup.find('h3')
	# tmp_lst.append(head)
	add_csv(head.string.strip(),tmp_str)


#main code 
all = dist_page(distnum)

collect = False
tmp_str=""

# write headings to an op file
titles = ['Segment','District','Division','Area','Info']
with open('output.csv', 'w') as op_file:
	writer = csv.writer(op_file)
	writer.writerow(titles)

if all != 0: 
	# print ("hi")
	# print(all.text)
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
					proc(tmp_str)
				tmp_str=""

			if (collect):
				# print(line)
				tmp_str = tmp_str + line.strip()
				# print(tmp_str)
	