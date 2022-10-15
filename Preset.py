from tkinter import *
from Game import Game

class Preset(object):


    def buildStartWindow(self, window):
        self.title_label = Label(window, text = "Enter the game size. Format: \"NxN\" ")
        self.title_label.pack()

        self.game_size = Entry(window)
        self.game_size.pack()
        self.game_size.insert(0, "30x45")

        self.rule_label = Label(window, text = "Enter the rule of the game. Format: N/N, for example 123/456")
        self.rule_label.pack()

        self.game_rule = Entry(window)
        self.game_rule.pack()
        self.game_rule.insert(0, "23/3")

        self.start_button = Button(window, text = "Start the game", command = lambda:self.startGame(window) )
        self.start_button.pack(pady = 10)


    def createGame(self, window):
        self.game_iteration = Game(self.x, self.y, self.rule, window)
        self.game_iteration.buildWindow()
        self.game_iteration.createCells()
        self.game_iteration.buildMenu()


    def forgetStartWindow(self):
        self.title_label.pack_forget()
        self.start_button.pack_forget()
        self.game_size.pack_forget()
        self.game_rule.pack_forget()
        self.rule_label.pack_forget()


    def isXY(self):
        size = str(self.game_size.get())
        size = size.split("x")
        try:
            self.y = int(size[0])
            self.x = int(size[1])
        except:
            messagebox.showerror("Error!", "Bad format of the game size!!")
            return 0
        if self.y<1 or self.x<1:
            messagebox.showerror("Error!", "Bad format of the game size!!")
            return 0
        return 1


    def isRule(self):
        rule = str(self.game_rule.get())
        self.rule = rule.split("/")
        try:
            z = int(self.rule[0])
            w = int(self.rule[1])
        except:
            if self.rule[0] and self.rule[1] != "":
                messagebox.showerror("Error!", "Bad format of the rules!!")
                return
        for c in self.rule[0]:
            if c == " ":
                messagebox.showerror("Error!", "Delete spaces in the rule format!!")
                return 0
        for c in self.rule[1]:
            if c == " ":
                messagebox.showerror("Error!", "Delete spaces in the rule format!!")
                return 0
        return 1


    def startGame(self, window):
        if self.isXY():
            if self.isRule():
                self.forgetStartWindow()
                self.createGame(window)
