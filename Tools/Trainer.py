"""Training Data Getter"""
import sys
sys.path.append("C:/Users/Gaurav/My Documents/GitHub/KineticEEG/KineticEEG")
import Preprocessers
import tkinter
import tkinter.ttk as tk
import EmotivDataGetter
import time
import csv
class TrainingCore:
    SENSORS_OF_INTEREST=["FC5","F3","F4","FC6"]
    def __init__(self):
        """It will get the training data like so;
        >>>max(window of ffted values)"""
        self.datagetter=EmotivDataGetter.EmotivDataGetter()
        self.interestingdata=dict()
        self.csvwrite
    def wait_window(self):
        """Wait for the arrival of the data"""
        window=self.datagetter.getwindowoffftdata(5)
        for g in SENSORS_OF_INTEREST:
             self.interestingdata.update({g:window[g]})
    def train_kick(self):
        self.wait_window()
        for c in self.interestingdata:
            maxa=max(c)
            del self.interestingdata[c]
            self.interestingdata[c]=maxa
        for z in self.interestingdata:
            
class TrainerApp(tkinter.Tk):
    def __init__(self, parent, TrainingCore):
        tkinter.Tk.__init__(self, parent)
        self.parent=parent
        self.minsize(width=400, height=400)
        self.maxsize(width=400, height=400)
        self.initialize()
    def train_kick(self):pass  
    def initialize(self):
        self.closebtn=tk.Button(self, text="close")
        self.closebtn.place(x=325,y=0)
        self.train_kickbtn=tk.Button(self, text="Train Kick", command=self.train_kick)
        self.train_kickbtn.place(x=120, y=100)
        self.train_armbtn=tk.Button(self, text="Train Arm")
        self.train_armbtn.place(x=200, y=100)
        self.train_nuetralbtn=tk.Button(self, text="Train Nuetral")
        self.train_nuetralbtn.place(x=160, y=130)
if __name__=='__main__':
    core=TrainingCore()
    app=TrainerApp(None,core)
    app.title("Trainer")
    app.mainloop()
