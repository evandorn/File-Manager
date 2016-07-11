#!/usr/bin/python

import sys, os
import Tkinter as tkinter
import FileManagerController

if __name__ == '__main__':
  screen = tkinter.Tk()
  screen.withdraw()
  screen.title("File Manager")
  app = FileManagerController.FileManagerController(screen)
  screen.mainloop()
