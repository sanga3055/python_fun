from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
#root.resizable(0,0)
root.title("Youtube video downloader by sanga3055@gmail.com")

Label(root,text = 'Youtube Video Downloader, written in python', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video_streams = url.streams
    # mp4_video_stream = video_streams.filter(file_extension = "mp4").filter(progressive=True)
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = '--> Click here to Download <-- ', font = 'arial 12 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
