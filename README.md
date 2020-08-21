## TO ACCESS THE "V-SEM CSE-2 Attendance" file please send a request to access it. It hasn't been uploaded for privacy ##
-https://docs.google.com/spreadsheets/d/14xYkrpZ-IqC7VWssLItvTFOMl-BOEI92hOvUm1kP330/edit?usp=sharing
>When downloading, please download in .csv format

>Just clicking attendance.py file will run it. It can also be run from command prompt
```bash
$ python attendance.py
```
## REQUIREMENTS ## 
-[Python 3.7 or any later version]
-[Pandas]
  -If Pandas isn't already installed, just run the folloeing code after installing Python
  ```bash
  $ pip install 
  ```
- ['meetingsAttendanceList' and the class attendance list must be in CSV Format
  - After downloading the list from Microsoft Teams, please open the'meetingsAttendanceList' file and save as CSV. Otherwise, the code will not work.


## OTHER GUIDELINES ##
>Please Request the class to join the meeting with their college assigned email IDs or to join with the same display name.
>The code works 100% if the names the participants used to access the meeting matches their name in "V-SEM CSE-2 Attendance" file.
>I have matched the names of all CSE2 students to their display names given by the college admin, i.e., ugsXXXXX_cse.XXXXX@cbit.org.in in the spreadsheet
>The guest participants entering will be marked ABSENT in the Attendance Register. But, the list of all these participants can be found in 'Unidentified Participants.txt'.
 The user will need to update manually
>'Left.txt' file contains names of participants who left in the middle of the meet with the timestamp. 
  -(It will be noted only for the first time they leave. If you want duplicates as well, refer to the code and read the comments)
>'Present.txt' file contains a list of all students (excluding unidentified users) Present today
>'Unidentified Participants', 'Left' and 'Present' are erased and updated everytime attendance.py is run
>If the date in the C2 file appears as ######, expand/increase its width to see the date
