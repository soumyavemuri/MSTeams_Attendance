import pandas as pd
import numpy as np
from datetime import date

# Microsoft Teams' participant list is saved as "meetingAttendanceList.csv"
# please open the meeting AttendanceList file and save as csv and
# the file name matches with attendance.csv
df = pd.read_csv('meetingAttendanceList.csv',index_col=0)
df.index.name = None


left = df[df['User Action']=='Left']
df = df[~df.index.duplicated(keep='first')]

# - Replace 'C2.csv' with the name of your attendance log csv file
# - please ensure that the names of students exactly match the display name
#   on Microsoft Teams
df1 = pd.read_csv('V-SEM CSE-2 Attendance.csv', index_col=0)

today = date.today().strftime("%d-%b-%Y")

df1[today] = 'A'
others = []

for index in df.index:
  if index in df1.index:
    df1[today][index] = 'P'
  else:
    others.append(index)

present = df1[df1[today]=='P']
df1.to_csv('V-SEM CSE-2 Attendance.csv')

with open('Left.txt','w') as outfile:
    left.to_string(outfile)

with open('Present Today.txt','w') as outfile:
    present.to_string(outfile)

with open('Unidentified Participants.txt','w') as f:
    for item in others:
        f.write("%s\n" % item)
