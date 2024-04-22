from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition_system")

        #===============variables============
        self.var_dep=StringVar()
        self.var_cource=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        
        #first img
        img=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\face-recognition.png")
        img=img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=100)

        #second img
        img1=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student2.jpg")
        img1=img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=480,height=100)


        #third img
        img2=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student4.jpeg")
        img2=img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=450,height=100)

        
        #bg img
        img3=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\bgimage.jpg")
        img3=img3.resize((1280,580))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=580)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Baskerville Old Face",25,"bold"), bg ="white",fg = "brown")
        title_lbl.place(x=0,y=0,width=1280,height=35)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=17,y=45,width=1220,height=525)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE,text="Student details",font=("Baskerville Old Face",12,"bold"))
        left_frame.place (x=10,y=1,width =590,height=515)

        
        img_left=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student3.jpeg")
        img_left=img_left.resize((580,130))
        self.photoimg_left  = ImageTk.PhotoImage(img_left)


        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=580,height=110)
        
        # current cource 
        current_cource_frame = LabelFrame(left_frame,bd=2,bg = "white",relief=RIDGE,text="Current Cource Information",font=("Baskerville Old Face",12,"bold"))
        current_cource_frame.place (x=5,y=112,width =580,height=100)
         
        #Department
        dep_label=Label(current_cource_frame,text="Department",font=("Baskerville Old Face",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo =ttk.Combobox(current_cource_frame,textvariable=self.var_dep,font=("Baskerville Old Face",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","computer science","IT","civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Cource
        cource_label=Label(current_cource_frame,text="Cource",font=("Baskerville Old Face",12,"bold"),bg="white")
        cource_label.grid(row=0,column=2,padx=10,sticky=W)

        cource_combo =ttk.Combobox(current_cource_frame,textvariable=self.var_cource,font=("Baskerville Old Face",12,"bold"),state="readonly",width=15)
        cource_combo["values"]=("Select Cource","FE","SE","TE","BE")
        cource_combo.current(0)
        cource_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_cource_frame,text="Year",font=("Baskerville Old Face",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo = ttk.Combobox(current_cource_frame,textvariable=self.var_year,font=("Baskerville Old Face",12,"bold"),state="readonly",width=20)
        year_combo["values"]= ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_cource_frame,text="Semester",font=("Baskerville Old Face",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo =ttk.Combobox(current_cource_frame,textvariable=self.var_semester,font=("Baskerville Old Face",12,"bold"),state="readonly",width=15)
        semester_combo["values"]=("Select semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information cource 
        class_student_frame = LabelFrame(left_frame,bd=2,bg = "white",relief=RIDGE,text="Class Student Information",font=("Baskerville Old Face",12,"bold"))
        class_student_frame.place (x=5,y=213,width =580,height=275)

        #Student ID
        student_id_label=Label(class_student_frame,text="Student Id",font=("Baskerville Old Face",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry =ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=19,font=("Baskerville Old Face",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student Name
        student_name_label=Label(class_student_frame,text="Student Name",font=("Baskerville Old Face",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=4,pady=5,sticky=W)

        student_name_entry =ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=12,font=("Baskerville Old Face",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=8,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division",font=("Baskerville Old Face",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry =ttk.Entry(class_student_frame,textvariable=self.var_div,width=19,font=("Baskerville Old Face",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Baskerville Old Face",12,"bold"),state="readonly",width=17)
        div_combo["values"]= ("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll Number
        roll_number_label=Label(class_student_frame,text="Roll Number",font=("Baskerville Old Face",12,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=4,pady=5,sticky=W)

        roll_number_entry =ttk.Entry(class_student_frame,textvariable=self.var_roll,width=12,font=("Baskerville Old Face",12,"bold"))
        roll_number_entry.grid(row=1,column=3,padx=8,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender",font=("Baskerville Old Face",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Baskerville Old Face",12,"bold"),state="readonly",width=17)
        gender_combo["values"]= ("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
       
        dob_label=Label(class_student_frame,text="DOB",font=("Baskerville Old Face",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=4,pady=5,sticky=W)

        dob_entry =ttk.Entry(class_student_frame,textvariable=self.var_dob,width=12,font=("Baskerville Old Face",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=8,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email",font=("Baskerville Old Face",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry =ttk.Entry(class_student_frame,textvariable=self.var_email,width=19,font=("Baskerville Old Face",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number 
        phone_label=Label(class_student_frame,text="Phone Number",font=("Baskerville Old Face",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=4,pady=5,sticky=W)

        phone_entry =ttk.Entry(class_student_frame,textvariable=self.var_phone,width=12,font=("Baskerville Old Face",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=8,pady=5,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address",font=("Baskerville Old Face",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry =ttk.Entry(class_student_frame,textvariable=self.var_address,width=19,font=("Baskerville Old Face",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("Baskerville Old Face",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=4,pady=5,sticky=W)

        teacher_entry =ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=12,font=("Baskerville Old Face",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=8,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)
        
        
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=575,height=29)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command = self.update_data,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=223,width=575,height=28)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=29,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=29,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE,text="Student details",font=("Baskerville Old Face",12,"bold"))
        Right_frame.place (x=615,y=1,width =593,height=515)

        img_right=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student.jpg")
        img_right=img_right.resize((580,130))
        self.photoimg_right  = ImageTk.PhotoImage(img_right)


        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=580,height=110)

        #---search system
        search_frame = LabelFrame(Right_frame,bd=2,bg = "white",relief=RIDGE,text="Search System",font=("Baskerville Old Face",12,"bold"))
        search_frame.place (x=5,y=115,width =580,height=60)

        search_label=Label(search_frame,text="Search By",font=("Baskerville Old Face",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)

        search_combo =ttk.Combobox(search_frame,font=("Baskerville Old Face",11,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry =ttk.Entry(search_frame,width=10,font=("Baskerville Old Face",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=10,font=("Baskerville Old Face",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=6)

        show_all_btn=Button(search_frame,text="Show All",width=10,font=("Baskerville Old Face",11,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=6)

        #Table Frame
        table_frame =Frame(Right_frame,bd=2,bg = "white",relief=RIDGE,)
        table_frame.place (x=5,y=180,width =580,height=308)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","cource","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand =scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("cource",text="Cource")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("cource",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    #=================fuction declaration================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_cource.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.va_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()


                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception  as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





    #=====fetch data========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #========  get cursor =========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_cource.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
 
    # ===== Update Data ======
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details:",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep =%s,Cource = %s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                               

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_cource.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.va_std_id.get()

                    



                                                                                                                                                                         ))
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==== delete function=====
    def  delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent = self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql= "delete from student where Student_id =%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ==== reset fuction =======
    def reset_data(self):
        self.var_dep.set("Select Departement"),
        self.var_cource.set("Select Cource"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set("Select Division"),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        
    #  =======   Generate Data Set or Take Photo Sample  =======
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Udit@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myreseult = my_cursor.fetchall()
                id = 0
                for x in myreseult:
                    id+=1
                my_cursor.execute("update student set Dep =%s,Cource = %s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                               

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_cource.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.va_std_id.get()==id+1

                    



                                                                                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #======  Load predefined data on Face Frontals from opencv  =====

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimun Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                        cv2.imshow("cropped face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets compled !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





                                                                                                                            
                                                                                                                                                                                                                                                                                                     
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()




