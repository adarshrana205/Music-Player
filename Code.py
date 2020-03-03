from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("Music Player")


text = Label(root, text='Lets play music')
text.pack()


def play_btn():
    print("Hey!")


photo = PhotoImage(file='play.png')
btn = Button(root, image=photo, command=play_btn)
btn.pack()

root.mainloop()