import datetime

writeflag=0
start_string="\"DCP Goals: This month in past years\""
stop_sring="\"Educational awards this year\""
blank_string="\" \""

input_file = open('title.csv', 'r')
output_file = open('output.csv','w')

# get today's date
date  = datetime.datetime.now()
d = date.strftime("%d")+"-"
d += date.strftime("%m")+"-"
d += date.strftime("%y")
print(d)

for each in input_file:
    # Python code to create a file
     output_file.write(each)
input_file.close()

input_file = open('DCP_History_report_for_Club_1.csv', 'r')
for each in input_file:
    # Python code to create a file
    #print(each)
    #print(start_string)
    bool = (each.strip() == start_string.strip())
    if (bool):
        writeflag=1
        print(each)
        print("found")
    elif (each.strip()==stop_sring.strip()):
        writeflag=0
    elif (each.strip() == blank_string.strip()):
        print("blank line")
    elif (writeflag==1):      
        each=each.strip()+("," + str(d) + "," + "marshall\n") 
        output_file.write(each)
        print("wrting output")
    #else:
    #    print ("no write")
print(start_string)
print(stop_sring)

output_file.close()
input_file.close()


