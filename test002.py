from tkinter import *

window = Tk()

window.title("hello")

window.geometry("600x400+660+340")

window.resizable(False, False)

label = Label(window, text="이경태")

label.pack()

window.mainloop()