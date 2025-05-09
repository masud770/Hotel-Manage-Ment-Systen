from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class room_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management ")
        self.root.geometry("1295x550+230+220")

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

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",font=("times new roman", 20, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # ...........labels and entrys............

        # ..........Floor.......
        floor = Label(labelframeleft, text="Floor:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        floor.grid(row=0, column=0, sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor ,width=20, font=("times new roman", 12, "bold"))
        entry_floor.grid(row=0, column=1,sticky=W)

        # ..........room no.......
        room_no = Label(labelframeleft, text="Room no:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        room_no.grid(row=1, column=0, sticky=W,padx=20)

        self.var_room_no = StringVar()

        entry_room_no = ttk.Entry(labelframeleft,textvariable=self.var_room_no ,width=20, font=("times new roman", 12, "bold"))
        entry_room_no.grid(row=1, column=1,sticky=W)

        # ..........Room Type.......
        room_type = Label(labelframeleft, text="Room Type:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        room_type.grid(row=2, column=0, sticky=W,padx=20)

        self.var_room_type = StringVar()

        entry_room_type = ttk.Entry(labelframeleft,textvariable=self.var_room_type ,width=20, font=("times new roman", 12, "bold"))
        entry_room_type.grid(row=2, column=1,sticky=W)

        # ..............buttons................
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD",command=self.add_data,font=("arial", 12, "bold"), bg="green",fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1, pady=2)

        btnUpdate = Button(btn_frame, text="UPDATE",command=self.update ,font=("arial", 12, "bold"), bg="gold",fg="black", width=9)
        btnUpdate.grid(row=0, column=1, padx=1, pady=2)

        btnDelete = Button(btn_frame, text="DELETE",command=self.dlt_data,font=("arial", 12, "bold"), bg="red",fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1, pady=2)

        btnReset = Button(btn_frame, text="RESET", command=self.rst_data ,font=("arial", 12, "bold"), bg="purple",fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1, pady=2)

        # .................Table Frame And Search SYSTEM................
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE,text="Show Room Details",font=("times new roman", 20, "bold"), padx=2)
        table_frame.place(x=600, y=50, width=600, height=350)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("floor","room_no","room_type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("room_no", text="Room_No")
        self.room_table.heading("room_type", text="Room_Type")


        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("room_no",width=100)
        self.room_table.column("room_type",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error!!!","All fields are required!!",parent=self.root)
        else:
            try:
                connct=mysql.connector.connect(host="localhost",username="root",password="Sharkboy14757@",database="management")
                my_cursor=connct.cursor()
                my_cursor.execute("insert into room_details values(%s,%s,%s)",(
                    self.var_floor.get(),
                    self.var_room_no.get(),
                    self.var_room_type.get(),


                ))

                connct.commit()
                self.fetch_data()
                connct.close()
                messagebox.showinfo("Success!!!","New Room Added!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning!!!",f"Something went wrong:{str(es)}",parent=self.root)

   # ..........fetch data table............

    def fetch_data(self):
        connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
        my_cursor = connct.cursor()
        my_cursor.execute("SELECT * from room_details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            connct.commit()
        connct.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        cntent = self.room_table.item(cursor_row)
        row = cntent["values"]

        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])

        # .........................Update Data.................

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error!!!", "Please Enter Floor Number!!!", parent=self.root)
        else:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",database="management")
            my_cursor = connct.cursor()
            my_cursor.execute("UPDATE room_details set floor=%s,room_type=%s where room_no=%s", (

                    self.var_floor.get(),
                    self.var_room_type.get(),
                    self.var_room_no.get()


                ))
            connct.commit()
            self.fetch_data()
            connct.close()
            messagebox.showinfo("UPDATE!!!", "New Room Has Been Updated Successfully!!", parent=self.root)


        # ................Delete data.................

    def dlt_data(self):
        dlt_data = messagebox.askyesno("DELETE!!!", "Do You Want To Delete This Room???", parent=self.root)
        if dlt_data > 0:
            connct = mysql.connector.connect(host="localhost", username="root", password="Sharkboy14757@",
                                             database="management")
            my_cursor = connct.cursor()
            query = "DELETE from room_details where room_no=%s"
            value = (self.var_room_no.get(),)
            my_cursor.execute(query, value)
        else:
            if not dlt_data:
                return
        connct.commit()
        self.fetch_data()
        connct.close()


        # ...................reset data............

    def rst_data(self):
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")



if __name__ == '__main__':
    root=Tk()
    obj2=room_details(root)
    root.mainloop()