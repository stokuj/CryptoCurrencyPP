
import tkinter as tk
from tkinter import messagebox
##
from model import Model
from view  import View
##


class Controller():
    """ Controller class
    """
    def __init__(self):
        """ Initialization of model, view and root of tkinter
        """
        Model(self)
        self.m= Model(self)
        root = tk.Tk()
        View(root,self)
        root.mainloop()

    def do_train(self):
        """ Simple function to do training
        """
        self.m.train()
        
    def do_plot(self):
        """ Simple function to preform plot after training
        """
        if( self.m.ready_to_do_plot == True):
            self.m.plot()
        else:
            messagebox.showwarning(title='Wrong Button!', message='U need to train first')
        
    def do_gain(self):
        """ Simple function that calls gain from model and next shows it using messagebox
        """
        gain = self.m.gain()

        messagebox.showinfo(title='Gain', message='Current value is ' + str(int(gain)) +'% of staring value\n'
                            +   '100% - Gain is equal: ' + str(100-int(gain)) +'%\n'    )

    def set_model_currency(self,i):
        self.m.set_currency(i)

    def set_model_data_source(self,i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_data_source(i)

    def set_model_model_ID(self,i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_model_id(i)

    def set_model_file_path(self, p):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_file_path(p)

    def set_model_switch_state(self, i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_switch_state(i)
        
    def set_model_predition_days(self,i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_predition_days(i)
        
    def set_model_future_days(self, i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_future_days(i)
        
    def set_model_test_start_date(self, i):
        """ Simple function that passes int variable to model function

        Args:
            i (int): Variable to pass to model function
        """
        self.m.set_test_start_date(i)

        

if __name__ == "__main__":
    c = Controller()