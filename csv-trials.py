import csv
#trying different csv things


count = 0
t=[]
db=[]
with open("sv.dat", "r") as f:
	reader = csv.reader(f)
	for row in reader:
		if(count>0):
			if(row[1]!=''):
				if (row[0] not in t):
					t.append(float(row[0]))
					db.append(float(row[1]))
		count ++

with open("new.dat",'w') as f:
	for i in range(len(t)):