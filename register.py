from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        # ============ Variable ===============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cnfmpass=StringVar()


        # ====== bg image  =====

        img=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\un.jpg")
        img=img.resize((1280,690))
        self.photoimg = ImageTk.PhotoImage(img)


        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1280,height=705)

        # ==== left image  =======

        img1=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\thought-good-morning-messages-LoveSove.jpg")
        img1=img1.resize((400,500))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=50,y=50,width=400,height=500)

        # ====== main farme  =====
        frame  = Frame(self.root,bg="white")
        frame.place(x=450,y=50,width=670,height=500)
         
        # ===== Lables =======
        register_lbl=lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="darkgreen")
        register_lbl.place(x=20,y=15)

        # ====== Lables and entry fields =====
           
        # ====== >>>>>>> Row1:-1 <<<<< ======
        fname=lbl=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=37,y=90)

        fname_entry  =ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=40,y=120,width=205)

        lname=lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=300,y=90)

        lname_entry  =ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        lname_entry.place(x=300,y=120,width=205)



        # ====== >>>>>>>row2:-2 <<<<< ======
        contact=lbl=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=37,y=160)

        self.text_contact =ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13))
        self.text_contact.place(x=40,y=190,width=205)

        email=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=300,y=160)

        self.text_email =ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13))
        self.text_email.place(x=300,y=190,width=205)

         # ====== >>>>>>>row3:-3 <<<<< ======
        security_Q=lbl=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=37,y=230)

        self_combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self_combo_security_Q["values"]=("Select","Select Your Birth Place ","Your Girlfriend Name","Your Pet Name")
        self_combo_security_Q.current(0)
        self_combo_security_Q.place(x=37,y=260 ,width = 205)

        security_A=lbl=Label(frame,text=" Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=300,y=230)

        self.text_security =ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",13))
        self.text_security.place(x=300,y=260,width=205)

        # ====== >>>>>>>row4:-4 <<<<< ======
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=37,y=300)

        self.text_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",13))
        self.text_password.place(x=40,y=330,width=205)


        cnfm_password=lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cnfm_password.place(x=300,y=300)

        self.text_cnfm_password=ttk.Entry(frame,textvariable=self.var_cnfmpass,font=("times new roman",13))
        self.text_cnfm_password.place(x=300,y=330,width=205)

        # =====  check button ======
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font =("times new roman",12,"bold"),onvalue = 1, offvalue =0,bg="white")
        checkbtn.place(x=37,y=370)

        # =======  Buttons ===========
        
        img2=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\register-now-button1.jpg")
        img2=img2.resize((200,55))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=Button(frame,image= self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",font =("times new roman",12,"bold"),fg="white",bg="white")
        b1.place(x=10,y=400,width=250)
        

        img3=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\loginpng.png")
        img3=img3.resize((200,43))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1=Button(frame,image= self.photoimg3,borderwidth=0,cursor="hand2",font =("times new roman",12,"bold"),fg="white",bg="white")
        b1.place(x=300,y=405,width=250)

        #  ========= fuction declaration =========

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error" , "All fields are required:")

        elif self.var_pass.get()!=self.var_cnfmpass.get():
            messagebox.showerror("Error","password & confirm password must be same:")
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error" , "Please agree our terms  & conditions")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
            my_cursor=conn.cursor()

            query = ("select * from registration where email =%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
               messagebox.showerror("Error","user already exist, please try another email")
            else:
               my_cursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                  
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully")
        



      

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()