import os
from tkinter import *

labels = []

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

        self.renderFilesAndDirectories()

    def renderFilesAndDirectories(self):
        global labels
        for label in labels:
            label.destroy()
        labels = []
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
        labels.append(label)
        label.grid(row=self.directoryIndex, column=0)
        label.bind('<Button-1>', self.generateFolderClickHandler(folder))

    def generateFolderClickHandler(self, folder):
        def handler(_):
            os.chdir(folder)
            print('User clicked on directory:', folder)
            self.renderFilesAndDirectories()
        return handler

    def renderFile(self, file):
        print(f"[FILE] {file}")
        label = Label(self.mainPart, text=file)
        labels.append(label)
        label.grid(row=self.currentFileIndex, column=0)

root = Tk()
app = App(root)
root.wm_title("File explorer")
root.geometry("1000x500")
root.mainloop()
