from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class room_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management ")
        self.root.geometry("1295x550+230+220")

        # ...................variable...............
        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype =StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days=StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()


        # ...................title.................

        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 24, "bold"),bg="Midnight Blue", fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ....................logo.................

        img2 = Image.open(r"F:\Hotel\logo2.jpg")
        img2 = img2.resize((100, 60), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=100, height=50)

        # .........label frame..........

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",font=("times new roman", 20, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ...........labels and entrys............

        # ..........cstmr contact.......
        cstmr_contact = Label(labelframeleft, text="Customer Contact:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        cstmr_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("times new roman", 12, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)

        # ..........Show data button.......
        btnShowData=Button(labelframeleft,command=self.Show_contact,text="Show Data",font=("arial", 12, "bold"),bg="black",fg="gold",width=8)
        btnShowData.place(x=310,y=4)

        # .........check_in_date.............
        chk_in_date = Label(labelframeleft, text="Check in Date:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        chk_in_date.grid(row=1, column=0, sticky=W)

        entry_chk_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29,font=("times new roman", 12, "bold"))
        entry_chk_in_date.grid(row=1, column=1)

        # .........check_out date.............
        chk_out_date = Label(labelframeleft, text="Check out Date:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        chk_out_date.grid(row=2, column=0, sticky=W)

        entry_ckh_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout , width=29,font=("times new roman", 12, "bold"))
        entry_ckh_out_date.grid(row=2, column=1)

        # ........room type combo box.......
        lbl_room_type = Label(labelframeleft, text="Room Type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()
        my_cursor.execute("SELECT room_type from room_details")
        roomtype=my_cursor.fetchall()

        combo_room_type = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype , font=("times new roman", 12, "bold"),width=27, state="readonly")
        combo_room_type["value"] = roomtype
        combo_room_type.current()
        combo_room_type.grid(row=3, column=1)

        # .........Room_Available.............
        Room_Available = Label(labelframeleft, text="Available Room:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        Room_Available.grid(row=4, column=0, sticky=W)

        #entry_Room_Available = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable ,width=29, font=("times new roman", 12, "bold"))
        #entry_Room_Available.grid(row=4, column=1)

        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()
        my_cursor.execute("SELECT room_no from room_details")
        rows=my_cursor.fetchall()

        combo_room_no = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("times new roman", 12, "bold"), width=27, state="readonly")
        combo_room_no["value"] = rows
        combo_room_no.current()
        combo_room_no.grid(row=4, column=1)

        # .........Meal...............
        meal = Label(labelframeleft, text="Meal:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        meal.grid(row=5, column=0, sticky=W)

        entry_Meal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=29, font=("times new roman", 12, "bold"))
        entry_Meal.grid(row=5, column=1)

        # .........No_of_Days...............
        No_of_Days = Label(labelframeleft, text="Number of Days:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        No_of_Days.grid(row=6, column=0, sticky=W)

        entry_No_of_Days = ttk.Entry(labelframeleft, textvariable=self.var_no_of_days ,width=29, font=("times new roman", 12, "bold"))
        entry_No_of_Days.grid(row=6, column=1)

        # .........Paid Tax...............
        Paid_tax = Label(labelframeleft, text="Paid Tax:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        Paid_tax.grid(row=7, column=0, sticky=W)

        entry_paid_tax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=("times new roman", 12, "bold"))
        entry_paid_tax.grid(row=7, column=1)

        # .........Sub Total...............
        sub_total = Label(labelframeleft, text="Sub Total:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        sub_total.grid(row=8, column=0, sticky=W)

        entry_sub_total = ttk.Entry(labelframeleft,textvariable=self.var_subtotal, width=29, font=("times new roman", 12, "bold"))
        entry_sub_total.grid(row=8, column=1)

        # .........Total cost...............
        total_cost = Label(labelframeleft, text="Total Cost:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        total_cost.grid(row=9, column=0, sticky=W)

        entry_total_cost = ttk.Entry(labelframeleft, textvariable=self.var_total, width=29, font=("times new roman", 12, "bold"))
        entry_total_cost.grid(row=9, column=1)

        # ..............Bill_buttons................
        btnBill = Button(labelframeleft, text="BILL",command=self.total, font=("arial", 12, "bold"), bg="teal",fg="white", width=9)
        btnBill.grid(row=10, column=0, padx=1, pady=2,sticky=W)


        # ..............buttons................
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_data,font=("arial", 12, "bold"), bg="green",fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1, pady=2)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update, font=("arial", 12, "bold"), bg="gold",fg="black", width=9)
        btnUpdate.grid(row=0, column=1, padx=1, pady=2)

        btnDelete = Button(btn_frame, text="DELETE",command=self.dlt_data,font=("arial", 12, "bold"), bg="red",fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1, pady=2)

        btnReset = Button(btn_frame, text="RESET",command=self.rst_data, font=("arial", 12, "bold"), bg="purple",fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1, pady=2)

        # .................Right side image................
        img3 = Image.open(r"F:\Hotel\Room.jpeg")
        img3 = img3.resize((520, 300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg3.place(x=760, y=55, width=520, height=230)

        # .................Table Frame And Search SYSTEM................
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search System",font=("times new roman", 20, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lbl_search = Label(table_frame, text="Search By:", font=("arial", 13, "bold"), bg="navyblue", fg="white")
        lbl_search.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("times new roman", 12, "bold"),width=24, state="readonly")
        combo_search["value"] = ("Contact Number", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(table_frame, textvariable=self.txt_search, width=28,font=("times new roman", 12, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_frame, text="SEARCH",command=self.search_system, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1, pady=2)

        btnShowALL = Button(table_frame, text="SHOW ALL",command=self.fetch_data, font=("arial", 12, "bold"),bg="black", fg="gold", width=9)
        btnShowALL.grid(row=0, column=4, padx=1, pady=2)

        #..........show data table............
        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=50, width=860, height=180)

        scroll_x =ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient=VERTICAL)

        self.room_table=ttk.Treeview(details_frame,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","no_of_days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin", text="Checkin")
        self.room_table.heading("checkout", text="Checkout")
        self.room_table.heading("roomtype", text="Room type")
        self.room_table.heading("roomavailable", text="Room no")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("no_of_days", text="No_of_Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("no_of_days",width=170)
        self.room_table.pack(fill=BOTH,expand=1)


        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        #..........add_data............

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error!!!","All fields are required!!",parent=self.root)
        else:
            try:
                connct=mysql.connector.connect(host="localhost",username="root",password="Sharkboy14757@",database="management")
                my_cursor=connct.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_no_of_days.get()

                ))

                connct.commit()
                self.fetch_data()
                connct.close()
                messagebox.showinfo("Success!!!","Room Booked!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning!!!",f"Something went wrong:{str(es)}",parent=self.root)

    # ..........fetch data table............
    def fetch_data(self):
        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()
        my_cursor.execute("SELECT * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            connct.commit()
        connct.close()

    # .........................get_cursor_data.................
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        cntent=self.room_table.item(cursor_row)
        row=cntent["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_no_of_days.set(row[6])


    #.........................Update Data.................
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error!!!","All fields are required!!",parent=self.root)
        else:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            my_cursor.execute("UPDATE room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where contact=%s",(

                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_no_of_days.get(),
                    self.var_contact.get()

            ))
            connct.commit()
            self.fetch_data()
            connct.close()
            messagebox.showinfo("UPDATE!!!","Room Details Has Been Updated Successfully!!",parent=self.root)

    #................Delete data.................

    def dlt_data(self):
        dlt_data = messagebox.askyesno("DELETE!!!", "Do You Want To Delete This Customer???", parent=self.root)
        if dlt_data > 0:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            query = "DELETE from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not dlt_data:
                return
        connct.commit()
        self.fetch_data()
        connct.close()

    #...................reset data............
    def rst_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_no_of_days.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")


    #.........................All Data Show.................
    def Show_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "This Number Not Found!!!!", parent=self.root)
            else:
                connct.commit()
                connct.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=70,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbls=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbls.place(x=70, y=0)

                #................Gender Show.................

                connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
                my_cursor = connct.cursor()
                query = ("select gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbls2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbls2.place(x=70, y=30)

                # ................Email Show.................

                connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@", database="management")
                my_cursor = connct.cursor()
                query = ("select email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lbls3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbls3.place(x=70, y=60)

                # ................Country Show.................

                connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
                my_cursor = connct.cursor()
                query = ("select country from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblcntry = Label(showDataframe, text="Country:", font=("arial", 12, "bold"))
                lblcntry.place(x=0, y=90)

                lbls4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbls4.place(x=70, y=90)

                # ................Address Show.................

                connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
                my_cursor = connct.cursor()
                query = ("select address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbls5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbls5.place(x=70, y=120)


    #....................search...............
    def search_system(self):
        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()

        my_cursor.execute("select * from room where contact="+ str(self.txt_search.get()))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            connct.commit()
        connct.close()



    def total(self):
        inDate=self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_no_of_days.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax=str("%.2f"%((q5)*0.1))+" Tk."
            sub_totl = str("%.2f" % (q5))+" Tk."
            ttotal=str("%.2f" % (q5+(q5*0.1)))+" Tk."
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(sub_totl)
            self.var_total.set(ttotal)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(500)
            q2 = float(700)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = str("%.2f" % ((q5) * 0.1)) + " Tk."
            sub_totl = str("%.2f" % (q5)) + " Tk."
            ttotal = str("%.2f" % (q5 + (q5 * 0.1))) + " Tk."
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(sub_totl)
            self.var_total.set(ttotal)
        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = str("%.2f" % ((q5) * 0.1)) + " Tk."
            sub_totl = str("%.2f" % (q5)) + " Tk."
            ttotal = str("%.2f" % (q5 + (q5 * 0.1))) + " Tk."
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(sub_totl)
            self.var_total.set(ttotal)
        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(1000)
            q2 = float(7000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = str("%.2f" % ((q5) * 0.1)) + " Tk."
            sub_totl = str("%.2f" % (q5)) + " Tk."
            ttotal = str("%.2f" % (q5 + (q5 * 0.1))) + " Tk."
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(sub_totl)
            self.var_total.set(ttotal)




if __name__ == '__main__':
    root=Tk()
    obj2=room_window(root)
    root.mainloop()