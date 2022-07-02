from tkinter import *

class InstructionLevel(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.title("Instructions Page")
        self.geometry("500x500")
        self.icon = PhotoImage(r"menu-icon.png")
        self.iconphoto(False,self.icon)
        self.arrow1 = PhotoImage(r"arrow-left.png")
        self.arrow2 = PhotoImage(r"arrow-right.png")
        Label(text="Press the left arrow to move bob left ",image=self.arrow1).pack()
        Label(text="Press the right arrow to move bob right ", image=self.arrow2).pack()

app = Tk()
inst = InstructionLevel(app)
app.mainloop()
