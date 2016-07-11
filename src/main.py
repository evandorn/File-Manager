#!/usr/bin/python

import sys
import Tkinter as tkinter
import FileManagerView

# I think this is the correct way to write main
if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.withdraw()
    screen.title("File Manager")
    app = FileManagerView.FileManagerView(screen)
    screen.mainloop()
