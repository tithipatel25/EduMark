"""
Description: This module provides functionalities for managing educational marks for students.
It includes classes and methods to add, update, retrieve, and calculate average marks.

Programmer: Tithi Patel

Pre-conditions: Require the word "test" or "final"
Post-conditions: Returns a treeview that can add, update, or remove a test & students from the files.

"""

from tkinter import * #imports all tkinter functions
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

        

