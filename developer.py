from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition_system")


        title_lbl = Label(self.root,text="DEVELOPER",font=("Baskerville Old Face",25,"bold"), bg ="white",fg = "blue")
        title_lbl.place(x=0,y=0,width=1280,height=35)

        img_top=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\dev.jpg")
        img_top=img_top.resize((1400,580))
        self.photoimg_top  = ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1272,height=580)
   
        # Frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=830,y=0,width=420,height=480)

        img_top1=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\kiran.jpg")
        img_top1=img_top1.resize((160,160))
        self.photoimg_top1  = ImageTk.PhotoImage(img_top1)


        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=258,y=0,width=160,height=160)
   
        # Developer info
        dev_label=Label(main_frame,text="Hello my name , Shreyansh",font=("Baskerville Old Face",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am full stack developer .",font=("Baskerville Old Face",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)
       
        
        img2=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,310))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=170,width=450,height=310)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()