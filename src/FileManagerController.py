"""
    FileManegerController.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import sys, os
import FileManagerModel
import FileManagerView

class FileManagerController(object):
    def __init__(self, screen):
        self.model = FileManagerModel.FileManagerModel()
        self.model.hits.addCallback(self.hitsChanged)                   # change these variable names
        self.view  = FileManagerView.FileManagerView(screen)            # pass the screen to the view
        # Key bindings
        self.view.bind("<Escape>", lambda event: root.quit())
        self.view.setEntry("<Enter search term here>")
        self.view.bindEntry("<Button-1>", self.view.clearEntry)
        self.view.bindEntry("<Return>", self.searchModel)
        # Button bindings
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
                tempHits.append(toPush)     # I think this spacing is correct
      
            self.view.updateHits(tempHits)

if __name__ == "__main__":
    controller = FileManagerController()
