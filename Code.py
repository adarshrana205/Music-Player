from tkinter import *
root=Tk()
root.geometry('300x300')
root.title("Music Player")


text=Label(root,text='Lets play music')
text.pack()
photo=PhotoImage(file='play.png')
photolabel=Label(root,image=photo)
photolabel.pack()
root.mainloop()