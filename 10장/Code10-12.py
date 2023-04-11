from tkinter import *
from time import *

fnameList=["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif","jeju6.gif"]
photoList=[None]*6
num=0

def clickNext():
    global num
    num+=1
    if num>5:
        num=0
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    fileName.configure(text=fnameList[num])

def clickPrev():
    global num
    num-=1
    if num<0:
        num=5
    photo=PhotoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    fileName.configure(text=fnameList[num])

window=Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev=Button(window,text="<<이전",command=clickPrev)
btnNext=Button(window,text="다음>>",command=clickNext)

photo=PhotoImage(file="gif/"+fnameList[0])
pLabel=Label(window,image=photo)

fileName=Label(window,text=fnameList[0])

btnPrev.place(x=250,y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=50)
fileName.place(x=325,y=10)

window.mainloop()