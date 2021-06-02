# Web Scraping Tools for ToastMasters Websites

## To run in one go (Bash shell script)

```bash
#give permission to execute the run.sh script
chmod +x ./run.sh

#execute it 
./run.sh

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

- [ ] Marshall rename CSV

- [ x ] make entire program single click

- [ ] make marshall download automated

- [ ] correct table with two heading rows 

- [ ] Fix issue with dates