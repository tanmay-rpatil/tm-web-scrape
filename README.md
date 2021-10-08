# Web Scraping Tools for ToastMasters Websites

## To run in one go (Bash or Bat fille)

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
# cd into marhsall-csv folder
./run-m.sh # run-m.bat for windows

```

## Task List and Current Progress

| #   | CSV-names                        | Name                                                    | Link                                                                                  | Task                             | Notes                                                                     |
|:---:| -------------------------------- |:-------------------------------------------------------:| ------------------------------------------------------------------------------------- |:--------------------------------:| ------------------------------------------------------------------------- |
| 1   | DCP_History_report_for_Dist.csv  | marhsall/dist-csv-cleanup.py   marhsall/csv-modifier.py | https://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&mon=0             | Clean csv, add date, link        | DCP , Club size, membership size  For  District                           |
| 2   | DCP_History_report_for_Div.csv   | marhsall/div-csv-cleanup.py   marhsall/csv-modifier.py  | http://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&divview=on&mon=0   | Clean csv, add date, link        | DCP , Club size, membership size  For    Division                         |
| 3   | DCP_History_report_for_Area.csv  | marhsall/area-csv-cleanup.py   marhsall/csv-modifier.py | http://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&areaview=on&mon=0  | Clean csv, add date, link        | DCP , Club size, membership size  For  District Division Area             |
| 4   | DCP_History_report_for_Club.csv  | marhsall/club-csv-cleanup.py   marhsall/csv-modifier.py | https://marshalls.org/tmtools/DCP_Hist.cgi?club=&dist=98&div=&area=&clubview=on&mon=0 | Clean csv, add date, link        | DCP etc at club level                                                     |
| 5   | getclubs-details-D98.csv         | marhsall/csv-modifier.py                                | https://www.marshalls.org/tmtools/getclubs.cgi?dist=98&Go=getclubs                    | Clean csv, add date, link        | club details , “find a club” like information                             |
| 6   | District_Performance.csv         | tmi/tm-org.py                                           | http://dashboards.toastmasters.org/District.aspx?id=98                                | Download csv,add date,link       | TI dashboard for district performance                                     |
| 7   | Division_Performance.csv         | tmi/tm-org.py                                           | http://dashboards.toastmasters.org/Division.aspx?id=98                                | Download csv,add date,link       | TI dashboard for Division and Area performance                            |
| 8   | Club_Performance.csv             | tmi/tm-org.py                                           | http://dashboards.toastmasters.org/Club.aspx?id=98                                    | Download csv,add date,link       | TI dashboard for Club performance                                         |
| 9   | D98_Area_To_Do.csv               | report-2do/tables-t6                                    | https://reports2.toastmasters.org/ToDo.cgi?dist=98                                    | Create csv with a mardown column | Distinguished Goals Needed for District 98 -- "To Do"                     |
| 10  | club_growth_ranking.csv          | report-2do/tables-t8                                    | https://reports2.toastmasters.org/PrezExt20.cgi                                       | Convert table to CSVs            | Districts with highest net club growth – Global Ranking                   |
| 11  | 20_plus_members_ranking.csv      | report-2do/tables-t8                                    | https://reports2.toastmasters.org/PrezExt20.cgi                                       | Convert table to CSVs            | Districts with highest percent of clubs with 20+ members – Global Ranking |
| 12  | District_goal_birds_eye.csv      | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary -  Global Ranking                                        |
| 13  | Club_goal.csv                    | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary -  for Clubs                                             |
| 14  | Area_goal.csv                    | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary -  for Areas                                             |
| 15  | Distinguished_Division_goals.csv | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary – Distinguished Division Goals                           |
| 16  | Distinguished_Area_goals.csv     | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary – Distinguished Area Goals                               |
| 17  | Clubs_need_coach.csv             | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary – Clubs that need coaches                                |
| 18  | Top10_Edu_Award.csv              | report-2do/tables-t9                                    | https://reports2.toastmasters.org/District.cgi?dist=98                                | Convert table to CSVs            | District summary –Top 10 clubs                                            |