#importing module
from tkinter import Text
from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import Scrollbar
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import END
from tkinter import INSERT
from tkinter.messagebox import showerror
from tkinter.messagebox import askquestion
#----------------------------------------------------------------------------
path = ''
def open_file():
    global path
    x = path[:]
    try:
        file_path = askopenfilename(title='Open file', filetypes=[('Text Documents','*.txt'),('All files','*.*')])
        path = file_path
        x = open(file_path, 'rb')
        text.delete(1.0, END)
        text.insert(INSERT, x.read())
        x.close()
    except:
        path = x
def save_file():
    global path
    if len(path)==0:
        file_path = asksaveasfile(title='Save file', filetypes=[('Text Documents', '*.txt'),('All files','*.*')], defaultextension=[('Text Documents', '*.txt'),('All files','*.*')])
        path = file_path.name
        o = open(path, 'w')
        o.write(text.get(1.0, END))
        o.close()
    else:
        o = open(path, 'w')
        o.write(text.get(1.0, END))
        o.close()
def new_file():
    global path
    if len(text.get(1.0, END))==1:
        path = ''
        text.delete(1.0, END)
    else:
        a = askquestion(title='Notepad', message='Do you wand to save changes?')
        print(a)
        if a == 'yes':
            file_path = asksaveasfile(title='Save file', filetypes=[('Text Documents', '*.txt'),('All files','*.*')], defaultextension=[('Text Documents', '*.txt'),('All files','*.*')])
            path = file_path.name
            o = open(path, 'w')
            o.write(text.get(1.0, END))
            o.close()
        if a == 'no':
            path = ''
            text.delete(1.0, END)
#----------------------------------------------------------------------------
window = Tk()
window.title('Notepad')
window.geometry('0x0')
window.resizable(0,0)
try:
    window.iconbitmap('icon.ico')
except:
    showerror(title='Error', message='Icon not found')
    window.destroy()
window.resizable(1,1)
window.geometry('700x500')
window.resizable(0,0)
window.configure(bg='light gray')
#----------------------------------------------------------------------------
frame_title = Frame(window, width=300, bg='green')
frame_title.pack()

frame_body = Frame(window)
frame_body.pack()

open_button = Button(frame_title, text='Open',font=('',10), bd=0, bg='Sky Blue', command=open_file)
open_button.bind()
open_button.grid(row=0, column=0)

new_button = Button(frame_title, text='New',font=('',10), bd=0, bg='light green', command=new_file)
new_button.grid(row=0, column=1)

save_button = Button(frame_title, text='Save', font=('',10), bd=0, bg='light pink', command=save_file)
save_button.bind()
save_button.grid(row=0, column=2)

text = Text(frame_body,font=('Consolas',15), bd=0, fg='gray', highlightbackground='pink', highlightcolor='pink')
text.pack(expand=1)

#text_scrollbar = Scrollbar(frame_body, command=text)
#text_scrollbar.pack(side='right' ,fill='y')


#----------------------------------------------------------------------------
window.mainloop()
#----------------------------------------------------------------------------
'''\ \    ____    / /
 \ \  / __ \  / /
  \ \/ /  \ \/ /
   \__/    \__/'''
