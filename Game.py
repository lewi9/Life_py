from tkinter import *
from Square import Square
from threading import Thread
from time import sleep

class Game(object):


    def __init__(self, x, y, rule = ["23", "3"], window = NONE):
        self.area = []
        self.rule = rule
        self.alive = str(rule[0])
        self.born = str(rule[1])
        self.x =  x
        self.y = y
        self.running = 0;
        self.main_window = window
        

    def buildWindow(self):
        self.game = LabelFrame(self.main_window, text = "game")
        self.game.grid(row = 0, column = 0)
        self.menu = LabelFrame(self.main_window, text = "menu")
        self.menu.grid(row = 0, column = 1, sticky = NW+S)


    def buildMenu(self):

        self.take_step = Button(self.menu, text="take a step", command = self.step, width = 10 )
        self.take_step.grid(row = 0, column = 0, pady = 5, sticky = W)

        self.x_steps = Entry(self.menu, width = 5)
        self.x_steps.grid(row = 1, column = 1, padx = 5)
        self.x_steps.insert(0, "5")

        self.take_x_steps = Button(self.menu, text = "take x steps", width = 10, command = lambda:self.stepS( self.x_steps.get() ))
        self.take_x_steps.grid(row = 1, column = 0, sticky = W)

        self.label0 = Label(self.menu, text = "entry time in s")
        self.label0.grid(row = 2, column = 0, columnspan = 2)
        self.label1 = Label(self.menu, text = "e.g. 0.3")
        self.label1.grid(row = 3, column = 0, columnspan = 2)

        self.time = Entry(self.menu, width = 5)
        self.time.grid(row=4, column = 1)
        self.time.insert(0, "0.250")

        self.start_button = Button(self.menu, text="start", width = 10, command = self.start)
        self.start_button.grid(row = 4, column = 0, sticky = W)

        self.stop_button = Button(self.menu, text="stop", width = 10, command = self.stop)


    def createCells(self):
        i=0
        j=0
        while(i < self.y):
            self.area.append( [] )
            while(j < self.x):
                self.area[i].append( Square( self.game, j, i ) )
                self.area[i][j].showCell()
                j+=1
            j=0
            i+=1


    def isDead(self, element, S=0):
        if self.alive == "":
                return 0
        counter = -1
        ru = element.y - 1
        rr = element.x + 1
        rd = element.y + 1
        rl = element.x - 1
    
        if ru < 0:
            ru = 0
        if rr >= self.x:
            rr = self.x-1
        if rd >= self.y:
            rd = self.y-1
        if rl < 0:
            rl = 0

        for i in range(ru, rd+1):
            for j in range(rl, rr+1):
                if S:
                    counter += self.area[i][j].operation_value
                else:
                    counter += self.area[i][j].var.get()
        for temp in self.alive:
            if temp == " ":
                continue
            if counter == int(temp):
                return 1

        return 0


    def isLive(self, element, S=0):
        if self.born == "":
            return 0
        counter = 0
        ru = element.y - 1
        rr = element.x + 1
        rd = element.y + 1
        rl = element.x - 1

        if ru < 0:
            ru = 0
        if rr >= self.x:
            rr = self.x-1
        if rd >= self.y:
            rd = self.y-1
        if rl < 0:
            rl = 0

        for i in range(ru, rd+1):
            for j in range(rl, rr+1):
                if S:
                    counter += self.area[i][j].operation_value
                else:
                    counter += self.area[i][j].var.get() 
        for temp in self.born:
            if temp == " ":
                continue
            if counter == int(temp):
                return 1

        return 0


    def step(self):
        for row in self.area:
            for element in row:
                condition = element.var.get()
                if condition==1:
                    element.expected_value = self.isDead(element)
                else:
                    element.expected_value = self.isLive(element)
        for row in self.area:
            for element in row:
                element.changeValue()       

    #Similar to step, but faster than using step x time for that. With that function, checkboxes don't uptade themselfs in every iteration
    def stepS(self, i):
        try:
            i = int(i)
        except:
            return
        for row in self.area:
            for element in row:
                element.operation_value = element.var.get()
        while(i>0):
            for row in self.area:
                for element in row:
                    condition = element.operation_value
                    if condition==1:
                        element.expected_value = self.isDead(element, 1)
                    else:
                        element.expected_value = self.isLive(element, 1)
            for row in self.area:
                for element in row:
                    element.changeValueS()
            i-=1
        for row in self.area:
            for element in row:
                 element.var.set( element.operation_value )
                 element.setColor()

    def isTime(self):
        try:
            self.action_time = float(self.time.get())
        except:
            return 0
        return 1

    def start(self):
        if self.isTime():
            self.time.grid_forget()
            self.start_button.grid_forget()
            self.stop_button.grid(row = 4, column = 0)
            self.running = 1
            t = Thread (target = self.going)
            t.start()

    def stop(self):
        self.running = 0
        self.stop_button.grid_forget()
        self.time.grid(row=4, column = 1)
        #self.time.insert(0, "250")
        self.start_button.grid(row = 4, column = 0, sticky = W)


    def going(self):
        while 1:
            self.step()
            if not self.running:
                return
            sleep(self.action_time)
            