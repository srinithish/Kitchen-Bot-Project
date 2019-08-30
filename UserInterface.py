# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
#        self.pack()
        
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        
        ### hi button
        self.startRobotBtn = tk.Button(self)
        self.startRobotBtn["text"] = "Start Robot"
        self.startRobotBtn["command"] = self.say_hi
#        self.hi_there.pack(side="left")
        self.startRobotBtn.grid(row = 0,column = 0)
        
        ## 
        
        self.pickUpSauceBtn = tk.Button(self)
        self.pickUpSauceBtn["text"] = "Pick up sauce"
        self.pickUpSauceBtn["command"] = self.say_hi
        self.pickUpSauceBtn.grid(row = 0,column = 1)       
#        self.hi.pack(side="top")
        
        
        
        self.spreadSauce = tk.Button(self)
        self.spreadSauce["text"] = "spread sauce"
        self.spreadSauce["command"] = self.say_hi
        self.spreadSauce.grid(row = 1,column = 0) 
        
        ## quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        
        
        self.quit.grid(row = 1,column = 1)
#        self.quit.pack(side="right")
        

        
        
        
        ## message button:
        
        
        self.currAction = tk.Label()
        self.currAction["text"] = "Hello"
        self.currAction.grid(row = 2,column = 0)
        
        
    def say_hi(self):
        self.currAction["text"] = 'You pressed a button'
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()