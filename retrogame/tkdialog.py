# This file is part of Stoneworks (Sishya Hacks D.A.V.).

# Stoneworks (Sishya Hacks D.A.V.) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Stoneworks (Sishya Hacks D.A.V.) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Stoneworks (Sishya Hacks D.A.V.).  If not, see <https://www.gnu.org/licenses/>.

import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

from retrogame.score_tracker import Score
from retrogame.pygamediag import main as pygamemain

scor_track = Score()

class Menu(Tk):
    def placeTopics(self, back, lab):
        back.place(x=0, y=0)
        lab.place(x=175, y=10)
    
    def __init__(self):
        """Menu
        
        This class provides a menu to work with the application. It 
        displays the highscore, as well as relevant buttons.
        """
        super().__init__()
        self.geometry("700x500")
        self.title("Stoneworks")
        
        self.menu_icon = tkinter.PhotoImage(file="img/menu-icon.png")
        self.background = PhotoImage(file="img/background.png")
        self.iconphoto(False,self.menu_icon)
        self.bg_label = Label(self,image=self.background)
        self.topic = Label(self,text="StoneWorks - 2022",font=("Arial",30),borderwidth=3,relief=SUNKEN)

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

class InstructionLevel(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Instructions Page")
        self.geometry("700x300")

        self.arrl = tk.PhotoImage(file="img/arrow-left.png")
        self.arrr = tk.PhotoImage(file="img/arrow-right.png")
        self.apple = tk.PhotoImage(file="img/apple.png")
        self.heart = tk.PhotoImage(file="img/heart.png")
        self.stone1 = tk.PhotoImage(file="img/stone.png")
        self.stone2 = tk.PhotoImage(file="img/stone2.png")

        self.label1img = tk.Label(self,image=self.arrl)
        self.label2img = tk.Label(self,image=self.arrr)
        self.label3img1 = tk.Label(self,image=self.apple)
        self.label3img2 = tk.Label(self,image=self.heart)
        self.label4img1 = tk.Label(self,image=self.stone1)
        self.label4img2 = tk.Label(self,image=self.stone2)

        self.label0 = tk.Label(self)
        self.toplbl = tk.Label(self)
        self.botlbl = tk.Label(self)
        self.label1 = tk.Label(self,text="1 - Press left arrow to move bob left",font=("Arial",20))
        self.label2 = tk.Label(self,text="2 - Press right arrow to move bob right",font=("Arial",20))
        self.label3 = tk.Label(self,text="3 - Collect apples to gain points and hearts to gain lives",font=("Arial",20))
        self.label4 = tk.Label(self,text="4 - You will lose a life when a stone falls on you!",font=("Arial",20))
        self.label5 = tk.Label(self,text="5 - You will start with 3 lives at the beginning",font=("Arial",20))
        self.label6 = tk.Label(self)

        self.label0.grid(row=0, column=0, rowspan=5)
        self.label0.grid(row=0, column=4, rowspan=5)
        self.toplbl.grid(row=0, column=0, columnspan=5)
        self.botlbl.grid(row=6, column=0, columnspan=5)
        self.label1.grid(row=1, column=3,sticky="w")
        self.label2.grid(row=2, column=3,sticky="w")
        self.label3.grid(row=3, column=3,sticky="w")
        self.label4.grid(row=4, column=3,sticky="w")
        self.label5.grid(row=5, column=3,sticky="w")
        self.label1img.grid(row=1, column=1,columnspan=2)
        self.label2img.grid(row=2, column=1,columnspan=2)
        self.label3img1.grid(row=3,column=1)
        self.label3img2.grid(row=3,column=2)
        self.label4img1.grid(row=4,column=1)
        self.label4img2.grid(row=4,column=2)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 6, weight=1)


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
