from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata =[]
class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_recognition_system")

        # ========== variables =========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


         #first img
        img=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student2.jpg")
        img=img.resize((660,150))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=660,height=150)

        #second img
        img1=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student1.jpg")
        img1=img1.resize((660,150))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=660,y=0,width=660,height=150)

        #bg img
        img3=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\bgimage.jpg")
        img3=img3.resize((1280,580))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1280,height=580)

        
        title_lbl = Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("Baskerville Old Face",25,"bold"), bg ="white",fg = "brown")
        title_lbl.place(x=0,y=0,width=1280,height=35)

        
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=17,y=45,width=1220,height=525)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE,text="Student Attendence Details",font=("Baskerville Old Face",12,"bold"))
        left_frame.place (x=10,y=1,width =590,height=515)

        img_left=Image.open(r"C:\Users\UDIT MISHRA\Desktop\Face Recognition System\college_images\student3.jpeg")
        img_left=img_left.resize((580,130))
        self.photoimg_left  = ImageTk.PhotoImage(img_left)


        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=580,height=110)
        
        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=115,width=580,height=340)


        # Lables and Entry

        #Attendence ID
        attendence_id_label=Label(left_inside_frame,text="Attendence Id",font=("Baskerville Old Face",12,"bold"),bg="white")
        attendence_id_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)

        attendence_id_entry =ttk.Entry(left_inside_frame,width=13,textvariable=self.var_atten_id,font=("Baskerville Old Face",12,"bold"))
        attendence_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll
        rollLabel=Label(left_inside_frame,text="Roll",font=("Baskerville Old Face",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=8,pady=5,sticky=W)

        atten_roll =ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("Baskerville Old Face",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=14,pady=5,sticky=W)

        #name
        nameLabel=Label(left_inside_frame,text="Name",font=("Baskerville Old Face",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=4,pady=5,sticky=W)

        atten_name =ttk.Entry(left_inside_frame,width=13,textvariable=self.var_atten_name,font=("Baskerville Old Face",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Department
        depLabel=Label(left_inside_frame,text="Department",font=("Baskerville Old Face",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=8,pady=5,sticky=W)

        atten_roll =ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("Baskerville Old Face",12,"bold"))
        atten_roll.grid(row=1,column=3,padx=14,pady=5,sticky=W)

        # Time
        timeLabel=Label(left_inside_frame,text="Time",font=("Baskerville Old Face",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=4,pady=5,sticky=W)

        atten_roll =ttk.Entry(left_inside_frame,width=13,textvariable=self.var_atten_time,font=("Baskerville Old Face",12,"bold"))
        atten_roll.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date
        dateLabel=Label(left_inside_frame,text="Date",font=("Baskerville Old Face",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=8,pady=5,sticky=W)

        atten_roll =ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("Baskerville Old Face",12,"bold"))
        atten_roll.grid(row=2,column=3,padx=14,pady=5,sticky=W)

         # Attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status",font=("Baskerville Old Face",12,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0,padx=4,pady=5,sticky=W)

        self.atten_status =ttk.Combobox(left_inside_frame,font=("Baskerville Old Face",11,"bold"),state="readonly",width=13,textvariable=self.var_atten_attendance,)
        self.atten_status["values"]=("Status ","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        self.atten_status.current(0)
        

        #bbuttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=575,height=29)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("Baskerville Old Face",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE,text="Attendence details",font=("Baskerville Old Face",12,"bold"))
        Right_frame.place (x=615,y=1,width =593,height=515)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=579,height=390)

        # ===== scroll bar =====
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id", "roll", "name" , "department" , "time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence Id")
        self.AttendenceReportTable.heading("roll",text ="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text ="Department")
        self.AttendenceReportTable.heading("time",text ="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text ="Attendence")

        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ========  fetch data =======
    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title = "Open CSV",filetypes=(("CSV file","*.csv"),("ALl File","*.*")),parent=self.root)
        with open (fln) as myfile:
            csvread  = csv.reader(myfile,delimiter=",")
            for  i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv
    def exportCsv(self):
        try:
            if(len(mydata))<1:
                messagebox.showerror("No data","No Data found to export ", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir= os.getcwd(),title = "Open CSV",filetypes=(("CSV file","*.csv"),("ALl File","*.*")),parent=self.root)
            with open (fln, mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export" , "Your data exported to "+os.path.basename(fln) + "successfully")
        except Exception  as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows  = content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")












        



if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()