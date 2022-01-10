import sqlite3
import tkinter  as tk
import tkinter.font as font
from tkinter import ttk,messagebox
import re

import Email
from in_out import in_out
from record import record
from identify import maincall
from find_motion import  find_motion
from PIL import Image, ImageTk
from rect_noise import rect_noise
from Database_Operations import database

import cv2
import pyzbar.pyzbar as pyzbar
import pyqrcode
import random as rd
import os
import Email

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title("Smart Box Surveillance")
        self.iconphoto(False, tk.PhotoImage(file='Images\main_icon.png'))
        self.geometry('1080x760')
        self.configure(bg='#4FBDBA')





        header = tk.Frame(self)
        self.icon = Image.open('Images\Main logo.png')
        self.icon = self.icon.resize((180, 78),Image.ANTIALIAS)
        self.icon = ImageTk.PhotoImage(self.icon)
        label_icon = tk.Label(header, image=self.icon)

        self.label_title = tk.Label(header, text="SMART SURVEILLANCE SYSTEM")
        self.label_font = font.Font(size=35, weight='bold', family='Helvetica')
        self.label_title['font'] = self.label_font
        self.label_title['bg'] = '#072227'
        self.label_title['fg'] = '#AEFEFF'

        header.columnconfigure(0, weight=4)
        header.columnconfigure(1, weight=2)
        header.columnconfigure(2, weight=4)

        label_icon.grid(row=0,column=0,sticky=tk.NW)
        self.label_title.grid(row=0, column=1,pady=(10, 10), sticky=tk.NW)
        header.config(bg="#072227")

        footer = tk.Frame(self)
        self.label_title = tk.Label(footer, text="Rights Reserved by @Nodmadic_Lad's team ")
        self.label_font = font.Font(size=8, weight='bold', family='Helvetica')
        self.label_title['font'] = self.label_font
        self.label_title['bg'] = '#072227'
        self.label_title['fg'] = '#4FBDBA'
        footer.columnconfigure(0,weight=1)
        self.label_title.grid(pady=(10, 10), column=0,sticky=tk.NS)
        footer.config(bg="#072227")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=9)
        self.rowconfigure(2,weight=1)

        header.grid(row=0,sticky="news")
        footer.grid(row=2, sticky="news")

        container = tk.Frame(self)
        container.config(bg="#4FBDBA")
        container.grid(row=1, column=0,padx=10, pady=(60, 95),sticky="NS")



        self.frames={}

        for F in (LoginPage, Mainmenu, RegisterPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.config(bg="#4FBDBA")
            frame.grid(row=1,padx=(130,10) ,sticky="NSEW")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent.rowconfigure(0,weight=1)
        parent.rowconfigure(1,weight=4)
        parent.rowconfigure(2,weight=2)
        parent.rowconfigure(3, weight=1)
        parent.rowconfigure(4, weight=2)

        self.icon = Image.open('Images\Login_Page.png')
        self.icon = self.icon.resize((130,100), Image.ANTIALIAS)
        self.icon = ImageTk.PhotoImage(self.icon)
        login_icon = tk.Label(self, image=self.icon)
        login_icon.grid(row=1, column=0,padx=(200,10),pady=(40,40), sticky=tk.NS)

        page_heading=tk.Label(self, text = "LOGIN PAGE")
        self.label_font = font.Font(size=30, weight='bold', family='Helvetica')
        page_heading['font'] = self.label_font
        page_heading['bg'] = '#4FBDBA'
        page_heading.grid(pady=(10, 10),padx=(220, 10),row=0, column=0, sticky=tk.NS)

        login=tk.Frame(self)

        user_id = tk.Label(login, text="User ID",bg='#4FBDBA',font=('Helvetica',12,'bold')).grid(row=0, column=0,pady=15)
        user_id = tk.Label(login, text="Password",bg='#4FBDBA',font=('Helvetica',12,'bold')).grid(row=1, column=0,pady=15)

        self.user_id= tk.Entry(login, width=20)
        self.user_id.grid(row=0, column=1, pady=15, padx=10)

        self.user_password= tk.Entry(login, width=20, show='*')
        self.user_password.grid(row=1, column=1, pady=15, padx=10)

        Log_in_button = tk.Button(login, text="Log in",bg='#000080',fg="#FDFDFD",width=20, command = lambda : self.check_login(controller)).grid(row=3, column=1,sticky=tk.NS)
        login.config(bg="#4FBDBA")
        login.grid(row=3,column=0,sticky=tk.NS,pady=(10,10),padx=(220,10))

        text=tk.Label(self, text = "OR")
        self.label_font = font.Font(size=10, weight='bold', family='Helvetica')
        text['font'] = self.label_font
        text['bg'] = '#4FBDBA'
        text.grid(pady=(5, 5),padx=(280,10),row=4, column=0, sticky=tk.NS)

        self.Qr_image = Image.open('Images/Buttons/anti theft.png')
        self.Qr_image = self.Qr_image.resize((150, 150), Image.ANTIALIAS)
        self.Qr_image = ImageTk.PhotoImage(self.Qr_image)
        QR_button = tk.Button(self, text="Scan QR-Code",bg="#000080",fg="#FDFDFD",width=22, command = lambda : self.Qr_Scan(controller)).grid(row=5, column=0,pady=(10,10),padx=(250,10), sticky=tk.NE)

    def check_login(self,controller):




        if(self.user_id.get()=="" or self.user_password.get()==""):
            messagebox.showerror("Empty Fields","All Fields required",parent=self)
        elif (len(str(self.user_id.get()))!=10):
            messagebox.showerror("Value Error", "User Id should be exactly of length 10", parent=self)
        elif(len(str(self.user_password.get()))!=8):
            messagebox.showerror("Value Error", "Password should be exactly of length 8", parent=self)

        elif(db.verify(uid=self.user_id.get(),pin=self.user_password.get())):
            d=database()
            d.set_status(uid=self.user_id.get(),status=1)


            controller.show_frame(Mainmenu)
        else:
            messagebox.showwarning("Log in Error","Wrong Credentials.Please try Again",parent=self)

    def Qr_Scan(self,controller):
        img = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            success, frame = img.read()
            decoded = pyzbar.decode(frame)

            for object in decoded:
                (x, y, w, h) = object.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                a2 = database()
                user_cred = str(object[0], 'utf-8')
                user_cred_l = user_cred.split('/')
                if(len(user_cred_l)<2):
                    check=False
                else:
                    check = a2.verify(user_cred_l[0], user_cred_l[1])
                cv2.putText(frame, "Press ESC to close this window.", (50, 50), font, 1, (255, 0, 0), 2)
                if (check == True):

                    cv2.putText(frame, "DETECTED", (x, y), font, 1, (0, 255, 0), 2)
                    controller.show_frame(Mainmenu)

                else:
                    cv2.putText(frame, "INVALID", (x, y), font, 1, (0, 255, 0), 2)


            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) == 27:
                break
        cv2.destroyAllWindows()


