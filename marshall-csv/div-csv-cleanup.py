import csv,datetime

output_file = open('div_output.csv','w')
write = True
div=''
headings = ["Month","Clubs","Goals <4","Goals 5-6","Goals 7-8","Goals 9-10","Members 20+","Members +5","Member Base","Member T/Date","CCs","ACs","Ldrs","CCs/Mem","ACs/Mem","Ldrs/Mem","Pos. Dist. clubs","div","date_updated","source"]

# get today's date
date  = datetime.datetime.now()
d = date.strftime("%d")+"-"
d += date.strftime("%m")+"-"
d += date.strftime("%y")
print(d)

with open('DCP_History_report_for_Div.csv', newline='') as i_file:
	ip_reader = csv.reader(i_file)
	output_writer = csv.writer(output_file)
	output_writer.writerow(headings) #write the headings
	for row in ip_reader:
		# print(row)
		# check = row[0].strip()
		if(not row): #empty
			continue;
		else:
			check = row[0].strip()
			# print(check)
			if(check=="Summary for District 98"):
				# print(check)
				write=False
			elif (check.startswith("<a")): #ignore the hyperlink 
				continue;
			elif( check.startswith("Summary for District 98, Division") ):
				write=True
				div=check[-1]
				# print("new div")
			elif(write and (div!='')):
				row.append(div)
				row.append(d)
				row.append("marshall")
				output_writer.writerow(row)
				print("div = " + div)       