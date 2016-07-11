"""
    FileManegerView.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

#!/usr/bin/python

import os, sys
import Tkinter as tkinter
import tkMessageBox

TITLE = "File Manager"
GEOMETRY = '962x409+200+250'
TASHVIEW_GEOMETRY = '783x465+400+400'

class FileManagerView(tkinter.Toplevel):
    def __init__(self, screen):
        tkinter.Toplevel.__init__(self, screen)
        self.screen = screen
        self.geometry(GEOMETRY)
        topFrame = tkinter.Frame(self)

        bottomFrame = tkinter.Frame(self)
        bottomFrame.pack(side = tkinter.BOTTOM)
        topFrame.pack()
        
        self.fileList = tkinter.Listbox(topFrame, width = 105, height = 20)
        self.fileList.pack()
        bottomFrame = tkinter.Frame(self, height = 8)
        bottomFrame.pack(side = tkinter.BOTTOM)
        topFrame.pack()
        
        """
        scrollbar = tkinter.Scrollbar(topFrame, orient = tkinter.VERTICAL)
        scrollbar.pack(side = tkinter.BOTTOM, fill = tkinter.y)
        """
        # self.fileList.config(xscrollcommand = scrollbar.set)

        """
        self.fileList = tkinter.Listbox(topFrame, selectmode=tkinter.MULTIPLE)
        self.fileList.pack(side="top", fill="both", expand=True)
        
        self.scrollbar = tkinter.Scrollbar(topFrame, orient = tkinter.VERTICAL)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self.fileList.config(xscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.fileList.xview)
        """
        
        self.entryBox = tkinter.Entry(bottomFrame, width = 32)
        self.entryBox.pack(side = tkinter.LEFT)
       
        # Search Button
        searchButton = tkinter.Button(bottomFrame, text='Search') #, command=self.executeSearch)
        # searchButton.config(width=10, height=3, bd=5)
        searchButton.pack(side=tkinter.LEFT, padx=5, pady=5)
           
        # Clear Button
        clearButton = tkinter.Button(bottomFrame, text='Clear Results') #, command=self.clearListView)
        # clearButton.config(width=10, height=3, bd=5)
        clearButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        
        # Quit Button
        quitButton = tkinter.Button(bottomFrame, text='Quit') #, command=self.quitDialog)
        # quitButton.config(width=10, height=3, bd=5)
        quitButton.pack(side=tkinter.RIGHT, padx=5, pady=5)

        # View Trash Button
        viewTrashButton = tkinter.Button(bottomFrame, text='View Trash', command=self.makeTrashWindow)
        viewTrashButton.config(width=10, height=3, bd=5)
        viewTrashButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        
        # Move to Trash Button
        trashButton = tkinter.Button(bottomFrame, text='Move To Trash', command=self.moveToTrash)
        trashButton.config(width=10, height=3, bd=5)
        trashButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        
    def quitDialog(self):
        if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
            sys.exit()
        else:
            tkMessageBox.showinfo(' ', 'Okay cool. Keep managing your files :)')

    def makeTrashWindow(self):
        self.newWindow = tkinter.Toplevel(self)
        self.trashView = TrashView(self.newWindow)

    # TODO - Move To Trash
    def moveToTrash(self):
        print("Move to trash - not yet implemented")

    # TODO - Search functionality
    def executeSearch(self):
        print("Search - Not yet implemented")

    # TODO - Clear List
    def clearListView(self):
        print("Clear - Not yet implemented")

    def updateHits(self, newHits):
        self.fileList.delete(0, tkinter.END)
        for h in newHits:
            self.fileList.insert(tkinter.END, h)
    
    def clearEntry(self, event):
        self.entryBox.delete(0, tkinter.END)

    def setEntry(self, text):
        self.entryBox.insert(0, text)

    def bindEntry(self, cmd, handler):
        self.entryBox.bind(cmd, handler)

    def getEntry(self):
        return self.entryBox.get()

        """
        # self.screen = tkinter.Tk()
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)
        self.screen.geometry(GEOMETRY)
        self.screen.title(TITLE)
        self.screen.bind('<Escape>', (lambda event: self.quit()))
        
        self.scrollbar = tkinter.Scrollbar(self.screen)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox = tkinter.Listbox(self.screen, selectmode=tkinter.MULTIPLE)
        self.listbox.pack(side="top", fill="both", expand=True)

        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        # The selection is one off with Button-1; gotta use ListboxSelect
        #self.listbox.bind("<Double-1>", self.onDoubleClick)
        
        """
class TrashView:
    def __init__(self, screen):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)
        self.screen.title("Trash")
        self.screen.geometry(TASHVIEW_GEOMETRY)
        self.deleteButton = tkinter.Button(self.frame, text = 'delete', width = 25, command = self.deleteFile)
        self.deleteButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.restoreButton = tkinter.Button(self.frame, text = 'restore', width = 25, command = self.restoreFile)
        self.restoreButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        self.closeButton = tkinter.Button(self.frame, text = 'close', width = 25, command = self.closeWindow)
        self.closeButton.pack(side=tkinter.LEFT, padx=5, pady=5)

        # Trash view listbox
        self.scrollbar = tkinter.Scrollbar(self.screen)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox = tkinter.Listbox(self.screen, selectmode=tkinter.MULTIPLE)
        self.listbox.pack(side="top", fill="both", expand=True)
    
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.frame.pack()

    # TODO - Restore file
    def restoreFile(self):
        print("Restore File - Not yet implemented")
    
    # TODO - Delete file
    def deleteFile(self):
        print("Delete File = Not yet implemented")
    
    def closeWindow(self):
        self.screen.destroy()

if __name__ == '__main__':
    screen = tkinter.Tk()
    screen.withdraw()
    screen.title("File Manager")
    fileManager = FileManagerView(screen)
    screen.mainloop()
