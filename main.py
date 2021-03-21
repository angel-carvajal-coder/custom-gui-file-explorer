import os
from tkinter import *

class App(Tk):
    def __init__(self, master):
        self.master = master

        sidebar = Frame(master)
        # sidebar.size = "50x500"
        sidebar.grid(row=0, column=0)

        mainPart = Frame(master)
        mainPart.grid(row=0, column=1)

        self.sidebar = sidebar
        self.mainPart = mainPart

        os.chdir(os.environ["USER" if os.name != "nt" else "userprofile"])

        self.directoryIndex = 0
        self.currentFileIndex = 0

        for folderOrFile in os.listdir():
            if os.path.isdir(folderOrFile):
                self.renderDirectory(folderOrFile)
                self.directoryIndex += 1
            else:
                self.renderFile(folderOrFile)
                self.currentFileIndex += 1

    def renderDirectory(self, folder):
        print(f"[DIR] {folder}")
        label = Label(self.sidebar, text=folder)
        label.grid(row=self.directoryIndex, column=0)

    def renderFile(self, file):
        print(f"[FILE] {file}")
        label = Label(self.mainPart, text=file)
        label.grid(row=self.currentFileIndex, column=1)

root = Tk()
app = App(root)
root.wm_title("File explorer")
root.geometry("1000x500")
root.mainloop()
