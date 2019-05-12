from Tkinter import *

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)
        
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    
    entry.placeholder_state = state

    return state

userWindow = Tk()
userWindow.geometry('300x160')
userWindow.title("Anonymous Chat")
userWindow.resizable(False, False) 

frame = Frame(userWindow, bg='green')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)


label_0 = Label(userWindow, text="Take a Username:",font=("bold", 15), bg='green')
label_0.place(x=15,y=20)

entry_1 = Entry(userWindow,width=42, justify='center')
entry_1.place(x=20,y=60)
entry_1.grid(row=0,column=1,padx=20,pady=65,ipady=5)
add_placeholder_to(entry_1, 'Username')

Button(userWindow, text="Let's Chat",width=10,bg='brown',fg='white').place(x=110,y=120)
Button(userWindow, text='Kembali',width=10,bg='brown',fg='white').place(x=198,y=120)

userWindow.mainloop()