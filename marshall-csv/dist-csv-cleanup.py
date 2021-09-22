csv_name = 'DCP_History_report_for_Dist.csv'
output_file = open(csv_name[:-4]+'_output.csv','w')
# output_file = open('dist_output.csv','w')

input_file = open(csv_name, 'r')
for row in input_file:
    check = row.strip()
    bool = ( (check=="") or (check.startswith("\"Sum")) or (check.startswith("\"<a")) )
    if (bool):
        print("line to skip")
    else:
        print("writing line")
        output_file.write(row)

output_file.close()
input_file.close()


