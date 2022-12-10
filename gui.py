from tkinter import *
from shapes import area
from shapes import perimeter
import csv

class GUI:
    def __init__(self, window):
        self.window = window
        
        # radio buttons one
        self.rad1 = StringVar(value='None')
        self.frame_ap = Frame(self.window)
        self.label_ap = Label(self.frame_ap, text='Area/Perimeter?').pack(padx=5, side='left')
        self.radio_area = Radiobutton(self.frame_ap, text="Area", variable=self.rad1, value='Area').pack(padx=5, side='left')
        self.radio_perimeter = Radiobutton(self.frame_ap, text="Perimeter", variable=self.rad1, value='Perimeter').pack(padx=5, side='left')
        self.frame_ap.pack(anchor='w', pady=10)
        
        #radio buttons two: electric boogaloo
        self.rad2 = StringVar(value='None')
        self.frame_shape = Frame(self.window)
        self.label_shape = Label(self.frame_shape, text='Status')
        self.radio_circle = Radiobutton(self.frame_shape, text="Circle", variable=self.rad2, value='Circle').pack(padx=5, side='left')
        self.radio_rectangle = Radiobutton(self.frame_shape, text="Rectangle", variable=self.rad2, value='Rectangle').pack(padx=5, side='left')
        self.radio_square = Radiobutton(self.frame_shape, text="Square", variable=self.rad2, value='Square').pack(padx=5, side='left')
        self.radio_triangle = Radiobutton(self.frame_shape, text="Triangle", variable=self.rad2, value='Triangle').pack(padx=5, side='left')
        self.frame_shape.pack(anchor='w', pady=10)
        
        # save button
        self.button_save = Button(self.window, text = 'Select', command = self.clicked).pack()
    
    def clicked(self):
        print('debug: button clicked')
        self.ap_choice = self.rad1.get()
        self.shape_choice = self.rad2.get()
        
        self.top = Toplevel()
        self.top.geometry('400x275')
        self.top.resizable(False, False)
        
        if self.shape_choice == 'Circle':
            self.top.title(f'Circle {self.ap_choice}')
            self.frame_top = Frame(self.top)
            self.label_top = Label(self.top, text='Enter radius:').pack()
            self.entry_radius = Entry(self.top)
            self.entry_radius.pack()
            self.label_calc = Label(self.top, text=' ')
            self.label_calc.pack()
            
            def calculate():
                try:
                    self.radius = float(self.entry_radius.get().strip())
                    if self.ap_choice == 'Area':
                        self.result = area.circle(self.radius)
                    elif self.ap_choice == 'Perimeter':
                        self.result = perimeter.circle(self.radius)
                    
                    self.label_calc.config(text = f'Output = {self.result:.2f}', fg = 'black')
                except ValueError:
                    self.label_calc.config(text='Please enter numeric values', fg = 'red')
        
        elif self.shape_choice == 'Rectangle':
            self.top.title(f'Rectangle {self.ap_choice}')
            self.frame_top = Frame(self.top)
            self.label_top1 = Label(self.top, text='Enter side 1 length:').pack()
            self.entry_side1 = Entry(self.top)
            self.entry_side1.pack()
            self.label_top2 = Label(self.top, text='Enter side 2 length:').pack()
            self.entry_side2 = Entry(self.top)
            self.entry_side2.pack()
            self.label_calc = Label(self.top, text=' ')
            self.label_calc.pack()
            
            def calculate():
                try:
                    self.side1 = float(self.entry_side1.get().strip())
                    self.side2 = float(self.entry_side2.get().strip())
                    if self.ap_choice == 'Area':
                        self.result = area.rectangle(self.side1,self.side2)
                    elif self.ap_choice == 'Perimeter':
                        self.result = perimeter.rectangle(self.side1,self.side2)
                    
                    self.label_calc.config(text = f'Output = {self.result:.2f}', fg = 'black')
                except ValueError:
                    self.label_calc.config(text='Please enter numeric values', fg = 'red')
            
        elif self.shape_choice == 'Square':
            self.top.title(f'Square {self.ap_choice}')
            self.frame_top = Frame(self.top)
            self.label_top = Label(self.top, text='Enter side length:').pack()
            self.entry_side = Entry(self.top)
            self.entry_side.pack()
            self.label_calc = Label(self.top, text=' ')
            self.label_calc.pack()
            
            def calculate():
                try:
                    self.side = float(self.entry_side.get().strip())
                    if self.ap_choice == 'Area':
                        self.result = area.square(self.side)
                    elif self.ap_choice == 'Perimeter':
                        self.result = perimeter.square(self.side)
                    
                    self.label_calc.config(text = f'Output = {self.result:.2f}', fg = 'black')
                except ValueError:
                    self.label_calc.config(text='Please enter numeric values', fg = 'red')
                
        elif self.shape_choice == 'Triangle' and self.ap_choice == 'Area':
            self.top.title(f'Triangle {self.ap_choice}')
            self.frame_top = Frame(self.top)
            self.label_top1 = Label(self.top, text='Enter base length:').pack()
            self.entry_base = Entry(self.top)
            self.entry_base.pack()
            self.label_top2 = Label(self.top, text='Enter height:').pack()
            self.entry_height = Entry(self.top)
            self.entry_height.pack()
            self.label_calc = Label(self.top, text=' ')
            self.label_calc.pack()
            
            def calculate():
                try:
                    self.base = float(self.entry_base.get().strip())
                    self.height = float(self.entry_height.get().strip())
                    
                    self.result = area.triangle(self.base,self.height)
                    
                    self.label_calc.config(text = f'Output = {self.result:.2f}', fg = 'black')
                except ValueError:
                    self.label_calc.config(text='Please enter numeric values', fg = 'red')
        
        elif self.shape_choice == 'Triangle' and self.ap_choice == 'Perimeter':
            self.top.title(f'Triangle {self.ap_choice}')
            self.frame_top = Frame(self.top)
            self.label_top1 = Label(self.top, text='Enter side 1 length:').pack()
            self.entry_side1 = Entry(self.top)
            self.entry_side1.pack()
            self.label_top2 = Label(self.top, text='Enter side 2 length:').pack()
            self.entry_side2 = Entry(self.top)
            self.entry_side2.pack()
            self.label_top3 = Label(self.top, text='Enter side 3 length:').pack()
            self.entry_side3 = Entry(self.top)
            self.entry_side3.pack()
            self.label_calc = Label(self.top, text=' ')
            self.label_calc.pack()
            
            def calculate():
                try:
                    self.side1 = float(self.entry_side1.get().strip())
                    self.side2 = float(self.entry_side2.get().strip())
                    self.side3 = float(self.entry_side3.get().strip())
                    
                    self.result = perimeter.triangle(self.side1, self.side2, self.side3)
                    
                    self.label_calc.config(text = f'Output = {self.result:.2f}', fg = 'black')
                except ValueError:
                    self.label_calc.config(text='Please enter numeric values', fg = 'red')
        
        self.calc_ulate = Button(self.top,text= "Calculate", command=calculate).pack(pady= 5,side=TOP)
        self.rad1.set('None')
        self.rad2.set('None')
