from tkinter import *



class Square:
    

    def __init__ (self, frame, x, y, expected_value = 0 ):
        self.var = IntVar()
        self.cell = Checkbutton(frame, variable = self.var, width = 0, height = 0, bd=0, padx = 0, pady = 0, selectcolor="white", activeforeground="white", command = self.setColor)
        self.operation_value = 0
        self.expected_value = expected_value
        self.x = x
        self.y = y


    def showCell(self):
        self.cell.grid(row = self.y, column = self.x)


    def setColor(self):
        if self.var.get() == 1:
            self.cell["selectcolor"] = "black"
            return
        self.cell["selectcolor"] = "white"


    def changeValue(self):
        self.var.set(self.expected_value )
        self.setColor()


    def changeValueS(self):
        self.operation_value = self.expected_value 
             

    
