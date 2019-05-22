from tkinter import filedialog
from tkinter import *
from functools import partial
import os

root = Tk()

def get():
	print('now')
	p = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Image files","*.jpg;*.png;*.gif"),("Document files","*.pdf;*.doc,;*.docx"),("all files", "*.*")))
	print(os.path.isfile(p))
	print(p)

button = Button(root,text="hallo",command=partial(get))
button.pack()
root.mainloop()