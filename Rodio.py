from tkinter import *
from tkinter import font 
from tkinter import ttk,messagebox
from playsound import playsound
import webbrowser
from PIL import Image,ImageTk
def hello():
    messagebox.showinfo("INFO","You need internet connection for this!")
    webbrowser.open("https://rajib3728.github.io/bengali/")
def hi():
    messagebox.showinfo("INFO","You need internet connection for this!")
    webbrowser.open("https://rajib3728.github.io/hindi/")
def lol():
    root.destroy() 
def bol():
    messagebox.showinfo("INFO","You need internet connection for this!")
    webbrowser.open("https://rajib3728.github.io/english/")
def welso():
    playsound("C:\\Users\\Rajib Kr paul\\OneDrive\\Documents\\visiual stdio code\\python practice\\song1.mp3")
def link():
    webbrowser.open("https://sites.google.com/view/the-earth-infomation/home")    
root = Tk()    
root.geometry("1600x900")
root.minsize(600,400)
photo = PhotoImage(file = "logo.png")
root.iconphoto(False, photo)
root.title("Rajib paul")
bg=ImageTk.PhotoImage(file="C:\\Users\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\python practice\\b5.jpg")
bglb=Label(root,image=bg)
bglb.place(x=0,y=0,height=900,width=1600)
x = Label(root,text=" WELCOME TO THIS MP3 PLAYER",bg="black",padx="30",pady="20",font=("bold",40),fg="yellow")
f4=Frame(root,bg="grey",width=400,height=400)
f4.place(x=560,y=200)
l2=Label(f4,fg="black",font=("bold",25),text="SELECT CATAGORY",bg="green2")
l2.place(x=27,y=10)
b1=Button(f4,text="Bengali",command=hello,bg="purple",fg="black",padx=60,font=("bold",20),borderwidth=1)
b1.place(x=80,y=80)
b2=Button(f4,bg="purple",text="Hindi",command=hi,font=("bold",20),padx=75,fg="black")
b2.place(x=80,y=160)
b3=Button(f4,bg="red",text="Exit",command=lol,font=("bold",13))
b3.place(x=180,y=340)
b4=Button(f4,bg="purple",text="English",command=bol,font=("bold",20),padx=60,fg="black")
b4.place(x=80,y=240)
x.pack()
welso()
l3=Label(root,text="You may visit our page!",font=("bold",15),fg="white",bg="black")
l3.place(x=580,y=620)
b5=Button(root,text="visit now",fg="yellow",bg="blue",command=link)
b5.place(x=820,y=621)
root.mainloop()