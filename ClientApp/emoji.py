import tkinter as tk
from tkinter import ttk
from functools import partial
import re
from random import randrange


#Firstinisiasi
_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def rendertext(text):
    return _nonbmp.sub(_surrogatepair, text)

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="emo",fg="blue",
                                command=self.emoji_window)
        self.button.pack(side="top")
        self.label = tk.Label(self,text='hallo')
        self.label.config(font=("Courier", 44))
        self.label.pack(side="left")

    def emoji_window(self):
        emojiCategory = ['orang','hewan','aksesoris']
        test = ['\N{Grinning Face}','\N{Face With Tears Of Joy}','\N{Slightly Smiling Face}']
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
                    p['val'] = rendertext(test[randrange(0,3)])
                    p['widget'] = tk.Button(tab[i],fg="black",bg="blue",text=str(roww*coll),command=partial(self.sendstring,p['val']))
                    
                    p['widget'].grid(row=roww,column=coll)
                    button.append(p)
            index = index + 1
        tabControl.configure(width=500,height=500,padding=3)
        tabControl.pack(expand=True,fill="both")

    def sendstring(self,p):
        self.label.configure(text=str(p))
        
    

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()