
import tkinter as tk

##
from model import Model
from view  import View
##


class Controller():
    def __init__(self):
        Model()
        root = tk.Tk()
        View(root,self)

        root.mainloop()
    m = Model()
    def test(self):
        Model.Alert()

    def do_train(self):

        self.m.train()

    def do_plot(self):

        self.m.plot()


    def setModelCurrency(self,i):
        self.m.setCurrency(i)

    def setModelDataSource(self,i):
        self.m.setDataSource(i)

    def setModelModelID(self,i):
        self.m.setModelId(i)

    def setModelFilePath(self, p):
        self.m.setFilePath(p)

    def setMoeldSwitchState(self, i):
        self.m.setSwitchState(i)
        
    def setModelPreditionDays(self,i):
        self.m.setPreditionDays(i)

if __name__ == "__main__":
    c = Controller()