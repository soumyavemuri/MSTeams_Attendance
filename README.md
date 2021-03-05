### REQUIREMENTS ###
- [Python 3.7 or any later version]
- [Pandas]
  - If Pandas isn't already installed, just run the following command after installing Python
    ```bash
    $ pip install pandas
    ```
- ['meetingsAttendanceList']
  - After downloading the list from Microsoft Teams, it should be directly uploaded, no format change required.
  
>Run the below command in the Console or just click on main.py
> ```bash
> $ python main.py
> ```
<br/>

#### IMPORTANT: To test the script, add the full name of the students (exactly how their display names are in Microsoft Teams) under the "Full Name" column in Attendance.csv ####

<br/>

-----


### OTHER GUIDELINES ###
- Please Request the class to join the meeting with their college assigned email IDs or to join with the same display name.
- The code is 100% efficient if the names the attendees join with matches their name in "Attendance.csv" file.
- The list of students absent can be found in the Reports directory as 'absentees.txt'.

- The guest participants attending the meeting won't be marked in the Attendance Register. But, the list of all these participants can be found in 'Unidentified_Participants.txt'.
  - The user will need to update their attendance manually
- 'Left.txt' file contains names of attendees who left in the middle of the meeting along with the timestamp. 
  - It will be noted only for the first time they leave.
- 'Present_Today.txt' file contains a list of all attendees (excluding unidentified users).
- If the date in the Attendance file appears as ######, expand/increase its width to see the date.

<br/>

##### CSE-2 teachers, please send a request to access the below file to retrieve the list of students from the class. It hasn't been uploaded to maintain privacy. #####
https://docs.google.com/spreadsheets/d/14xYkrpZ-IqC7VWssLItvTFOMl-BOEI92hOvUm1kP330/edit?usp=sharing
>When downloading, please download in .csv format
