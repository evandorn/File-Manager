"""
    FileManegerView.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

#!/usr/bin/python

import os, sys
import Tkinter as tkinter

TITLE = "File Manager"
GEOMETRY = '864x620+200+250'
class FileManagerView(object):
    def __init__(self):
        self.screen = tkinter.Tk()
        self.screen.geometry(GEOMETRY)
        self.screen.title(TITLE)
        self.screen.bind('<Escape>', (lambda event: self.quit()))
        self.interfaceInit()
        self.screen.mainloop()
        
    def interfaceInit(self):
        # labelFont = ('times', 20, 'bold')
        """
        label = tkinter.Label(self.screen, text = "Hello World")
        label.config(bg='white', fg='black')
        label.config(font=labelFont, height=3, width=20)
        label.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        """
        # Quit functionality
        """
        quitButton = tkinter.Button(text='Quit', command=quit)
        quitButton.config(width=20, height=3, bg='#ff0000', relief=tkinter.SUNKEN, bd=5)
        quitButton.pack(side=tkinter.BOTTOM, padx=5, pady=5)
    
        searchButton = tkinter.Button(text='Search')
        searchButton.config(width=20, height=3, bg='#ff0000', relief=tkinter.SUNKEN, bd=5)
        searchButton.pack(side=tkinter.BOTTOM, padx=0, pady=0)
        """
        MyButton1 = tkinter.Button(text="BUTTON1", width=10)
        MyButton1.grid(side=tkinter.BOTTOM, row=0, column=1)

        MyButton2 = tkinter.Button(text="BUTTON2", width=10)
        MyButton2.grid(side=tkinter.BOTTOM, row=0, column=2)

        MyButton3 = tkinter.Button(text="BUTTON3", width=10)
        MyButton3.grid(side=tkinter.BOTTOM, row=0, column=3)

    def quit(self):
        sys.exit()


if __name__ == '__main__':
    fileManager = FileManagerView()
