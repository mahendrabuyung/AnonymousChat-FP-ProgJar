import tkinter as tk
from tkinter import ttk
from functools import partial
import os
from PIL import ImageTk, Image

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="emo",fg="blue",command=self.emoji_window)
        self.button.pack(side="top")
        self.label = tk.Label(self,text='hallo')
        self.label.pack(side="left")
        self.imageton = []
        self.getstiker()

    def emoji_window(self):
        emojiCategory = ['orang','hewan','aksesoris']
        tab = {}
        self.counter += 1
        index = 0
        button = []
        ink = 0
        t = tk.Toplevel(self)
        tabControl = ttk.Notebook(t)
        for i in emojiCategory :
            tab[i] = ttk.Frame(tabControl)
            tabControl.add(tab[i], text=i,)
            for coll in range(1,20):
                for roww in range (1,20):
                    p = {}
                    p['val'] = coll*roww
                    p['widget'] = tk.Button(tab[i],fg="black",bg="blue",text=str(roww*coll),command=partial(self.sendstring,p['val']))
                    
                    p['widget'].grid(row=roww,column=coll)
                    button.append(p)
            index = index + 1
        tabControl.configure(width=500,height=500,padding=3)
        tabControl.pack(expand=True,fill="both")

    def sendstring(self,p):
        self.label.configure(text=str(p))
    
    def getstiker(self):
        listStiker = []
        index = 0
        masterpath = "stiker"
        for i in os.listdir(masterpath):
            img = ImageTk.PhotoImage(Image.open(masterpath+"/"+i))
            listStiker.append(img)
            k = tk.Button(self, text="i",image = img,width=100)
            k.image = img
            k.pack(side="left",fill = "both", expand = "yes")
            self.imageton.append(k)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()