#BASIC SETUP

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font

window = Tk()
window.title("untitled")
window.geometry("1200x660")

#BASIC SETUP DONE

#DEINE FUNCYTIONS

#define new function

global savefileexists
savefileexists = False

def newfile():
    text.delete("1.0", END)
    window.title("New File")

#defines open function
def openfile():
    text.delete("1.0", END)
    text_file=filedialog.askopenfilename(initialdir="C:/Users/shash/Desktop", title="Open File",
                                         filetypes=(("Text Files", "*.txt"), ("Python", "*.py")) )

    if text_file:
        global savefileexists
        savefileexists = text_file
        #updates nanme
        name = text_file
        filename = name.split('/')
        length = len(filename)-1
        title = filename[length]
        window.title(title)

        #actually opens file lmao
        text_file = open(text_file, 'r')
        sample_text = text_file.read()
        text.insert(END, sample_text)
    else:
        window.title("Text Editor")

        text_file.close()

#defines save as
def saveasfile():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/shash/Desktop",
                                             title="Save File", filetypes=(("Text Files", "*.txt"), ("Python", "*.py")) )
    if text_file:
        name = text_file
        filename = name.split('/')
        length = len(filename) - 1
        title = filename[length]
        window.title(title)

        #actually saves file
        text_file = open(text_file, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()

#defines save
def savefile():
    global savefileexists
    if savefileexists:
        #actually saves file
        text_file = open(savefileexists, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()

        name = savefileexists
        filename = name.split('/')
        length = len(filename) - 1
        title = filename[length]
        window.title(title)
    else:
        saveasfile()


#MAKE EDIT MENU BUTTONS

#make cut
def cut(h):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete("sel.first", "sel.last")

def paste(h):
    position = text.index(INSERT)
    text.insert(position, selected)

def copy(h):
    global selected
    if text.selection_get():
        selected = text.selection_get()



#creates frame
frame = Frame(window)
frame.pack()

#scrollbar
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

#create text box
text = Text(frame, width=97, height=25, font=("Comic Sans", 20),
            selectbackground='sky blue', selectforeground="black",
            undo=True, yscrollcommand=text_scroll.set)

#config text_scroll
text_scroll.config(command = text.yview)

#create manu
menux = Menu(window)
window.config(menu=menux)

#add file menu buttons
menu_file = Menu(menux, tearoff=False)
menux.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="New", command=newfile)
menu_file.add_command(label="Open", command=openfile)
menu_file.add_command(label="Save", command=savefile)
menu_file.add_command(label="Save As", command=saveasfile)
menu_file.add_separator()
menu_file.add_command(labe="Exit", command=window.quit)

#add edit menu buttons
menu_edit = Menu(menux, tearoff=False)
menux.add_cascade(label="Edit", menu=menu_edit)
menu_edit.add_command(label="Undo")
menu_edit.add_separator()
menu_edit.add_command(label="Cut", command = lambda: cut(False))
menu_edit.add_command(label="Copy", command = lambda: copy(False))
menu_edit.add_command(label="Paste", command = lambda: paste(False))
menu_edit.add_command(labe="Delete")

text.pack()
window.mainloop()
