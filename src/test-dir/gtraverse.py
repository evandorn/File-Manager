import os
import sys
import Tkinter as tk

GEOMETRY = '640x480+400+400'

# Observable was shamelessly taken from the Toy MVC in the project spec
class Observable:
  def __init__(self, initValue=None):
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

class View(tk.Toplevel):
  def __init__(self, master):
    tk.Toplevel.__init__(self, master)
    self.protocol('WM_DELETE_WINDOW', self.master.destroy)
    self.geometry(GEOMETRY)
    label = tk.Label(self, text = "Graphical file locator")
    label.pack()
    topFrame = tk.Frame(self)
    self.fileList = tk.Listbox(topFrame, width = 70, height = 25)
    self.fileList.pack()
    bottomFrame = tk.Frame(self, height = 8)
    bottomFrame.pack(side = tk.BOTTOM)
    topFrame.pack()
    scrollbar = tk.Scrollbar(topFrame, orient = tk.HORIZONTAL)
    scrollbar.pack(side = tk.BOTTOM, fill = tk.X)
    self.fileList.config(xscrollcommand = scrollbar.set)
    scrollbar.config(command = self.fileList.xview)
    self.entryBox = tk.Entry(bottomFrame, width = 32)
    self.entryBox.pack(side = tk.LEFT)
    self.searchButton = tk.Button(bottomFrame, text = "Search")
    self.searchButton.config(width = 6, height = 2, bg = '#00FF00', bd = 3)
    self.searchButton.pack(side = tk.LEFT, padx = 5)
    self.clearButton = tk.Button(bottomFrame, text = "Clear list")
    self.clearButton.config(width = 6, height = 2, bg = '#FFFF00', bd = 3)
    self.clearButton.pack(side = tk.LEFT, padx = 5)
    self.quitButton = tk.Button(bottomFrame, text = "Quit")
    self.quitButton.config(width = 6, height = 2, bg = '#FF0000', bd = 3)
    self.quitButton.pack(side = tk.LEFT, padx = 5)

  def updateHits(self, newHits):
    self.fileList.delete(0,tk.END)
    for h in newHits:
      self.fileList.insert(tk.END,h)
    
  def clearEntry(self, event):
    self.entryBox.delete(0,tk.END)

  def setEntry(self, text):
    self.entryBox.insert(0,text)

  def bindEntry(self, cmd, handler):
    self.entryBox.bind(cmd, handler)

  def getEntry(self):
    return self.entryBox.get()

class Controller(object):
  def __init__(self, root):
    self.model = Model()
    self.model.hits.addCallback(self.hitsChanged)
    self.view = View(root)
    self.view.bind("<Escape>", lambda event: root.quit())
    self.view.setEntry("<Enter search term here>")
    self.view.bindEntry("<Escape>", self.view.clearEntry)
    self.view.bindEntry("<Return>", self.searchModel)
    self.view.clearButton.config(command = self.clear)
    self.view.searchButton.config(command = self.searchModel)
    self.view.quitButton.config(command = root.quit)
  
  def hitsChanged(self, hits):
    self.view.updateHits(hits)

  def entryChanged(self,entry):
    pass

  def clear(self):
    self.model.clear()
    
  def searchModel(self, event = None):
    self.model.clear()
    part = self.view.getEntry()
    subdirs = [self.model.getDir()]
    tempHits = []
    while subdirs:
      dirToSearch = subdirs.pop()
      thisDirectory = os.listdir(dirToSearch)
      for i in thisDirectory:
        toPush = os.path.join(dirToSearch, i)

        if os.path.isdir(toPush):
          subdirs.append(toPush)
          
        if part in i:
	  tempHits.append(toPush)
      
      self.view.updateHits(tempHits)

if __name__ == '__main__':
  root = tk.Tk()
  root.withdraw()
  main = Controller(root)
  root.mainloop()
