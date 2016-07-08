"""
    FileManegerController.py
    
    Created by: Evan Dorn
    Created on: 7/5/16
"""

import sys, os
import FileManagerModel
import FileManagerView

class FileManagerController(object):
    def __init__(self):
        self.model = FileManagerModel.FileManagerModel()
        self.view  = FileManagerView.FileManagerView()

if __name__ == "__main__":
    controller = FileManagerController()
