import tkinter
from tkinter import *
from retrogame.score_tracker import Score

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
    def destroy_menu(self):
        app.destroy()
    def __init__(self,root):
        super().__init__(root)
        self.quitButton = Button(self,text="Quit the Game  ",font=("Arial",20),borderwidth=5,relief=RIDGE,command=app.destroy)
        self.startButton = Button(self,text="Start new Game",font=("Arial",20),borderwidth=5,relief=RIDGE)
        self.highscore = scor_track.getScore()
        self.scoreboard = Label(self,text=f"Highscore : {self.highscore}",font=("Arial",20))
        self.__place_widgets()

    def __place_widgets(self):
        self.startButton.grid(row=1,column=0,sticky="NSEW")
        self.quitButton.grid(row=2,column=0,sticky="NSEW")
        self.scoreboard.grid(row=3,column=0,sticky="NSEW")

def main():
    app = Menu()
    buttons = ButtonFrame(app)
    buttons.place(x=230,y=170)
    return app

if __name__ == "__main__":
    app.mainloop()
