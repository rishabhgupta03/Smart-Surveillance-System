import tkinter  as tk, threading

import tkinter.font as font
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart Box Surveillance")
window.iconphoto(False, tk.PhotoImage(file='Images/Icon-removebg-preview.png'))

frame1=tk.Frame(window)
icon=Image.open('Images/Icon.png')
icon=icon.resize((250,250),Image.ANTIALIAS)
icon=ImageTk.PhotoImage(icon)
label_icon=tk.Label(frame1,image=icon)
label_icon.pack()




frame2=tk.Frame(window)
user_name=tk.Label(frame2,text="User ID").grid(row=0,column=0)
user_pass=tk.Label(frame2,text="Password").grid(row=1,column=0)

Log_in_button=tk.Button(frame2,text="Log in").grid(row=2,column=1)

user_name_input_area = tk.Entry(frame2,width = 30).grid(row=0,column=1, pady=3,padx=4)
user_password_entry_area = tk.Entry(frame2,width = 30,show='*').grid(row=1,column=1,pady=3,padx=4)



frame3=tk.Frame(window)
Choice=tk.Label(frame3,text="OR")
Choice.grid(row=0,column=0)
QR_Scan_btn = tk.Button(frame3, text='Scan QR-Code', height=2, width=10, fg='white',bg='#05386B', compound='left')
QR_Scan_btn.grid(row=1,column=0,pady=(40,40))

frame1.grid(row=0,column=0,padx=(450,450),pady=20)
frame2.grid(row=1,column=0)
frame3.grid(row=2,column=0,pady=(40,40))

window.mainloop()
