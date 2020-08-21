* Just clicking attendance.py file will run it.
	It can also be run from command prompt
	python attendance.py

REQUIREMENTS 
* To use this code, the user needs Python 3.7 or any later version installed

* Pandas is also required to be installed
* After installing Python please run the following command to install Pandas
	pip install pandas

* After downloading the list from Microsoft Teams, please open the'meetingsAttendanceList' 
	file and save as CSV. Otherwise, the code will not work.


OTHER GUIDELINES

* Please Request the class to join the meeting with their college assigned email IDs
	or at least using the display name in that email ID

* The code works at 100% efficiency if the names the participants used to access the class
	matches their name in C2 file.

* I have matched the names of all C2 students to their display names given by the college admin
	for the college assigned email IDs, i.e., ugsXXXXX_cse.XXXXX@cbit.org.in

* The guest participants entering will be marked ABSENT in the Attendance Register
	BUT, the list of all these participants can be found in 'Unidentified Participants.txt'.
	The user will need to update manually

* 'Left.txt' File contains names of participants who left in the middle of todays class
	their last timestamp for their leave will also be displayed

* 'Present.txt' File contains a list of all students (excluding unidentified users) Present today

* 'Unidentified Participants', 'Left' and 'Present' are erased and updated everytime  
	attendance.py is run

* If the date in the C2 file appears as ######, expand/increase its width to see the date