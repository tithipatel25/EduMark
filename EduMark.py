"""
Description: This module provides functionalities for managing educational marks for students.
It includes classes and methods to add, update, retrieve, and calculate average marks.

Programmer: Tithi Patel

Pre-conditions: Require the word "test" or "final"
Post-conditions: Returns a treeview that can add, update, or remove a test & students from the files.

"""

from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
import sys

my_filetypes = [('Text File', '*.txt'), ('All Files', '*.*')]

student1 = []
file1=[]

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("EduMark - Educational Marks Manager")
        self.screenwidth = 925
        self.screenheight = 500
        self.screenx = 300
        self.screeny = 100
        self.geometry(f"{self.screenwidth}x{self.screenheight}+{self.screenx}+{self.screeny}")
        self.resizable(False, False)
        self.signupframe = Frame(width=self.screenwidth, height=self.screenheight, bg="#f0f0f0")
        self.signupframe.place(x=0, y=0)
        bgiamage = PhotoImage(file="temp_back.png")
        bglbl = Label(self.signupframe, image=bgiamage, bg="#00001A")
        bglbl.image = bgiamage
        frame = Frame(self.signupframe, width=350, height=400, bg="lightgrey")
        frame.place(x=300, y=50)
        





app = App()
app.mainloop()