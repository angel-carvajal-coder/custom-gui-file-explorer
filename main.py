import os
from tkinter import *

class App(Tk):
    def __init__(self, master):
        self.master = master

        sidebar = Frame(master)
        # sidebar.size = "50x500"
        sidebar.grid(row=0, column=0)

        self.sidebar = sidebar

        os.chdir(os.environ["USER" if os.name != "nt" else "userprofile"])

        for folderOrFile in os.listdir():
            print(f'[{"DIR" if os.path.isdir(os.path.join(os.getcwd(), folderOrFile)) else "FILE"}] ', end=f"{folderOrFile}\n")


root = Tk()
app = App(root)
root.wm_title("File explorer")
root.geometry("1000x500")
root.mainloop()
