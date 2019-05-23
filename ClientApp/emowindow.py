import tkinter as tk
from tkinter import ttk
from functools import partial
import emoji
import emo
import re

#Fungsi Di luar kelas
_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def rendertext(text):
    return _nonbmp.sub(_surrogatepair,emoji.emojize(text))
#Fungsi buat render di dalam kelas

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
        t = tk.Toplevel(self)
        emojiFrame = tk.Frame(t)
        listbutton = []
        for coll in range(4):
            for roww in range ((int(len(emo.label)/4))):
                button = {}
                button['val'] = rendertext(emo.label[coll*(roww-1)+roww])
                button['widget'] = tk.Button(emojiFrame,fg="black",text=rendertext(button['val']),command=partial(self.addstring,button['val']))
                button['widget'].config(font=("Courier", 50))
                button['widget'].grid(row=roww,column=coll)
                listbutton.append(button)
        emojiFrame.pack(expand=True,fill="both")

    def addstring(self,p):
        self.label.configure(text=str(p))
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()

