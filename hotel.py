from tkinter import*
from PIL import Image,ImageTk
from customer import cstmr_window
from room import room_window
from detail import room_details

class HotelManSys:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #.....1st pic.......

        img=Image.open(r"F:\Hotel\hotelpic.jpg")
        img=img.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #.....logo.........

        img2 = Image.open(r"F:\Hotel\logo2.jpg")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

        #.........title.........

        lbl_title=Label(self.root,text="Royal Hotel & Resort",font=("georgian",40,"bold","italic"),bg="navy blue",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=120,width=1550,height=80)

        #...........Main Frame...........
        hotel_frame=Frame(self.root,bd=4,relief=RIDGE)
        hotel_frame.place(x=0,y=190,width=1550,height=620)

        #............menu............
        lbl_menu = Label(hotel_frame,text="MENU",font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=0,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ...........Button Frame...........
        btn_frame = Frame(hotel_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=34, width=230, height=200)

        cstmr_btn = Button(btn_frame,text="CUSTOMER",command = self.cstmr_dtls,width=19,font=("times new roman", 16, "bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cstmr_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.room_dtls, width=19, font=("times new roman", 16, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        dtls_btn = Button(btn_frame, text="DETAILS",command=self.room_details, width=19, font=("times new roman", 16, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        dtls_btn.grid(row=2, column=0, pady=1)

        reprt_btn = Button(btn_frame, text="REPORT", width=19, font=("times new roman", 16, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        reprt_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=19, font=("times new roman", 16, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        #..........right side img.........

        img3 = Image.open(r"F:\Hotel\Receiption.jpg")
        img3 = img3.resize((1340, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(hotel_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1340, height=590)

        #..........Down Image............
        img4 = Image.open(r"F:\Hotel\outside_view.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(hotel_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=235, width=230, height=210)

        img5 = Image.open(r"F:\Hotel\food.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(hotel_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=426, width=230, height=190)

    def cstmr_dtls(self):
        self.new_window=Toplevel(self.root)
        self.app=cstmr_window(self.new_window)

    def room_dtls(self):
        self.new_window = Toplevel(self.root)
        self.app2 =room_window (self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app2 =room_details (self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=HotelManSys(root)
    root.mainloop()