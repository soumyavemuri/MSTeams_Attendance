### REQUIREMENTS ###
- [Python 3.7 or any later version]
- [Pandas]
  - If Pandas isn't already installed, just run the following code after installing Python
    ```bash
    $ pip install pandas
    ```
- ['meetingsAttendanceList']
  - After downloading the list from Microsoft Teams, it should be directly uploaded, no format change required.
  
>Run the file in Console
> ```bash
> $ python main.py
> ```
<br/>

#### IMPORTANT: To test the script, add the full name of the students (exactly how their display names are in Microsoft Teams) under the "Full Name" column in Attendance.csv ####

<br/>

-----


### OTHER GUIDELINES ###
- Please Request the class to join the meeting with their college assigned email IDs or to join with the same display name.
- The code works 100% if the names the participants used to access the meeting matches their name in "Attendance" file.
- The list of students absent can be found in the absentees.txt file in the directory with the date of the meeting in the Reports directory.

- The guest participants entering won't be marked in the Attendance Register. But, the list of all these participants can be found in 'Unidentified_Participants.txt'.
  - The user will need to update manually
- 'Left.txt' file contains names of participants who left in the middle of the meet with the timestamp. 
  - It will be noted only for the first time they leave.
- 'Present_Today.txt' file contains a list of all students (excluding unidentified users) who attended the meeting.
- If the date in the Attendance file appears as ######, expand/increase its width to see the date.

<br/>

##### TO ACCESS THE "CSE-2 Attendance" file please send a request to access it. It hasn't been uploaded to maintain privacy. #####
https://docs.google.com/spreadsheets/d/14xYkrpZ-IqC7VWssLItvTFOMl-BOEI92hOvUm1kP330/edit?usp=sharing
>When downloading, please download in .csv format
