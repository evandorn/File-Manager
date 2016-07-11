import os
import sys
import Tkinter as tk

class Observable:
  def __init__(self, initValue = None):
    self.data = initValue
    self.callbacks = {}

  def addCallback(self, func):
    self.callbacks[func] = 1

  def delCallback(self, func):
    del self.callback[func]

  def _docallbacks(self):
    for func in self.callbacks:
      func(self.data)

  def set(self, data):
    self.data = data
    self._docallbacks()

  def get(self):
    return self.data

  def unset(self):
    self.data = None

class Model(object):

  def __init__(self):
    self.hits = Observable([])
    self.directory = Observable(os.getcwd())

  def clear(self):
    self.setHits([])
  
# UNUSED AS OF YET, WILL BE MADE FUNCTIONAL LATER
  def newDir(self, newDirectory):
    self.directory = newDirectory

  def setHits(self, newHits):
    self.hits.set(newHits)

  def getDir(self):
    return self.directory.get()
