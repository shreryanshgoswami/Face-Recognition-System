from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition_system")


        title_lbl = Label(self.root,text="HELP DESK",font=("Baskerville Old Face",25,"bold"), bg ="white",fg = "black")
        title_lbl.place(x=0,y=0,width=1280,height=35)

        img_top=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student4.jpeg")
        img_top=img_top.resize((1400,580))
        self.photoimg_top  = ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1272,height=580)

        dev_label=Label(f_lbl,text="Email  :shrnshgoswami@gmail.com ",font=("Baskerville Old Face",15,"bold"),bg="white")
        dev_label.place(x=450,y=150)



if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()