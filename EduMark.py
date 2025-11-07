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