class Mainmenu(tk.Frame):
    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)
        self.btn1_image = Image.open('Images/Buttons/anti theft.png')
        self.btn1_image = self.btn1_image.resize((150, 150), Image.ANTIALIAS)
        self.btn1_image = ImageTk.PhotoImage(self.btn1_image)

        self.btn2_image = Image.open('Images/Buttons/face-recognition.png')
        self.btn2_image = self.btn2_image.resize((150, 150), Image.ANTIALIAS)
        self.btn2_image = ImageTk.PhotoImage(self.btn2_image)

        self.btn3_image = Image.open('Images/Buttons/record.png')
        self.btn3_image = self.btn3_image.resize((150, 150), Image.ANTIALIAS)
        self.btn3_image = ImageTk.PhotoImage(self.btn3_image)

        self.btn4_image = Image.open('Images/Buttons/visitors.png')
        self.btn4_image = self.btn4_image.resize((150, 150), Image.ANTIALIAS)
        self.btn4_image = ImageTk.PhotoImage(self.btn4_image)

        self.btn5_image = Image.open('Images/Buttons/restricted.png')
        self.btn5_image = self.btn5_image.resize((150, 150), Image.ANTIALIAS)
        self.btn5_image = ImageTk.PhotoImage(self.btn5_image)

        self.btn6_image = Image.open('Images/Buttons/exit.png')
        self.btn6_image = self.btn6_image.resize((150, 150), Image.ANTIALIAS)
        self.btn6_image = ImageTk.PhotoImage(self.btn6_image)

        # -----Button-------#

        btn_font = font.Font(size=18)
        btn1 = tk.Button(self, text='Anti-Theft', height=180, width=180, fg='white', bg='#090910', image=self.btn1_image,
                         compound='top', command=find_motion)
        btn1['font'] = btn_font
        btn1.grid(row=1, column=0, pady=(20, 10), padx=10)

        btn_font = font.Font(size=18)
        btn2 = tk.Button(self, text='Identify', height=180, width=180, fg='white', bg='#090910', image=self.btn2_image,
                         compound='top', command=maincall)
        btn2['font'] = btn_font
        btn2.grid(row=1, column=1, pady=(20, 10), padx=10)

        btn_font = font.Font(size=18)
        btn3 = tk.Button(self, text='Record', height=180, width=180, fg='white', bg='#090910', image=self.btn3_image,
                         compound='top', command=record)
        btn3['font'] = btn_font
        btn3.grid(row=1, column=2, pady=(20, 10), padx=10)

        btn_font = font.Font(size=18)
        btn4 = tk.Button(self, text='Visitors', height=180, width=180, fg='white', bg='#090910', image=self.btn4_image,
                         compound='top', command=in_out)
        btn4['font'] = btn_font
        btn4.grid(row=2, column=0, pady=(20, 10), padx=10)

        btn_font = font.Font(size=18)
        btn5 = tk.Button(self, text='Restricted Area', height=180, width=180, fg='white', bg='#090910',
                         image=self.btn5_image, compound='top', command=rect_noise)
        btn5['font'] = btn_font
        btn5.grid(row=2, column=1, pady=(20, 10), padx=10)

        btn_font = font.Font(size=18)
        btn6 = tk.Button(self, text='Close', height=180, width=180, fg='white', bg='#090910', command=super().quit,
                         image=self.btn6_image, compound='top')
        btn6['font'] = btn_font
        btn6.grid(row=2,column=2, pady=(20, 10), padx=10)

        tk.Button(self, text="Register New", bg="#000080", fg="#FDFDFD", command=lambda:controller.show_frame(RegisterPage)).grid(
            row=0, column=3, pady=(20, 40), sticky=tk.NE)

        self.config(bg='#214252')

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent.columnconfigure(0, weight=2)
        parent.columnconfigure(1, weight=4)

        page_heading = tk.Label(self, text="REGISTER NEW USER")
        self.label_font = font.Font(size=30, weight='bold', family='Helvetica')
        page_heading['font'] = self.label_font
        page_heading['bg'] = '#4FBDBA'
        page_heading.grid(pady=(10, 10), padx=(10, 10), row=0, column=0, sticky=tk.NS)


        register = tk.Frame(self)
        tk.Label(register, text="User Name", bg='#4FBDBA',font=('Helvetica',12)).grid(row=1, column=0,sticky=tk.NW,pady=(10,2))
        tk.Label(register, text=" Email ID", bg='#4FBDBA',font=('Helvetica',12)).grid(row=3, column=0,sticky=tk.NW,pady=(10,2))
        tk.Label(register, text="Phone", bg='#4FBDBA',font=('Helvetica',12)).grid(row=5, column=0,sticky=tk.NW,pady=(10,2))
        tk.Label(register, text="PIN", bg='#4FBDBA',font=('Helvetica',12)).grid(row=7, column=0,sticky=tk.NW,pady=(10,2))
        tk.Label(register,text="Confirm PIN",bg='#4FBDBA',font=('Helvetica',12)).grid(row=9, column=0,sticky=tk.NW,pady=(10,2))

        self.user_name = tk.Entry(register, width=70)
        self.user_name.grid(row=2, column=0, pady=5, padx=4,sticky=tk.NS,ipady=3)

        self.user_mail = tk.Entry(register, width=70)
        self.user_mail.grid(row=4, column=0, pady=5, padx=4,sticky=tk.NS,ipady=3)

        self.user_phone = tk.Entry(register, width=70)
        self.user_phone.grid(row=6, column=0, pady=5, padx=4,sticky=tk.NS,ipady=3)

        self.user_pass = tk.Entry(register, width=70,show='*')
        self.user_pass.grid(row=8, column=0, pady=5, padx=4,sticky=tk.NS,ipady=3)

        self.user_Cpass = tk.Entry(register, width=70, show='*')
        self.user_Cpass.grid(row=10, column=0, pady=5, padx=4,sticky=tk.NS,ipady=3)

        tk.Button(self, text="Register", bg="#000080", fg="#FDFDFD",width=20,command= lambda:self.input_database()).grid(row=11, column=0, pady=(20, 40), sticky=tk.NS)
        tk.Button(self, text="Back", bg="#000080", fg="#FDFDFD",command=lambda:controller.show_frame(Mainmenu)).grid(row=11,column=1,pady=(20,40),sticky=tk.NE)
        register.config(bg="#4FBDBA")
        register.grid(row=1, column=0, sticky=tk.NW)

    def input_database(self):
        regex_mail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        regex_phone=r'^[0-9]{10}$'

        if(self.user_name.get()=="" or
          self.user_mail.get()==""  or
          self.user_phone.get()=="" or
          self.user_pass.get()==""  or
          self.user_Cpass.get()==""):
            messagebox.showerror("Empty Fields", "All Fields required", parent=self)

        elif (not (re.fullmatch(regex_mail, (str(self.user_mail.get()))))):
            messagebox.showerror("Error", "Invalid Email ID", parent=self)
        elif(not (re.fullmatch(regex_phone, (self.user_phone.get())))):
            messagebox.showerror("Invalid Entry", "Enter valid phone number.", parent=self)
        elif(not(self.user_pass.get().isnumeric())):
            messagebox.showerror("Invalid Entry", "PIN can only contain numeric values.", parent=self)

        elif(self.user_pass.get()!=self.user_Cpass.get()) :
            messagebox.showerror("Error", "PIN Doesn't Match", parent=self)



        else:

            conn=sqlite3.connect("SURVEILLANCE_SYSTEM.db")
            crsr=conn.cursor()
            crsr.execute("""Select uid from USER""")
            check=crsr.fetchall()
            conn.commit()
            self.uid = rd.randint(1000000000, 9999999999)
            while (self.uid in check):
                self.uid = rd.randint(1000000000, 9999999999)

            d1=database()
            d1.record_input(uid=self.uid,name=self.user_name.get(),email=self.user_mail.get(),phone=self.user_phone.get(),pin=self.user_pass.get())
            self.Qr_code_gen()
            messagebox.showinfo("INFO", "Member Succesfully added. User ID and Qr-Code has been mailed.", parent=self)


    def Qr_code_gen(self):
        encode=str(self.uid)+"/"+str(self.user_pass.get())
        url=pyqrcode.create(encode)
        filename=str(self.uid)+".png"
        url.png(filename,scale=8)
        user_email=self.user_mail.get()
        msg="Use this User Id={} or QR-code for Log In in Future".format(self.uid)
        sub="Congratulation, you're succesfully registered"

        f_path=os.path.join(os.getcwd(),filename)
        print(f_path)
        Email.send_email(toaddr=self.user_mail.get(),body_msg=msg,sub_msg=sub,path=str(f_path),filename=filename)
        os.remove(f_path)



if __name__ == "__main__":

    db=database()
    db.set_all_status()
    app = tkinterApp()
    app.resizable(True, True)
    app.mainloop()