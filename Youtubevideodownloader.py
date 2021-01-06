#Day7 Project
#Download youtube videos
from pytube import YouTube
from tkinter import *
root=Tk()
root.geometry("1500x1000")
root.title("YouTube video downloader")

def youtube():
    a=var.get()         #https://www.youtube.com/watch?v=X6fRmuZTO08
    ytvideo=YouTube(a).streams.filter(progressive=True).desc().first()

    ytvideo.download(r'C:\Users\kamal\Desktop')
    print('Entry Box',a)
l1=Label(root,text="Paste Your YouTube Video Link Here",bg='Papayawhip',fg='Lightcoral',font=('bold',40))
l1.place(x=10,y=50)
var=StringVar()
e1=Entry(root,textvariable=var,width=60)
e1.place(x=25,y=130)
e1.focus_set()
b1=Button(root,text='Download',command=youtube,bg='Green',fg='white',width=20,font=20)
b1.place(x=80,y=150)
root.mainloop()
