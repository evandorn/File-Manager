import os
import sys
import Tkinter as tk

GEOMETRY = '640x480+400+400'

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

if __name__ == '__main__':
    screen = tk.Tk()
    screen.withdraw()
    fileManager = View(screen)
    screen.mainloop()
