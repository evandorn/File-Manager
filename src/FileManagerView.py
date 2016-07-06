"""
    FileManegerView.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

#!/usr/bin/python

import Tkinter as tk
import Tkconstants, tkFileDialog

class FileManagerView(object):
    
    def __init__(self):
        self.root = tk.Tk()
        self.interfaceInit()

    def interfaceInit(self):
        self.root.title("File Manager")
        self.root.geometry("1024x768+300+300")
    
    def mainloop(self):
        self.root.mainloop()

    def quit(self):
        sys.exit()

if __name__ == 'main':
    fileManager = FileManagerView()
    fileManager.mainloop()
