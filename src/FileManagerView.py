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
GEOMETRY = '864x620+200+250'
class FileManagerView(object):
    def __init__(self, screen):
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

        # Quit Button
        quitButton = tkinter.Button(text='Quit', command=self.quitDialog)
        quitButton.config(width=10, height=3, bd=5)
        quitButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        
        # Search Button
        searchButton = tkinter.Button(text='Search', command=self.executeSearch)
        searchButton.config(width=10, height=3, bd=5)
        searchButton.pack(side=tkinter.LEFT, padx=5, pady=5)
        
        # Clear Button
        clearButton = tkinter.Button(text='Clear Results', command=self.clearListView)
        clearButton.config(width=10, height=3, bd=5)
        clearButton.pack(side=tkinter.LEFT, padx=5, pady=5)

        # View Trash Button
        viewTrashButton = tkinter.Button(text='View Trash', command=self.makeTrashWindow)
        viewTrashButton.config(width=10, height=3, bd=5)
        viewTrashButton.pack(side=tkinter.RIGHT, padx=10, pady=5)
        
        # Move to Trash Button
        trashButton = tkinter.Button(text='Move To Trash', command=self.moveToTrash)
        trashButton.config(width=10, height=3, bd=5)
        trashButton.pack(side=tkinter.RIGHT, padx=10, pady=5)
    
    def quitDialog(self):
        if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
            sys.exit()
        else:
            tkMessageBox.showinfo(' ', 'Okay cool. Keep managing your files :)')

    def makeTrashWindow(self):
        self.newWindow = tkinter.Toplevel(self.screen)
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

class TrashView:
    def __init__(self, screen):
        self.screen = screen
        self.frame = tkinter.Frame(self.screen)
        self.screen.title("Trash")
        self.deleteButton = tkinter.Button(self.frame, text = 'delete', width = 25, command = self.deleteFile)
        self.deleteButton.pack()
        self.restoreButton = tkinter.Button(self.frame, text = 'restore', width = 25, command = self.restoreFile)
        self.restoreButton.pack()

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
    fileManager = FileManagerView(screen)
    screen.mainloop()
