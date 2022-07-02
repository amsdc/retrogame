import tkinter
from tkinter import *
from tkinter import messagebox

from retrogame.score_tracker import Score
from retrogame.pygamediag import main as pygamemain

scor_track = Score()

class Menu(Tk):
    def placeTopics(self, back, lab):
        back.place(x=0, y=0)
        lab.place(x=80, y=10)
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        self.title("Retro Game")
        self.menu_icon = tkinter.PhotoImage(file="img/menu-icon.png")
        self.background = PhotoImage(file="img/background.png")
        self.iconphoto(False,self.menu_icon)
        self.bg_label = Label(self,image=self.background)
        self.topic = Label(self,text="Retro Game ! - ShishyaHacks",font=("Arial",30),borderwidth=3,relief=SUNKEN)

        self.placeTopics(self.bg_label,self.topic)

class ButtonFrame(Frame):
    def instructions(self):
        messagebox.showinfo("Instructions- Page", "LEFT ARROW - Move bob towards left\nRIGHT ARROW - Move bob towards\nCollect apples for points and hearts for more health\nAviod getting hit by stones!")

    def destroy_menu(self):
        self.root.destroy()
    def __init__(self,root):
        super().__init__(root)
        self.root = root
        self.quitButton = Button(self,text="Quit the Game  ",font=("Arial",20),borderwidth=5,relief=RIDGE,command=root.destroy)
        self.startButton = Button(self,text="Start new Game",font=("Arial",20),borderwidth=5,relief=RIDGE, command=self.open_game)
        self.helpButton = Button(self,text="Get Instructions",font=("Arial",20),borderwidth=5,relief=RIDGE,command=self.instructions)
        # self.highscore = scor_track.get_max_score()
        self.highscore = tkinter.StringVar(root, "Highscore: {}".format(scor_track.get_max_score()))
        self.scoreboard = Label(self,textvariable=self.highscore,font=("Arial",20))

        self.__place_widgets()

    def __place_widgets(self):
        self.startButton.grid(row=1,column=0,sticky="NSEW")
        self.quitButton.grid(row=2,column=0,sticky="NSEW")
        self.helpButton.grid(row=3,column=0,sticky="NSEW")
        self.scoreboard.grid(row=4,column=0,sticky="NSEW")

        
    def open_game(self):
        # self.root.deiconify()
        pygamemain()
        scor_track.close_file()
        scor_track.open_file()
        self.highscore.set("Highscore: {}".format(scor_track.get_max_score()))
        
        # self.root.withdraw()

import tkinter as tk
from tkinter import ttk

class InstructionLevel(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Instructions Page")
        self.geometry("700x300")
        self.arrl = tk.PhotoImage(file=r"arrow-left.png")
        self.arrr = tk.PhotoImage(file=r"arrow-right.png")
        self.apple = tk.PhotoImage(file=r"apple.png")
        self.heart = tk.PhotoImage(file=r"heart.png")
        self.stone1 = tk.PhotoImage(file=r"stone.png")
        self.stone2 = tk.PhotoImage(file=r"stone2.png")

        self.label1img = tk.Label(self,image=self.arrl)
        self.label2img = tk.Label(self,image=self.arrr)
        self.label3img1 = tk.Label(self,image=self.apple)
        self.label3img2 = tk.Label(self,image=self.heart)
        self.label4img1 = tk.Label(self,image=self.stone1)
        self.label4img2 = tk.Label(self,image=self.stone2)

        self.label0 = tk.Label(self)
        self.label1 = tk.Label(self,text="1 - Press left arrow to move bob left",font=("Arial",20))
        self.label2 = tk.Label(self,text="2 - Press right arrow to move bob right",font=("Arial",20))
        self.label3 = tk.Label(self,text="3 - Collect apples to gain points and hearts to gain lives",font=("Arial",20))
        self.label4 = tk.Label(self,text="4 - You will lose a life when a stone falls on you!",font=("Arial",20))
        self.label5 = tk.Label(self,text="5 - You will start with 3 lives at the beginning",font=("Arial",20))
        self.label6 = tk.Label(self)

        self.label0.grid(row=0, column=0, rowspan=5)
        self.label0.grid(row=0, column=4, rowspan=5)
        self.label1.grid(row=0, column=3,sticky="w")
        self.label2.grid(row=1, column=3,sticky="w")
        self.label3.grid(row=2, column=3,sticky="w")
        self.label4.grid(row=3, column=3,sticky="w")
        self.label5.grid(row=4, column=3,sticky="w")
        self.label1img.grid(row=0, column=1,columnspan=2)
        self.label2img.grid(row=1, column=1,columnspan=2)
        self.label3img1.grid(row=2,column=1)
        self.label3img2.grid(row=2,column=2)
        self.label4img1.grid(row=3,column=1)
        self.label4img2.grid(row=3,column=2)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)


app = tk.Tk()
inst = InstructionLevel(app)
app.mainloop()


def main():
    app = Menu()
    buttons = ButtonFrame(app)
    buttons.place(x=230,y=100)
    app.mainloop()
    return app

if __name__ == "__main__":
    app.mainloop()
