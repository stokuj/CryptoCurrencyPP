import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox



class View():
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        root.title('Cryptocurrency Price Prediction')

        window_height = 520
        window_width = 480
        def center_screen():
            """ gets the coordinates of the center of the screen """
            global screen_height, screen_width, x_cordinate, y_cordinate

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        center_screen()

        style = ttk.Style(root)
        root.tk.call('source', 'azure.tcl')
        style.theme_use('azure')

        options = ['', 'OptionMenu', 'Value 1', 'Value 2']
        currency_type = tk.IntVar()
        currency_type.set(1)
        b = tk.IntVar()
        b.set(1)
        c = tk.IntVar()
        data_source = tk.IntVar()
        data_source.set(1)
        e = tk.StringVar()
        e.set(options[1])
        f = tk.IntVar()

        prediction_days = tk.IntVar()
        prediction_days.set(30)

        switch_state = tk.IntVar()
        model_id = tk.IntVar()
        model_id.set(1)

        frame1 = ttk.LabelFrame(root, text='Select Currency', width=210, height=200)
        frame1.place(x=20, y=12)

        frame2 = ttk.LabelFrame(root, text='Online Source', width=210, height=160)
        frame2.place(x=20, y=252)


        frame3 = ttk.LabelFrame(root, text='Select Model', width=210, height=160)
        frame3.place(x=250, y=252)

        check1 = ttk.Radiobutton(frame1, text='BTC', variable=currency_type, value=1)
        check1.place(x=20, y=20)
        check2 = ttk.Radiobutton(frame1, text='ETH', variable=currency_type, value=2)
        check2.place(x=20, y=60)
        check3 = ttk.Radiobutton(frame1, text='Doge', variable=currency_type, value=3)
        check3.place(x=20, y=100)
        check4 = ttk.Radiobutton(frame1, text='LTC', variable=currency_type, value=4)
        check4.place(x=20, y=140)

        radio1 = ttk.Radiobutton(frame2, text='Yahoo', variable=data_source, value=1)
        radio1.place(x=20, y=20)
        radio2 = ttk.Radiobutton(frame2, text='Stooq', variable=data_source, value=2)
        radio2.place(x=20, y=60)
        radio3 = ttk.Radiobutton(frame2, text='Naver', variable=data_source, value=3)
        radio3.place(x=20, y=100)

        radio4 = ttk.Radiobutton(frame3, text='MODEL1', variable=model_id, value=1)
        radio4.place(x=20, y=20)
        radio5 = ttk.Radiobutton(frame3, text='MODEL2', variable=model_id, value=2)
        radio5.place(x=20, y=60)
        radio6 = ttk.Radiobutton(frame3, text='MODEL3', variable=model_id, value=3)
        radio6.place(x=20, y=100)

        
        def callback_button1():
            filename = fd.askopenfilename()
            laber = ttk.Label(root, text = filename)
            laber.place(x=120, y=425)
            self.controller.setModelFilePath(filename)


        button1 = ttk.Button(root, text='Select file', command=callback_button1)
        button1.place(x=20, y=430)

        def callback_button2():
            self.controller.setModelCurrency(currency_type.get())
            self.controller.setModelDataSource(data_source.get())
            self.controller.setModelModelID(model_id.get())
            self.controller.setMoeldSwitchState(switch_state.get())
            self.controller.setModelPreditionDays(prediction_days.get())
            self.controller.do_train()

        button2 = ttk.Button(root, text='Train', command = callback_button2)
        button2.place(x=20, y=480)

        def callback_button3():
            self.controller.do_plot()

        button3 = ttk.Button(root, text='Plot', command = callback_button3)
        button3.place(x=120, y=480)

        def scale(i):
            prediction_days.set(int(scale.get()))
            value_label.configure(text=get_current_value())

        scale = ttk.Scale(root, from_=1, to=100, variable=prediction_days, command=scale)
        scale.place(x=250, y=20)

        progress = ttk.Progressbar(root, value=1, variable=prediction_days, mode='determinate')
        progress.place(x=250, y=60)

        value_label = ttk.Label( root, text = 'Based on 30 days')
        value_label.place(x=375, y=40)


        switch = ttk.Checkbutton(root, text='Use online database', style='Switch', variable=switch_state, offvalue=0, onvalue=1)
        switch.place(x=250, y=100)
        switch.invoke()

        size = ttk.Sizegrip(root)
        size.place(x=780, y=510)




        spin1 = ttk.Spinbox(root, from_= 1, to=10, increment=1)
        spin1.place(x=250, y=140)
        spin1.insert(0, 'Future days')


        spin2 = ttk.Spinbox(root, from_= 20, to=100, increment=5)
        spin2.place(x=250, y=180)
        spin2.insert(0, 'Plot range')

        sep1 = ttk.Separator()
        sep1.place(x=20, y=235, width=210)

        sep2 = ttk.Separator()
        sep2.place(x=250, y=235, width=210)

        def get_current_value():
            return ' Based on {: .0f}days'.format(prediction_days.get())

