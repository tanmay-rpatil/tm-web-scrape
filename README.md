# Web Scraping Tools for ToastMasters Websites

## To run in one go (Bash shell script)

### Note 
- First install Python3
- These are instructions for bash shell
- These will generate all the CSVs except for the marshall sources

```bash
# install required libraries from the requirements.txt file
pip install -r requirements.txt

# clone this dir
git clone https://github.com/tanmay-rpatil/tm-web-scrape.git

# cd into the repo
cd ./tm-web-scrape
#give permission to execute the run.sh script
chmod +x ./run.sh

#execute it 
./run.sh
```

### Marshalls

Download each of the following CSVs into marshalls-csv folder
- https://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&mon=0 as DCP_History_report_for_Dist.csv
- https://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&clubview=on&mon=0 DCP_History_report_for_Club.csv
- http://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&divview=on&mon=0 as DCP_History_report_for_Div.csv
- http://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&areaview=on&mon=0 as DCP_History_report_for_Area.csv

```bash
# run all the pyhton scripts from marshalls-csv fodler
# cd into marhsall-csv folder
python3 ./area-csv-cleanup.py
python3 ./club-csv-cleanup.py
python3 ./dist-csv-cleanup.py
python3 ./div-csv-cleanup.py
python3 ./csv-modifier.py

# will get (csv-name)_output_final.csv for each of the files.
```


## Task List and Current Progress

| #   | Name,Link                                                                         | Task                           | CSV-names                                                                                                                             | Notes                               | Status                   |
|:---:|:---------------------------------------------------------------------------------:|:------------------------------:| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |:------------------------:|
| 1   |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
| 2   |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
| 3   |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
| 4   | [tmi/tm-org.py](https://dashboards.toastmasters.org/District.aspx?id=98)          | download the Div & club csv    | Division_performace, Club_performace                                                                                                  |                                     | <ul><li>- [x] </li></ul> |
| 5   | [tmi/tm-org.py ](https://dashboards.toastmasters.org/Division.aspx?id=98)         | download the Dist csv          | District_performace                                                                                                                   |                                     | <ul><li>- [x] </li></ul> |
| 6   | [report-2do/tables-t6](https://reports2.toastmasters.org/ToDo.cgi?dist=98)        | csv with raw html              | D98_Area_To_Do                                                                                                                        |                                     | <ul><li>- [x] </li></ul> |
| 7   | [report-2do/tables-t7](https://reports2.toastmasters.org/D98/D98-2021-01-16.html) | convert all tables to csvs     |                                                                                                                                       | Dynamic Page, based on date - TODO! | <ul><li>- [ ] </li></ul> |
| 8   | [report-2do/tables-t8](https://reports2.toastmasters.org/PrezExt20.cgi)           | convert 2 tables to CSVs       |                                                                                                                                       |                                     | <ul><li>- [x] </li></ul> |
| 9   | [report-2do/tables-t9](https://reports2.toastmasters.org/District.cgi?dist=98)    | convert all the tables to csvs | District_goal_birds_eye,Club_goal,Area_goal, Distinguished_Division_goals, Distinguished_Area_goals,Clubs_need_coach, Top10_Edu_Award |                                     | <ul><li>- [x] </li></ul> |
| 10  |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
| 11  |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
| 12  |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |
|     |                                                                                   |                                |                                                                                                                                       |                                     | <ul><li>- [ ] </li></ul> |



## To Do list

- [X] Marshall rename CSV

- [x] make entire program single click

- [] make marshall download automated

- [X] correct table with two heading rows 

- [X] Fix issue with dates