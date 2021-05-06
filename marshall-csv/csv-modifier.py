import glob,csv,datetime

def get_date():
	date  = datetime.datetime.now()
	d = ""
	d += date.strftime("%Y") + "-" #get year in yyyy format
	d += date.strftime("%m") + "-" #get month in 0 padded format e.g. 02,03,10,11,12
	d += date.strftime("%d") #get date in 0 padded format e.g. 02,03,10,11,12
	d = '2021-04-22' #hardcoding for testing purposes
	print(d) #for debugging
	return d

def add_date_source(date,map_src):
	lst = glob.glob("*.csv")
	for fname in lst:
		if( not (fname in map_src.keys())):
			continue #if unrequired file.
		tmpFile = fname[:-4]+"_output_final.csv"
		with open(fname, "r") as file, open(tmpFile, "w") as outFile:
			reader = csv.reader(file, delimiter=',')
			writer = csv.writer(outFile, delimiter=',')
			header = next(reader)
			header.append("date")
			header.append("source")
			writer.writerow(header)
			source = map_src[fname]
			
			for row in reader:
				row.append(date)
				row.append(source)
				writer.writerow(row)
map_src = { "area_output.csv":"https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&areaview=on&mon=0","club_output.csv":"https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&clubview=on&mon=0","dist_output.csv":"https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&mon=0","getclubs-D98.csv":"https://www.marshalls.org/tmtools/getclubs.cgi?dist=98&Go=getclubs","div_output.csv":"https://www.marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&divview=on&mon=0",}


add_date_source(get_date(),map_src)