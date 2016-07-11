#!/usr/bin/python

import sys, os
import Tkinter as tkinter
import src.FileManagerController

if __name__ == '__main__':
  screen = tkinter.Tk()
  screen.withdraw()
  screen.title("File Manager")
  app = src.FileManagerController.FileManagerController(screen)
  screen.mainloop()
