"""
    FileManegerController.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import sys, os
import Tkinter as tk
import tkMessageBox

import FileManagerModel
import FileManagerView 

class FileManagerController(object):
  def __init__(self, screen):
    self.model = FileManagerModel.FileManagerModel()
    self.model.results.addCallback(self.resultsChanged)
    self.view = FileManagerView.FileManagerView(screen)
    self.view.bind("<Escape>", lambda event: screen.quit())
    self.view.setEntry("Enter a search query....")
    self.view.bindEntry("<Button-1>", self.view.clearEntry)
    self.view.bindEntry("<Return>", self.search)
    
    self.view.clearAllButton.config(command = self.clearAll)
    self.view.searchButton.config(command = self.search)
    self.view.quitButton.config(command = self.quitDialog)
  
    
    self.view.filemenu.add_command(label='Search', command=self.search)
    self.view.filemenu.add_command(label='Clear All', command=self.clearAll)
    self.view.filemenu.add_command(label='Exit', command=self.quit)
  
    self.view.helpmenu.add_command(label='Get Help', command=self.showWarning)
    self.view.helpmenu.add_command(label='About', command=self.showWarning2)
    
  def showWarning(self):
    tkMessageBox.showwarning('Get Help', 'Contact Dr. Malloy.')
  
  def showWarning2(self):
    tkMessageBox.showwarning('About', 'A simple GUI file management application built in Python with Tkinter. This program allows the user to search for file names and file types and then returns the results of all matches within subdirectories. The user may rename, move, or delete the selected files.')
  
  def resultsChanged(self, results):
    self.view.updateResults(results)

  def clearAll(self):
    self.model.clearAllResults()
  
  
  def quit(self):
      sys.exit()

  def quitDialog(self):
    if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
        sys.exit()
    else:
        tkMessageBox.showinfo(' ', 'Okay cool. Keep managing your files :)')

  def search(self, event = None):
    self.model.clearAllResults()         # Must clear old results to make room for new searches
    entry = self.view.getEntry()
    subDirectories = [self.model.getDirectory()]
    temp = []
    while subDirectories:
      searchDirectory = subDirectories.pop()
      currentDirectory = os.listdir(searchDirectory)
      for i in currentDirectory:
        result = os.path.join(searchDirectory, i)

        if os.path.isdir(result):
          subDirectories.append(result)
          
        if entry in i:
	  temp.append(result)
      self.view.updateResults(temp)
