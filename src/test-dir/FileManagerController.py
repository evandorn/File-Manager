import sys, os
import Tkinter as tk
import tkMessageBox

import FileManagerModel
import FileManagerView 

class Controller(object):
  def __init__(self, root):
    self.model = FileManagerModel.Model()
    self.model.results.addCallback(self.resultsChanged)
    self.view = FileManagerView.View(root)
    self.view.bind("<Escape>", lambda event: root.quit())
    self.view.setEntry("Enter a search query....")
    self.view.bindEntry("<Button-1>", self.view.clearEntry)
    self.view.bindEntry("<Return>", self.searchModel)
    self.view.clearAllButton.config(command = self.clear)
    self.view.searchButton.config(command = self.searchModel)
    self.view.quitButton.config(command = self.quitDialog)
  
  def resultsChanged(self, hits):
    self.view.updateResults(hits)

  def entryChanged(self,entry):
    pass

  def clear(self):
    self.model.clear()
  
  def quitDialog(self):
    if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
        sys.exit()
    else:
        tkMessageBox.showinfo(' ', 'Okay cool. Keep managing your files :)')

  def searchModel(self, event = None):
    self.model.clear()
    part = self.view.getEntry()
    subdirs = [self.model.getDirectory()]
    temp = []
    while subdirs:
      dirToSearch = subdirs.pop()
      thisDirectory = os.listdir(dirToSearch)
      for i in thisDirectory:
        toPush = os.path.join(dirToSearch, i)

        if os.path.isdir(toPush):
          subdirs.append(toPush)
          
        if part in i:
	  temp.append(toPush)
      
      self.view.updateResults(temp)
