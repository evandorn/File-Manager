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
        
        # labelFont = ('times', 20, 'bold')
        """
            label = tkinter.Label(self.screen, text = "Hello World")
            label.config(bg='white', fg='black')
            label.config(font=labelFont, height=3, width=20)
            label.pack(expand=tkinter.YES, fill=tkinter.BOTH)
            """
        self.scrollbar = tkinter.Scrollbar(self.screen)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox = tkinter.Listbox(self.screen, selectmode=tkinter.MULTIPLE)
        self.listbox.pack(side="top", fill="both", expand=True)
        
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        # The selection is one off with Button-1; gotta use ListboxSelect
        self.listbox.bind("<Double-1>", self.onDoubleClick)
        
        
        # Quit functionality
        quitButton = tkinter.Button(text='Quit', command=quit)
        quitButton.config(width=20, height=3, bg='#ff0000', relief=tkinter.SUNKEN, bd=5)
        quitButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        
        searchButton = tkinter.Button(text='Search')
        searchButton.config(width=20, height=3, bg='#ff0000', relief=tkinter.SUNKEN, bd=5)
        searchButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        """
            MyButton1 = tkinter.Button(text="BUTTON1", width=10)
            MyButton1.grid(side=tkinter.BOTTOM, row=0, column=1)
            
            MyButton2 = tkinter.Button(text="BUTTON2", width=10)
            MyButton2.grid(side=tkinter.BOTTOM, row=0, column=2)
            
            MyButton3 = tkinter.Button(text="BUTTON3", width=10)
            MyButton3.grid(side=tkinter.BOTTOM, row=0, column=3)
        """
        
        self.screen.mainloop()
    
        
    def quit(self):
        sys.exit()

    def onDoubleClick(self, event):
        widget = event.widget
        selection=widget.curselection()
        print "SELECTION:", selection
        for x in selection:
            value = widget.get(x)
            print "Value is", value



if __name__ == '__main__':
    fileManager = FileManagerView()
