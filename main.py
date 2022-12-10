from gui import *

def main():

    window = Tk()
    window.title('Calculator')
    window.resizable(False, False)
    window.geometry('400x200')
    widgets = GUI(window)
    window.mainloop()
    
if __name__ == '__main__':
    main()
