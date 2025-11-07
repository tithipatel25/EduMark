"""
Description: A Module that imports the files and reads them, while organzing them into a treeview 
Programmer: Krisha Shah & Tithi Patel
Date: Januaray 22nd,2024
Version 1.0

Pre-condition: the tests, have to have the word test or final 
Post-condition: returns a treeview that can add,update or remove a test or students from the files
"""


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
#from finalreportmodule import Report

my_filetypes = [('all files', '.*'), ('text files', '.txt')]

student1=[]
file1=[]
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Marks")
        self.screenwidth = 925
        self.screenheight = 500
        self.screenx = 300
        self.screeny = 100
        self.geometry("{}x{}+{}+{}".format(self.screenwidth, self.screenheight, self.screenx, self.screeny))
        self.resizable(False, False)
        self.signupframe = Frame(width=self.screenwidth, height=self.screenheight, bg="#144190")
        self.signupframe.place(x=0, y=0)
        bgimage = PhotoImage(file="temp_back.png")
        bglbl = Label(self.signupframe, image=bgimage, bg="#00001A")
        bglbl.place(x=0, y=0)
        bglbl.image = bgimage
        frame = Frame(self.signupframe, width=350, height=400, bg="lightgrey")
        frame.place(x=300, y=50)
        continuelbl=Label(frame,text="Please select a file from each category!",fg="black",
                           bg="lightgrey",font=("garmond", 12))
        continuelbl.place(x=35,y=70)
        studentbtn = Button(frame, width=30, font=("garmond", 12), height=2, pady=7, text="Students Information",
                            bg="black", fg="white", border=0, command=self.students)
        studentbtn.place(x=35, y=123)
        filebtn = Button(frame, width=30, height=2, pady=7, font=("garmond", 12), text="Marks", border=0, fg="white",
                         bg="#053d53", command=self.file)
        filebtn.place(x=35, y=204)
        continuelbl=Label(frame,text="Please Continue!!",fg="black",
                           bg="lightgrey",font=("garmond", 12))
        continuelbl.place(x=55,y=290)
        contbtn=Button(frame,width=12,pady=7, text="Continue",border=0,fg="white",bg="#053d53",
                       command=self.continues)
        contbtn.place(x=200,y=285)
        

        self.mainloop()
    def students(self):
        answer = filedialog.askopenfilename(parent=self, initialdir=os.getcwd(), title="Please select a file:", filetypes=my_filetypes)
        messagebox.showinfo(message="You selected: " + answer)
        student1.append(answer)

        
    def file(self):
        answer = filedialog.askopenfilename(parent=self, initialdir=os.getcwd(), title="Please select a file:", filetypes=my_filetypes)
        messagebox.showinfo(message="You selected: " + answer)
        file1.append(answer)
    
    def continues(self):
        try:
            self.screenname = "signin"
            self.title("Student Marks")
            self.screenwidth = 925
            self.screenheight = 500
            self.screenx = 300
            self.screeny = 100
            self.font = ("garamond", 12)
            marks=[]
            self.geometry("{}x{}+{}+{}".format(self.screenwidth, self.screenheight, self.screenx, self.screeny))
            self.resizable(False, False)

            self.mycolumns = ["First Name", "Last Name", "Student Number"]
            
            #Check if both files have been selected
            if not student1 or not file1:
                messagebox.showerror("Error", "Please select both files.")
                return

            student_file = student1[0]
            mark_file = file1[0]

            #Opens the file with the test and makes the columns accordingly
            with open(mark_file, "r") as g:
                line = g.readline()
                lines = g.readlines()
                selected_lines = [line.strip() for line in lines if "test" in line.lower() or "final" in line.lower()]
            columns = []
            for line in selected_lines:
                l = line.split(",")
                name = l[0]
                columns.append(name)

            for test in columns:
                self.mycolumns.append(test)

            self.signinpageframe = Frame(width=self.screenwidth, height=self.screenheight, bg="lightgrey")
            self.signinpageframe.place(x=0, y=0)

            treeview_frame = Frame(self)
            treeview_frame.grid(row=0, column=0, padx=(10, 10), pady=10, sticky=E)

            self.tv = ttk.Treeview(treeview_frame, columns=self.mycolumns, show="headings", selectmode="browse")

            for col in self.mycolumns:
                self.tv.heading(col, text=col)
                self.tv.column(col, width=110)

            self.tv.pack(side=LEFT, fill=Y)

            v_scrollbar = ttk.Scrollbar(treeview_frame, orient=VERTICAL, command=self.tv.yview)
            v_scrollbar.pack(side=RIGHT, fill=Y)
            self.tv.configure(yscrollcommand=v_scrollbar.set)

            def add_data_to_treeview():
                for i in range(min(len(self.data), len(marks))):
                    record = self.data[i]
                    mark = marks[i]  
                    combined_values = record + mark
                    #print("Combined Values:", combined_values)
                    self.tv.insert("", "end", values=combined_values)
                    
            #open the file with student information and adds the data
            with open(student_file, 'r') as g:
                lines = g.readlines()
                self.data = [line.strip().split(",") for line in lines[1:]]
                

            # Read the content of the text file
            with open(mark_file, 'r') as file:
                lines = file.readlines()

            # Initialize a dictionary to store student scores
            student_scores = {}
            

            
            is_test_line = False
            is_final_line = False

            # Go through each line and extract information
            for line in lines:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Check if the line is a test line or final line
                is_test_line = "test" in line.lower() 
                is_final_line = "final" in line.lower()

                # Extract student number and scores if it's not a test or final line
                if not is_test_line and not is_final_line:
                    values = line.strip().split(',')
                    student_number = values[0]
                    scores = [int(score) if score.isdigit() else None for score in values[1:]]
                    
                    # If the student number already exists in the dictionary, append scores
                    if student_number in student_scores:
                        student_scores[student_number].extend(scores)
                    else:
                        student_scores[student_number] = scores

            # Get the values for each key
            for (key, values) in student_scores.items():
                marks.append(values)    
            add_data_to_treeview()    
            LF=LabelFrame(self,text="Student Information",font=self.font)
            LF.grid(row=1,column=0,padx=10,pady=(20,0),sticky=N)
            
            #labeling and adding entry box for student number
            self.studentnum_lbl=Label(LF,text="Student Number",font=self.font)
            self.studentnum_lbl.grid(row=2,column=0,sticky=E,pady=(10,10),padx=(20,10))
            self.studentnum_txt=Entry(LF,font=self.font)
            self.studentnum_txt.grid(row=0,column=1,sticky=W)
            self.studentnum_txt.focus()

            #labeling and adding entry box for first name
            self.firstname_lbl=Label(LF,text="First Name",font=self.font)
            self.firstname_lbl.grid(row=0,column=0,sticky=E,padx=(0,10),pady=(10,10))
            self.firstname_txt=Entry(LF,font=self.font)
            self.firstname_txt.grid(row=1,column=1,sticky=W)

            #labeling and adding entry box for last name
            self.lastname_lbl=Label(LF,text="Last Name",font=self.font)
            self.lastname_lbl.grid(row=1,column=0,sticky=E,padx=(0,10),pady=(10,10))
            self.lastname_txt=Entry(LF,font=self.font)
            self.lastname_txt.grid(row=2,column=1,sticky=W)

            #creating drop down options for the term
            self.termlbl=Label(LF,text="Term",font=self.font)
            self.termlbl.grid(row=0,column=2,padx=(50,0))
            self.termtypes=["Term","Final"]
            self.termcombo=ttk.Combobox(LF,width=5,state="readonly",values=self.termtypes)
            self.termcombo.grid(row=0,column=3,pady=10,padx=(0,20),sticky=W)
            self.termcombo.current(0)

            #creating a lbl + entry for the test name
            self.testlbl=Label(LF,text="Test Name",font=self.font)
            self.testlbl.grid(row=1,column=2,padx=(50,0))
            self.test_txt=Entry(LF,font=self.font,width=7)
            self.test_txt.grid(row=2,column=3,sticky=W,padx=(0,20))          

            #mark label
            self.mark_lbl=Label(LF,text="Mark",font=self.font)
            self.mark_lbl.grid(row=2,column=2,sticky=E,padx=(0,10))
            self.mark_txt=Entry(LF,font=self.font,width=7)
            self.mark_txt.grid(row=2,column=3,sticky=W,padx=(0,20))


            #adding the ADD button
            self.add_btn=Button(LF,text="Add",font=self.font,command=self.addbutton,width=10)
            self.add_btn.grid(row=3,column=1,sticky=E,padx=(0,10),pady=(15,5))

            #adding the UPDATE button
            self.update_btn=Button(LF,text="Update",font=self.font,command=self.updatebutton,width=10)
            self.update_btn.grid(row=3,column=2,sticky=E,padx=(0,10),pady=(15,5))

            #adding the DELETE button
            self.delete_btn=Button(LF,text="Delete",font=self.font,command=self.delbutton,width=10)
            self.delete_btn.grid(row=3,column=3,sticky=E,padx=(0,10),pady=(15,5))

            #Final Report Button
            self.report_btn=Button(LF,text="Final Report",font=self.font,command=self.repbutton,width=10)
            self.report_btn.grid(row=3,column=4,sticky=E,padx=(0,10),pady=(15,5))
        
        except:
            print("Error:",error,"Line:{}".format(sys.exc_info()[-1].tb_lineno))

    def addbutton(self):
        try:
            stunum_txt = self.studentnum_txt.get().strip()
            fn_txt = self.firstname_txt.get().strip()
            ln_txt = self.lastname_txt.get().strip()
            if stunum_txt != "" and fn_txt != "" and ln_txt != "":
                self.tv.insert("", "end", values=(stunum_txt, fn_txt, ln_txt))
                self.studentnum_txt.delete(0, END)
                self.firstname_txt.delete(0, END)
                self.lastname_txt.delete(0, END)
        except Exception as error:
            print("Error:", error, "Line:{}".format(sys.exc_info()[-1].tb_lineno))
    def updatebutton(self):
        pass
    def delbutton(self):
        pass
    def repbutton(self):
        pass
        
    
        
    
app = App()


