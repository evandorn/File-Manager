import os
import sys
import Tkinter as tkinter

GEOMETRY = '962x409+200+250'

class View(tkinter.Toplevel):
  def __init__(self, master):
    tkinter.Toplevel.__init__(self, master)
    self.geometry(GEOMETRY)
    topFrame = tkinter.Frame(self)
    self.resultsList = tkinter.Listbox(topFrame, width = 105, height = 20)
    self.resultsList.pack()
    bottomFrame = tkinter.Frame(self, height = 8)
    bottomFrame.pack(side = tkinter.BOTTOM)
    topFrame.pack()
    
    scrollbar = tkinter.Scrollbar(topFrame, orient = tkinter.VERTICAL)
    scrollbar.pack(side = tkinter.BOTTOM, fill = tkinter.Y)
    
    self.resultsList.config(xscrollcommand = scrollbar.set)
    scrollbar.config(command = self.resultsList.xview)
    
    self.searchBox = tkinter.Entry(bottomFrame, width = 32)
    self.searchBox.pack(side = tkinter.LEFT)
    
    self.searchButton = tkinter.Button(bottomFrame, text = 'Search')
    self.searchButton.config(width=10, height=3, bd=5)
    self.searchButton.pack(side=tkinter.LEFT, padx=5, pady=5)
    
    self.clearFile = tkinter.Button(bottomFrame, text='Clear Result')
    self.clearFile.config(width=10, height=3, bd=5)
    self.clearFile.pack(side=tkinter.LEFT, padx=5, pady=5)

    self.clearAllButton = tkinter.Button(bottomFrame, text = 'Clear All')
    self.clearAllButton.config(width = 10, height = 2, bd = 3)
    self.clearAllButton.pack(side=tkinter.LEFT, padx=5, pady=5)
    
    self.quitButton = tkinter.Button(bottomFrame, text = 'Quit')
    self.quitButton.config(width = 10, height = 3, bd = 5)
    self.quitButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
  
  def updateHits(self, newHits):
    self.resultsList.delete(0,tkinter.END)
    for h in newHits:
      self.resultsList.insert(tkinter.END, h)
    
  def clearEntry(self, event):
    self.searchBox.delete(0, tkinter.END)

  def setEntry(self, text):
    self.searchBox.insert(0, text)

  def bindEntry(self, command, handler):
    self.searchBox.bind(command, handler)

  def getEntry(self):
    return self.searchBox.get()
