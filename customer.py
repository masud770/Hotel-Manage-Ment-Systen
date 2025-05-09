from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class cstmr_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #.........variables..........
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_custname=StringVar()
        self.var_father = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_country = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumb = StringVar()
        self.var_address = StringVar()


        # .........title.........

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 24, "bold"), bg="Midnight Blue",fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # .....logo.........

        img2 = Image.open(r"F:\Hotel\logo2.jpg")
        img2 = img2.resize((100, 60), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=50)

        #.........label frame..........

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 20,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #...........labels and entrys............

        #..........cstmr reference.......
        cstmr_ref=Label(labelframeleft,text="Customer Reference:",font=("times new roman", 12,"bold"),padx=2,pady=6)
        cstmr_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman", 12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #.........cstmr name.............
        cstmr_name = Label(labelframeleft, text="Customer Name:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        cstmr_name.grid(row=1, column=0, sticky=W)

        entry_name = ttk.Entry(labelframeleft,textvariable=self.var_custname, width=29, font=("times new roman", 12, "bold"))
        entry_name.grid(row=1, column=1)

        # .........Father name.............
        father_name = Label(labelframeleft, text="Father's Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        father_name.grid(row=2, column=0, sticky=W)

        entry_f_name = ttk.Entry(labelframeleft,textvariable=self.var_father, width=29, font=("times new roman", 12, "bold"))
        entry_f_name.grid(row=2, column=1)

        #........gender combo box.......
        lbl_gender = Label(labelframeleft, text="Gender:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman", 12, "bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current()
        combo_gender.grid(row=3,column=1)

        # .........postcode.............
        lbl_postcode = Label(labelframeleft, text="Post Code:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)

        entry_postcode = ttk.Entry(labelframeleft,textvariable=self.var_post, width=29, font=("times new roman", 12, "bold"))
        entry_postcode.grid(row=4, column=1)

        # .........mobile number.............
        lbl_mblnumb = Label(labelframeleft, text="Contact Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mblnumb.grid(row=5, column=0, sticky=W)

        entry_mblnumb = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("times new roman", 12, "bold"))
        entry_mblnumb.grid(row=5, column=1)

        # .........Email.............
        lbl_email = Label(labelframeleft, text="Email:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("times new roman", 12, "bold"))
        entry_email.grid(row=6, column=1)

        # ........Country combo box.......
        lbl_country = Label(labelframeleft, text="Country:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_country.grid(row=7, column=0, sticky=W)

        combo_country = ttk.Combobox(labelframeleft,textvariable=self.var_country, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_country["value"] = ("America","Australia","Afghanistan","Argentina","Bangladesh","Belgium","Bhutan","Brazil","Canada","China","Colombia","Denmark",
                                 "Ecuador","Egypt","Finland","France","Germany","Ghana","Hungary","India","Indonesia","Iran","Iraq","Ireland","Italy",
                                 "Japan","Jordan","Kenya","Kuwait","Libya","Luxembourg","Malaysia","Maldives","Mexico","Morocco","Myanmar","Namibia",
                                 "Netherlands","Nepal","New Zealand","Nigeria","Norway","North Korea","Oman","Pakistan","Palestine State","Papua New Guinea",
                                 "Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Saudi Arabia","Senegal","Singapore","Somalia",
                                 "South Africa","South Korea","Spain","Sri Lanka","Sweden","Switzerland","Syria","Thailand","Turkey","Tunisia","Uganda","Ukraine",
                                 "United Arab Emirates","United Kingdom","Uruguay","Venezuela","Vietnam","Yemen","Zimbabwe")
        combo_country.current()
        combo_country.grid(row=7, column=1)


        # ........Id proof combo box.......
        lbl_idproof = Label(labelframeleft, text="ID Proof Type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_idproof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_idproof, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("NID", "Passport", "Birth Certificate","Driving Licence")
        combo_id.current()
        combo_id.grid(row=8, column=1)

        # .........Id number.............
        lbl_idnumb = Label(labelframeleft, text="ID Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_idnumb.grid(row=9, column=0, sticky=W)

        entry_idnumb = ttk.Entry(labelframeleft,textvariable=self.var_idnumb, width=29, font=("times new roman", 12, "bold"))
        entry_idnumb.grid(row=9, column=1)

        # .........Address.............
        lbl_address = Label(labelframeleft, text="Address:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        entry_address = ttk.Entry(labelframeleft,textvariable=self.var_address, width=29, font=("times new roman", 12, "bold"))
        entry_address.grid(row=10, column=1)

        #..............buttons................
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1,pady=2)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update ,font=("arial", 12, "bold"), bg="gold", fg="black", width=9)
        btnUpdate.grid(row=0, column=1, padx=1, pady=2)

        btnDelete = Button(btn_frame, text="DELETE",command=self.dlt_data ,font=("arial", 12, "bold"), bg="red", fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1, pady=2)

        btnReset = Button(btn_frame, text="RESET",command=self.rst_data, font=("arial", 12, "bold"), bg="purple", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1, pady=2)

        #.................Table Frame And Search................

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("times new roman", 20, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lbl_search = Label(table_frame, text="Search By:", font=("arial", 13, "bold"),bg="navyblue",fg="white")
        lbl_search.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Reference")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        entry_search = ttk.Entry(table_frame,textvariable=self.txt_search, width=28, font=("times new roman", 12, "bold"))
        entry_search.grid(row=0, column=2,padx=2)

        btnSearch = Button(table_frame, text="SEARCH",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1, pady=2)

        btnShowALL = Button(table_frame, text="SHOW ALL",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowALL.grid(row=0, column=4, padx=1, pady=2)

        #..........show data table............

        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=50, width=860, height=350)

        scroll_x =ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.cstmr_dtls_table=ttk.Treeview(details_frame,columns=("ref","name","father","gender","post","mobile","email",
                                           "country","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cstmr_dtls_table.xview)
        scroll_y.config(command=self.cstmr_dtls_table.yview)

        self.cstmr_dtls_table.heading("ref",text="Reference Number")
        self.cstmr_dtls_table.heading("name", text="Name")
        self.cstmr_dtls_table.heading("father", text="Father's Name")
        self.cstmr_dtls_table.heading("gender", text="Gender")
        self.cstmr_dtls_table.heading("post", text="Post Code")
        self.cstmr_dtls_table.heading("mobile", text="Contact Number")
        self.cstmr_dtls_table.heading("email", text="Email")
        self.cstmr_dtls_table.heading("country", text="Country")
        self.cstmr_dtls_table.heading("idproof", text="ID Proof")
        self.cstmr_dtls_table.heading("idnumber", text="ID Number")
        self.cstmr_dtls_table.heading("address", text="Address")

        self.cstmr_dtls_table["show"]="headings"

        self.cstmr_dtls_table.column("ref",width=120)
        self.cstmr_dtls_table.column("name",width=170)
        self.cstmr_dtls_table.column("father",width=170)
        self.cstmr_dtls_table.column("gender",width=100)
        self.cstmr_dtls_table.column("post",width=100)
        self.cstmr_dtls_table.column("mobile",width=100)
        self.cstmr_dtls_table.column("email",width=170)
        self.cstmr_dtls_table.column("country",width=100)
        self.cstmr_dtls_table.column("idproof",width=100)
        self.cstmr_dtls_table.column("idnumber",width=170)
        self.cstmr_dtls_table.column("address",width=170)

        self.cstmr_dtls_table.pack(fill=BOTH,expand=1)
        self.cstmr_dtls_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()=="":
            messagebox.showerror("Error!!!","All fields are required!!",parent=self.root)
        else:
            try:
                connct=mysql.connector.connect(host="localhost",username="root",password="Sharkboy14757@",database="management")
                my_cursor=connct.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_custname.get(),
                    self.var_father.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_country.get(),
                    self.var_idproof.get(),
                    self.var_idnumb.get(),
                    self.var_address.get()
                                              ))

                connct.commit()
                self.fetch_data()
                connct.close()
                messagebox.showinfo("Success!!!","Customer Has Been Added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning!!!",f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()
        my_cursor.execute("SELECT * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cstmr_dtls_table.delete(*self.cstmr_dtls_table.get_children())
            for i in rows:
                self.cstmr_dtls_table.insert("",END,values=i)
            connct.commit()
        connct.close()


    def get_cursor(self, event=""):
        cursor_row=self.cstmr_dtls_table.focus()
        cntent=self.cstmr_dtls_table.item(cursor_row)
        row=cntent["values"]

        self.var_ref.set(row[0]),
        self.var_custname.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_country.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumb.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "" or self.var_father.get() == "":
            messagebox.showerror("Error!!!","All fields are required!!",parent=self.root)
        else:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            my_cursor.execute("UPDATE customer set name=%s,father=%s,gender=%s,post=%s,mobile=%s,email=%s,country=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(

                self.var_custname.get(),
                self.var_father.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_country.get(),
                self.var_idproof.get(),
                self.var_idnumb.get(),
                self.var_address.get(),
                self.var_ref.get()

            ))
            connct.commit()
            self.fetch_data()
            connct.close()
            messagebox.showinfo("UPDATE!!!","Customer Details Has Been Updated Successfully!!",parent=self.root)

    def dlt_data(self):
        dlt_data=messagebox.askyesno("DELETE!!!","Do You Want To Delete This Customer???",parent=self.root)
        if dlt_data>0:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            query="DELETE from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not dlt_data:
                return
        connct.commit()
        self.fetch_data()
        connct.close()

    def rst_data(self):
        #self.var_ref.set(""),
        self.var_custname.set(""),
        self.var_father.set(""),
        self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_country.set(""),
        self.var_idproof.set(""),
        self.var_idnumb.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@", database="management")
        my_cursor = connct.cursor()

        my_cursor.execute("select * from customer where ref="+str(self.txt_search.get()))
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cstmr_dtls_table.delete(*self.cstmr_dtls_table.get_children())
            for i in rows:
                self.cstmr_dtls_table.insert("",END,values=i)
            connct.commit()
        connct.close()


    #my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")


















if __name__ == '__main__':
    root=Tk()
    obj=cstmr_window(root)
    root.mainloop()