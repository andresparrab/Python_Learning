from tkinter import *
from PIL import Image, ImageTk
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title('My GUI')
        self.pack(fill=BOTH, expand= 1)
        '''Here we make a quit button'''
        #quitButton = Button(self, text = 'Quit', command = self.client_exit)
        #quitButton.place(x=0,y=0)

        '''We are going to make a menu'''
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label = 'Save', command= self.client_exit)
        file.add_command(label = 'Exit', command=self.client_print_text)
        file.add_command(label = 'Exit', command=self.client_exit)
        menu.add_cascade(label = 'File', menu=file)

        edit = Menu(menu)
        edit.add_command(label = 'Show Image', command = self.showImg
                         )
        edit.add_command(label = 'Show Text', command = self.showTxt)
        menu.add_cascade(label ='Edit',menu=edit)

    def showImg(self):
        load = Image.open('/home/doctor/Pictures/141784.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image= render)
        img.image = render
        img.place(x=0,y=0)


    def showTxt(self):
        text = Label(self, text = 'Hej there handsome!')
        text.pack()


    def client_exit(self):
        exit()

    def client_print_text(self):
        print('Whatsapp Bitches')


root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()