#!/usr/bin/python

import sys
import Tkinter as tkinter
import src.FileManagerView

# I think this is the correct way to write main
if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.withdraw()
    screen.title("File Manager")
    app = src.FileManagerView.FileManagerView(screen)
    screen.mainloop()
