"""
    FileManegerView.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import sys, os
import Tkinter as tkinter

GEOMETRY = '962x409+200+250'

class FileManagerView(tkinter.Toplevel):
  def __init__(self, master):
      
    tkinter.Toplevel.__init__(self, master)
    
    # Menu bar
    self.menubar = tkinter.Menu(self.master) #Needs something relevant to root
    self.menubar.config(bg='#00ff00')
    
    self.filemenu = tkinter.Menu(self.menubar, tearoff=1)
    self.menubar.add_cascade(menu=self.filemenu, label='File')
    
    self.helpmenu = tkinter.Menu(self.menubar)
    self.menubar.add_cascade(menu=self.helpmenu, label='Help')
    
    self.master.config(menu=self.menubar) #same

    self.geometry(GEOMETRY)
    topFrame = tkinter.Frame(self)
    
    # Results list and scrollbar
    scrollbar = tkinter.Scrollbar(topFrame, orient = tkinter.VERTICAL)
    # scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)
    
    self.resultsList = tkinter.Listbox(topFrame, width = 105, height = 20)
    self.resultsList.pack()
    bottomFrame = tkinter.Frame(self, height = 8)
    bottomFrame.pack(side = tkinter.BOTTOM)
    topFrame.pack()
    
    self.resultsList.config(xscrollcommand = scrollbar.set)
    # scrollbar.config(command = self.resultsList.xview)
    
    # Search Box
    self.searchBox = tkinter.Entry(bottomFrame, width = 32)
    self.searchBox.pack(side = tkinter.LEFT)
    
    # Buttons
    self.searchButton = tkinter.Button(bottomFrame, text = 'Search')
    self.searchButton.config(width = 10, height = 2, bd = 3)
    self.searchButton.pack(side=tkinter.LEFT, padx=5, pady=5)
    
    self.clearFile = tkinter.Button(bottomFrame, text='Clear')
    self.clearFile.config(width = 10, height = 2, bd = 3, command = self.DeleteSelection)
    self.clearFile.pack(side=tkinter.LEFT, padx=5, pady=5)

    self.clearAllButton = tkinter.Button(bottomFrame, text = 'Clear All')
    self.clearAllButton.config(width = 10, height = 2, bd = 3)
    self.clearAllButton.pack(side=tkinter.LEFT, padx=5, pady=5)
    
    self.quitButton = tkinter.Button(bottomFrame, text = 'Quit')
    self.quitButton.config(width = 10, height = 2, bd = 3)
    self.quitButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
  
  def DeleteSelection(self) :
    items = self.resultsList.curselection()
    pos = 0
    for i in items:
        idx = int(i) - pos
        self.resultsList.delete(idx, idx)
        pos = pos + 1

  def updateResults(self, newResults):
    self.resultsList.delete(0,tkinter.END)
    for result in newResults:
      self.resultsList.insert(tkinter.END, result)
    
  def clearEntry(self, event):
    self.searchBox.delete(0, tkinter.END)

  def setEntry(self, text):
    self.searchBox.insert(0, text)

  def bindEntry(self, command, handler):
    self.searchBox.bind(command, handler)

  def getEntry(self):
    return self.searchBox.get()
