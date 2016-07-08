#!/usr/bin/python

import sys
import Tkinter as tkinter
import src.FileViewController

# I think this is the correct way to write main
if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.withdraw()
    app = src.FileViewController.FileViewController(screen)
    screen.mainloop()
