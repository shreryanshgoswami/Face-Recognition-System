from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help


class Face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Face_recognition_system")

        #first img
        img=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        #second img
        img1=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\facialrecognition.png")
        img1=img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=480,height=130)


        #third img
        img2=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\u.jpg")
        img2=img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=450,height=130)


        #bg img
        img3=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\bgimage.jpg")
        img3=img3.resize((1280,580))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1280,height=580)

        title_lbl = Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM",font=("Baskerville Old Face",35,"bold"), bg ="white",fg = "brown")
        title_lbl.place(x=0,y=0,width=1280,height=45)


        #student button
        img4=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student.jpg")
        img4=img4.resize((180,180))
        self.photoimg4 = ImageTk.PhotoImage(img4)
                
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=178,y=80,width=180,height=170)

        b1_1 = Button(bg_img,text= "Student Details",command=self.student_details,cursor="hand2",font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=178,y=248,width=180,height=30)



        
        #detect face button
        img5=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\face_detector1.jpg")
        img5=img5.resize((180,180))
        self.photoimg5 = ImageTk.PhotoImage(img5)
                
        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=413,y=80,width=180,height=170)

        b1_1 = Button(bg_img,text= "Face Detector",cursor="hand2",command=self.face_data,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=413,y=248,width=180,height=30)


        #Attendence button
        img6=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\Attendence.jpg")
        img6=img6.resize((180,180))
        self.photoimg6 = ImageTk.PhotoImage(img6)
                
        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=649,y=80,width=180,height=170)

        b1_1 = Button(bg_img,text= "Attendence",cursor="hand2",command=self.attendence_data,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=649,y=248,width=180,height=30)



        
        #Help button
        img7=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\Helpdesk.jpg")
        img7=img7.resize((180,180))
        self.photoimg7 = ImageTk.PhotoImage(img7)
                
        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=885,y=80,width=180,height=170)

        b1_1 = Button(bg_img,text= "Help Desk",cursor="hand2",command=self.help_data,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=885,y=248,width=180,height=30)



        #Train  Face button
        img8=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\Train.jpg")
        img8=img8.resize((180,180))
        self.photoimg8 = ImageTk.PhotoImage(img8)
                
        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=178,y=319,width=180,height=170)

        b1_1 = Button(bg_img,text= "Train",cursor="hand2",command=self.train_data,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=178,y=488,width=180,height=30)



        
        #Photos face   button
        img9=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\photos.jpg")
        img9=img9.resize((180,180))
        self.photoimg9 = ImageTk.PhotoImage(img9)
                
        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=413,y=319,width=180,height=170)

        b1_1 = Button(bg_img,text= "Photos",cursor="hand2",command=self.open_img,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=413,y=488,width=180,height=30)


        
        
        #Developer button
        img10=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\developer.jpg")
        img10=img10.resize((180,180))
        self.photoimg10 = ImageTk.PhotoImage(img10)
                
        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=649,y=319,width=180,height=170)

        b1_1 = Button(bg_img,text= "Developer",cursor="hand2",command=self.developer_data,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=649,y=488,width=180,height=30)


        #Exit button
        img11=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\exit.jpg")
        img11=img11.resize((180,180))
        self.photoimg11 = ImageTk.PhotoImage(img11)
                
        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=885,y=319,width=180,height=170)

        b1_1 = Button(bg_img,text= "Exit",cursor="hand2",command=self.iExit,font=("Baskerville Old Face",15,"bold"), bg ="darkblue",fg = "white")
        b1_1.place(x=885,y=488,width=180,height=30)
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition" , "Are you sure exit this project",parent = self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return




        # ========= Fuction Button  ========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Help(self.new_window)

      


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()


    
