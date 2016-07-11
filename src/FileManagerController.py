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

class Controller(object):
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
  
  def resultsChanged(self, results):
    self.view.updateResults(results)

  def clearAll(self):
    self.model.clearAllResults()
  
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
