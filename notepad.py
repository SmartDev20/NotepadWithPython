import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # Set Icon :

        try:
            self.__root.wm_iconbitmap("notepad.ico")
        except:
            pass
        # Set window size (the default is 300x300) and title
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        self.__root.title('Untitled -Notepad')

        # To center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # To make the textarea auto resizable
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label='New', command=self.__newFile)
        self.__thisFileMenu.add_command(label='Open', command=self.__openFile)
        self.__thisFileMenu.add_command(label='Save', command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label='Exit', command=self.__quitApp)
        self.__thisMenuBar.add_cascade(label='File', menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label='Cut', command=self.__cut)
        self.__thisEditMenu.add_command(label='Copy', command=self.__copy)
        self.__thisEditMenu.add_command(label='Past', command=self.__past)
        self.__thisMenuBar.add_cascade(label='Edit', menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label='About', command=self.__help)
        self.__thisMenuBar.add_cascade(label='Help', menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview())
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApp(self):
        self.__root.destroy()

    def __help(self):
        showinfo('Notepad', 'First Version By Nabih')

    def __newFile(self):
        self.__root.title('Untitled   Notepad')
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __openFile(self):
        self.__file = askopenfilename(defaultextension='.txt', filetypes=[('All files', '*.*'),
                                                                          ('Text Documents', '*.txt')])
        if self.__file == "":
            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __saveFile(self):
        if self.__file is None:
            self.__file = asksaveasfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'),
                                                                              ('Document Files', '*.txt')])
            if self.__file == '':
                self.__file = None
            else:
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate('<<Cut>>')

    def __copy(self):
        self.__thisTextArea.event_generate('<<Copy>>')

    def __past(self):
        self.__thisTextArea.event_generate('<<Paste>>')

    def run(self):
        self.__root.mainloop()


# Run main App
notepad = Notepad(width=600, height=400)
notepad.run()
