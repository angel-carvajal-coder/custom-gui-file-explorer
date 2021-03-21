from tkinter import *

class App(Tk):
    def __init__(self, master):
        self.master = master
        # self.title = "File explorer"

root = Tk()
app = App(root)
root.wm_title("File explorer")
root.geometry("1000x500")
root.mainloop()
