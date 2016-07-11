"""
    FileManegerModel.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import sys, os
import Tkinter as tkinter

class Helper:
  def __init__(self, value = None):
    self.data = value
    self.callbacks = {}

  def addCallback(self, func):
    self.callbacks[func] = 1

  def deleteCallback(self, func):
    del self.callback[func]

  def getCallbacks(self):
    for func in self.callbacks:
      func(self.data)

  def setData(self, data):
    self.data = data
    self.getCallbacks()

  def getData(self):
    return self.data

  def unsetData(self):
    self.data = None

class FileManagerModel(object):
  def __init__(self):
    self.results = Helper([])
    self.directory = Helper(os.getcwd())

  def clearAllResults(self):
    self.setResults([])

  def setResults(self, newResults):
    self.results.setData(newResults)

  def getDirectory(self):
    return self.directory.getData()
