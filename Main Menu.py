import tkinter  as tk
import tkinter.font as font
from in_out import in_out
from record import record
from identify import maincall
from find_motion import  find_motion
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart Box Surveillance")
window.iconphoto(False, tk.PhotoImage(file='Images/Icon-removebg-preview.png'))
window.geometry('1080x760')
window.configure(bg='#5CDB95')

frame1=tk.Frame(window)
label_title = tk.Label(frame1, text="Smart Surveillance system")
label_font = font.Font(size=30, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)

frame2=tk.Frame(window)
icon=Image.open('Images/Main logo.png')
icon=icon.resize((100,38),Image.ANTIALIAS)
icon=ImageTk.PhotoImage(icon)
label_icon=tk.Label(frame2,image=icon)
label_icon.pack()

frame3=tk.Frame(window)

btn1_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn1_image=btn1_image.resize((50,50),Image.ANTIALIAS)
btn1_image=ImageTk.PhotoImage(btn1_image)

btn2_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn2_image=btn2_image.resize((50,50),Image.ANTIALIAS)
btn2_image=ImageTk.PhotoImage(btn2_image)


btn3_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn3_image=btn3_image.resize((50,50),Image.ANTIALIAS)
btn3_image=ImageTk.PhotoImage(btn3_image)


btn4_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn4_image=btn4_image.resize((50,50),Image.ANTIALIAS)
btn4_image=ImageTk.PhotoImage(btn4_image)


btn5_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn5_image=btn5_image.resize((50,50),Image.ANTIALIAS)
btn5_image=ImageTk.PhotoImage(btn5_image)

btn6_image=Image.open('Images/Buttons/Icon-removebg-preview.png')
btn6_image=btn6_image.resize((50,50),Image.ANTIALIAS)
btn6_image=ImageTk.PhotoImage(btn6_image)

#-----Button-------#

btn_font = font.Font(size=20)
btn1 = tk.Button(frame3, text='Anti-theft', height=90, width=180, fg='white',bg='#05386B', image=btn1_image, compound='left',command=find_motion)
btn1['font'] = btn_font
btn1.grid(row=1,column=0, pady=(20,10), padx=10)

btn_font = font.Font(size=20)
btn2 = tk.Button(frame3, text='Identify', height=90, width=180, fg='white',bg='#05386B', image=btn2_image, compound='left',command=maincall)
btn2['font'] = btn_font
btn2.grid(row=1,column=1, pady=(20,10), padx=10)

btn_font = font.Font(size=20)
btn3 = tk.Button(frame3, text='Record', height=90, width=180, fg='white',bg='#05386B', image=btn3_image, compound='left',command=record)
btn3['font'] = btn_font
btn3.grid(row=1,column=2, pady=(20,10),padx=10)

btn_font = font.Font(size=20)
btn4 = tk.Button(frame3, text='Visitors', height=90, width=180, fg='white',bg='#05386B', image=btn4_image, compound='left',command=in_out)
btn4['font'] = btn_font
btn4.grid(row=2,column=0, pady=(20,10), padx =10)

btn_font = font.Font(size=20)
btn5 = tk.Button(frame3, text='Register', height=90, width=180, fg='white',bg='#05386B', image=btn5_image, compound='left')
btn5['font'] = btn_font
btn5.grid(row=2,column=1, pady=(20,10), padx =10)

btn_font = font.Font(size=20)
btn6 = tk.Button(frame3, text='Close', height=90, width=180, fg='white',bg='#05386B',command=window.quit, image=btn6_image ,compound='left')
btn6['font'] = btn_font
btn6.grid(row=2, pady=(20,10),padx=10, column=2)

frame1.grid(row=0,column=1,pady=(10,100),padx=450)
frame2.grid(row=0,column=0)
frame3.grid(row=1, column=1)


window.mainloop()