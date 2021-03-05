from tkinter import *
import os
from tkinter import ttk
from tkinter.filedialog import askopenfilename,askopenfile
import pandas as pd
from datetime import date,datetime
from tkinter.scrolledtext import ScrolledText

class attendance_app(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x500+300+200')

        self.title("Microsoft Teams Attendance Mapper")
        self.filepath = False
        self.label_1 = Label(self,text="Welcome.",font=('bold',14))
        self.label_1.place(x=400,y=50,anchor="center")

        self.label_2 = Label(self,text="Please upload the csv file directly downloaded from the Microsoft Teams Meeting in the next page")
        self.label_2.place(x=400,y=100,anchor="center")
        

        self.btn_1 = ttk.Button(self, text='Go', command=lambda:self.label_1.destroy() or self.btn_1.destroy() or self.label_2.destroy() or self.page_1())
        self.btn_1.place(x=400,y=150,anchor='center')


    def page_1(self):

        self.label_1 = Label(self,text="Please Upload the Participants List Downloaded from the Microsoft Teams Meeting",font=('bold',12))
        self.label_1.place(x=400,y=70,anchor="center")

        self.btn_1 = ttk.Button(self, text='Open Attendance Sheet',width=40, command=self.open_file)
        self.btn_1.place(x=400,y=110,anchor="center")

        

        self.btn_2 = ttk.Button(self,text='Next',command=lambda: destroywig() or self.verification_page())
        self.btn_2.place(x=400,y=160,anchor="center")

        def destroywig():
            self.label_1.destroy()
            self.label_2.destroy()
            self.btn_1.destroy()
            self.btn_2.destroy()
            
        
    
    def verification_page(self):
        if self.filepath:

            self.label_1 = Label(self,text="The File you have uploaded is: "+str(self.filepath),font=('bold',11))
            self.label_1.place(x=400,y=100,anchor="center")

            
            self.btn_1 = ttk.Button(self, text='Change Uploaded File', command=lambda: destroywig() or self.page_1())
            self.btn_1.place(x=330,y=150,anchor='center')

            self.btn_2 = ttk.Button(self,text="Map Attendance",command=lambda: destroywig() or self.attendance_mapper() or self.mark_attendance())
            self.btn_2.place(x=470,y=150,anchor="center")

        else:
            self.page_1()

        def destroywig():
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.label_1.destroy()

            
    def mark_attendance(self):

        self.label_1 = Label(self,text="Attendance has been marked!",font=('bold',14))
        self.label_1.place(x=400,y=40,anchor="center")

        self.label_2 = Label(self,text="All the lists will be found in the Reports Directory under "+self.date)
        self.label_2.place(x=400,y=70,anchor="center")

        
        self.label_3 = Label(self, text="Choose which list you would like to view", font=("bold", 11))
        self.label_3.place(x=260, y=160,anchor='center')

        
        self.display_choice = ttk.Combobox(self, values=["Display Absentees", "Display Attendees with Join Time", 
                                                          "Display Attendees with Time they Left",
                                                          "Display Unidentified Attendees"],width=35)

        self.display_choice.place(x=540, y=160,anchor='center')
        self.display_choice.current(0)

        self.btn_1 = ttk.Button(self,text="Quit",command=self.destroy)
        self.btn_1.place(x=350,y=220,anchor="center")  

        self.btn_2 = ttk.Button(self,text="Go",command=lambda: destroywig() or self.display_mapping(self.display_choice.get()))
        self.btn_2.place(x=450,y=220,anchor="center")  
 

        self.btn_3 = ttk.Button(self,text="Map Another Sheet",command=lambda: destroywig() or self.display_choice.destroy() or self.page_1())
        self.btn_3.place(x=70,y=40,anchor="center")
        
        def destroywig():
            self.btn_1.destroy()
            self.btn_2.destroy()
            self.btn_3.destroy()
            self.label_1.destroy()
            self.label_2.destroy()
            self.label_3.destroy()
            

    def display_mapping(self,choice):
        self.display_choice.destroy()
        if choice == "Display Absentees":
            self.absentees_display()
        elif choice == "Display Attendees with Join Time":
            self.attendees_display()
        elif choice == "Display Attendees with Time they Left":
            self.left_display()
        elif choice == "Display Unidentified Attendees":
            self.unidentified_display()
        else:
            self.mark_attendance()

    def absentees_display(self):
      

        self.btn_4 = ttk.Button(self,text="Go Back",command=lambda: destroywig() or self.mark_attendance())
        self.btn_4.place(x=50,y=30,anchor="center")  

        self.label_1 = Label(self,text="Absentees",font=('bold',14))
        self.label_1.place(x=420,y=40,anchor="center")

        self.label_2 = Label(self,text="(The same list will be found in  the Reports Directory under "+self.date+" as absentees.txt)")
        self.label_2.place(x=420,y=70,anchor="center")

        absentees = open('Reports/'+str(self.date)+'/absentees.txt','r')
        self.e1 = Entry(relief=GROOVE,justify='center')
        self.e1.place(x=270,y=100,anchor='center')
        self.e1.insert(END,'NAME')

        self.e2 = Entry(relief=GROOVE,justify='center')
        self.e2.place(x=570,y=100,anchor='center')
        self.e2.insert(END,'ROLL NUMBER')
        x=320
        y=130

        self.scrollbar1 = Scrollbar(self)
        self.textbox1 = ScrolledText(self,width=40,height=10)
        self.textbox1.place(x=270,y=200,anchor='center')

        self.scrollbar2 = Scrollbar(self)
        self.textbox2 = ScrolledText(self,width=25,height=9)
        self.textbox2.place(x=570,y=200,anchor='center')
        num = 1
        for line in absentees:
            name,rollnumber = line.split('\t')
            name=name.title()
            self.textbox1.insert(END, str(num)+'. '+name+'\n')
            self.textbox2.insert(END,str(num)+'. '+rollnumber)
            num+=1

        self.textbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textbox1.yview)
        self.textbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.textbox2.yview)
        


        self.label_3 = Label(self,text="Please Note the below Unidentified Participants")
        self.label_3.place(x=400,y=330,anchor="center")
        unidentified = open('Reports/'+str(self.date)+'/Unidentified_Participants.txt','r')
        self.scrollbar = Scrollbar(self)
        self.textbox = ScrolledText(self,width=50,height=2)
        self.textbox.place(x=400,y=365,anchor='center')
        for line in unidentified:
            if (line.startswith('Mrs')==True) or (line.startswith('Ms')==True) or (line.startswith('Smt')==True) or (line.startswith('Mr')==True) or (line.startswith('Dr')==True):
                continue
            self.textbox.insert(END, line)
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        def destroywig():
            self.e1.destroy()
            self.e2.destroy()
            self.label_3.destroy()
            self.scrollbar.destroy()
            self.textbox.destroy()
            self.textbox.frame.destroy()
            self.scrollbar1.destroy()
            self.textbox1.destroy()
            self.textbox1.frame.destroy()
            self.scrollbar2.destroy()
            self.textbox2.destroy()
            self.textbox2.frame.destroy()
            self.btn_4.destroy()
            self.label_1.destroy()
            self.label_2.destroy()
          


    def attendees_display(self):

        self.btn_1 = ttk.Button(self,text="Go Back",command=lambda: destroywig() or self.mark_attendance())
        self.btn_1.place(x=50,y=30,anchor="center")  

        self.label_1 = Label(self,text="Attendees with the Time they Joined",font=('bold',14))
        self.label_1.place(x=420,y=40,anchor="center")

        self.label_2 = Label(self,text="(The same list will be found in the Reports Directory under "+self.date+" as Present_Today.txt)")
        self.label_2.place(x=420,y=70,anchor="center")

        attendees = open('Reports/'+str(self.date)+'/Present_Today.txt','r')
        self.e1 = Entry(relief=GROOVE,justify='center')
        self.e1.place(x=270,y=100,anchor='center')
        self.e1.insert(END,'Attendee Name')

        self.e2 = Entry(relief=GROOVE,justify='center')
        self.e2.place(x=570,y=100,anchor='center')
        self.e2.insert(END,'Join Time')
        x=320
        y=130

        self.scrollbar1 = Scrollbar(self)
        self.textbox1 = ScrolledText(self,width=40,height=20)
        self.textbox1.place(x=270,y=280,anchor='center')

        self.scrollbar2 = Scrollbar(self)
        self.textbox2 = ScrolledText(self,width=20,height=20)
        self.textbox2.place(x=570,y=280,anchor='center')
        num=1
        for line in attendees:
            name,rollnumber = line.split('\t')
            name=name.title()
            self.textbox1.insert(END, str(num)+'. '+name+'\n')
            self.textbox2.insert(END,str(num)+'. '+rollnumber)
            num+=1

        self.textbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textbox1.yview)
        self.textbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.textbox2.yview)
        

        def destroywig():
            self.e1.destroy()
            self.e2.destroy()
            self.scrollbar1.destroy()
            self.textbox1.destroy()
            self.textbox1.frame.destroy()
            self.scrollbar2.destroy()
            self.textbox2.destroy()
            self.textbox2.frame.destroy()
            self.btn_1.destroy()
            self.label_1.destroy()
            self.label_2.destroy()
        
    def left_display(self):

        self.btn_1 = ttk.Button(self,text="Go Back",command=lambda: destroywig() or self.mark_attendance())
        self.btn_1.place(x=50,y=30,anchor="center")  

        self.label_1 = Label(self,text="Attendees with the Time they Left",font=('bold',14))
        self.label_1.place(x=420,y=40,anchor="center")

        self.label_2 = Label(self,text="(The same list will be found in the Reports Directory under "+self.date+" as Left.txt)")
        self.label_2.place(x=420,y=70,anchor="center")

        left = open('Reports/'+str(self.date)+'/Left.txt','r')
        self.e1 = Entry(relief=GROOVE,justify='center')
        self.e1.place(x=270,y=100,anchor='center')
        self.e1.insert(END,'Attendee Name')

        self.e2 = Entry(relief=GROOVE,justify='center')
        self.e2.place(x=570,y=100,anchor='center')
        self.e2.insert(END,'Leave Time')
        x=320
        y=130

        self.scrollbar1 = Scrollbar(self)
        self.textbox1 = ScrolledText(self,width=40,height=15)
        self.textbox1.place(x=270,y=240,anchor='center')

        self.scrollbar2 = Scrollbar(self)
        self.textbox2 = ScrolledText(self,width=20,height=15)
        self.textbox2.place(x=570,y=240,anchor='center')

        num=1
        for line in left:
            name,rollnumber = line.split('\t')
            name=name.title()
            self.textbox1.insert(END, str(num)+'. '+name+'\n')
            self.textbox2.insert(END,str(num)+'. '+rollnumber)
            num+=1

        self.textbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.textbox1.yview)
        self.textbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.textbox2.yview)
        

        def destroywig():
            self.e1.destroy()
            self.e2.destroy()
            self.scrollbar1.destroy()
            self.textbox1.destroy()
            self.textbox1.frame.destroy()
            self.scrollbar2.destroy()
            self.textbox2.destroy()
            self.textbox2.frame.destroy()
            self.btn_1.destroy()
            self.label_1.destroy()
            self.label_2.destroy()

    def unidentified_display(self):

        self.btn_1 = ttk.Button(self,text="Go Back",command=lambda: destroywig() or self.mark_attendance())
        self.btn_1.place(x=50,y=30,anchor="center")  

        self.label_1 = Label(self,text="Unidentified Participants",font=('bold',14))
        self.label_1.place(x=400,y=40,anchor="center")

        self.label_2 = Label(self,text="The same list will be found in the Reports Directory under "+self.date+" as Unidentified_Participants.txt")
        self.label_2.place(x=400,y=80,anchor="center")

        unidentified = open('Reports/'+str(self.date)+'/Unidentified_Participants.txt','r')
        self.scrollbar = Scrollbar(self)
        self.textbox = ScrolledText(self,width=50,height=5)
        self.textbox.place(x=400,y=140,anchor='center')
        for line in unidentified:
            if (line.startswith('Mrs')==True) or (line.startswith('Ms')==True) or (line.startswith('Smt')==True) or (line.startswith('Mr')==True) or (line.startswith('Dr')==True):
                continue
            self.textbox.insert(END, line)
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        def destroywig():
            self.scrollbar.destroy()
            self.textbox.destroy()
            self.textbox.frame.destroy()
            self.btn_1.destroy()
            self.label_1.destroy()
            self.label_2.destroy()
    
    def attendance_mapper(self):

        attendance_sheet = pd.read_csv(self.filepath, index_col=0, encoding='utf-16', sep="\t")
        attendance_sheet.index.name = None
        left = attendance_sheet[attendance_sheet['User Action'] == 'Left']
        attendance_sheet = attendance_sheet[~attendance_sheet.index.duplicated(keep='first')]

        student_record = pd.read_csv('Attendance.csv', index_col=0)

        
        today = str(attendance_sheet['Timestamp'][0].split(',')[0]).replace("/",'-')

        self.date = today
        student_record[today] = ''
        others = []

        for index in attendance_sheet.index:
            if index in student_record.index:
                student_record[today][index] = 'P'
            else:
                others.append(index)
        
        student_record.to_csv('Attendance.csv')

        
        if not os.path.exists('Reports'):
            os.makedirs('Reports')
        if not os.path.exists('Reports/'+str(today)):
            os.makedirs('Reports/'+str(today))

        with open('Reports/'+str(today)+'/Left.txt', 'w') as f:
            for index in left.index:
                date,time = attendance_sheet['Timestamp'][index].split(',')
                f.write("%s\n" % (index+'\t'+time))

        with open('Reports/'+str(today)+'/Present_Today.txt', 'w') as f:
            for index in attendance_sheet.index:
                date,time = attendance_sheet['Timestamp'][index].split(',')
                f.write("%s\n" % (index+'\t'+time))
            

        with open('Reports/'+str(today)+'/Unidentified_Participants.txt', 'w') as f:
            for item in others:
                f.write("%s\n" % item)
        
        student_df = pd.read_csv("Attendance.csv", index_col=0)
        absentees = student_df[student_df[today] != 'P']

        with open('Reports/'+str(today)+'/absentees.txt', 'w') as f:
            for index in absentees.index:
                f.write("%s\n" % (index+'\t'+absentees['Roll Number'][index]))

        
    
    def open_file(self):
        self.filepath = askopenfilename() 





if __name__ == '__main__':
    attendance_app().mainloop()

#Code developed, written and tested by Soumya Vemuri
