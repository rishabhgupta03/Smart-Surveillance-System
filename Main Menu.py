import tkinter  as tk
import tkinter.font as font
from in_out import in_out
from record import record
from identify import maincall
from find_motion import  find_motion
from PIL import Image, ImageTk
from rect_noise import rect_noise

window = tk.Tk()
window.title("Smart Box Surveillance")
window.iconphoto(False, tk.PhotoImage(file='Images\main_icon.png'))
window.geometry('1080x760')
window.configure(bg='#BD4B4B')

frame1=tk.Frame(window)
label_title = tk.Label(frame1, text="Smart Surveillance system")
label_font = font.Font(size=23, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title['bg']='#BD4B4B'
label_title.grid(pady=(10,10), column=2)
frame1.config(bg="#132743")

frame2=tk.Frame(window)
icon=Image.open('Images\main_icon.png')
icon=icon.resize((65,65),Image.ANTIALIAS)
icon=ImageTk.PhotoImage(icon)
label_icon=tk.Label(frame2,image=icon)
label_icon.pack()

frame3=tk.Frame(window)

btn1_image=Image.open('Images/Buttons/anti theft.png')
btn1_image=btn1_image.resize((150,150),Image.ANTIALIAS)
btn1_image=ImageTk.PhotoImage(btn1_image)

btn2_image=Image.open('Images/Buttons/face-recognition.png')
btn2_image=btn2_image.resize((150,150),Image.ANTIALIAS)
btn2_image=ImageTk.PhotoImage(btn2_image)


btn3_image=Image.open('Images/Buttons/record.png')
btn3_image=btn3_image.resize((150,150),Image.ANTIALIAS)
btn3_image=ImageTk.PhotoImage(btn3_image)


btn4_image=Image.open('Images/Buttons/visitors.png')
btn4_image=btn4_image.resize((150,150),Image.ANTIALIAS)
btn4_image=ImageTk.PhotoImage(btn4_image)


btn5_image=Image.open('Images/Buttons/restricted.png')
btn5_image=btn5_image.resize((150,150),Image.ANTIALIAS)
btn5_image=ImageTk.PhotoImage(btn5_image)

btn6_image=Image.open('Images/Buttons/exit.png')
btn6_image=btn6_image.resize((150,150),Image.ANTIALIAS)
btn6_image=ImageTk.PhotoImage(btn6_image)

#-----Button-------#

btn_font = font.Font(size=18)
btn1 = tk.Button(frame3, text='Anti-Theft', height=180, width=180, fg='white',bg='#090910', image=btn1_image, compound='top',command=find_motion)
btn1['font'] = btn_font
btn1.grid(row=1,column=0, pady=(20,10), padx=10)

btn_font = font.Font(size=18)
btn2 = tk.Button(frame3, text='Identify', height=180, width=180, fg='white',bg='#090910', image=btn2_image, compound='top',command=maincall)
btn2['font'] = btn_font
btn2.grid(row=1,column=1, pady=(20,10), padx=10)

btn_font = font.Font(size=18)
btn3 = tk.Button(frame3, text='Record', height=180, width=180, fg='white',bg='#090910', image=btn3_image, compound='top',command=record)
btn3['font'] = btn_font
btn3.grid(row=1,column=2, pady=(20,10),padx=10)

btn_font = font.Font(size=18)
btn4 = tk.Button(frame3, text='Visitors', height=180, width=180, fg='white',bg='#090910', image=btn4_image, compound='top',command=in_out)
btn4['font'] = btn_font
btn4.grid(row=2,column=0, pady=(20,10), padx =10)

btn_font = font.Font(size=18)
btn5 = tk.Button(frame3, text='Restricted Area', height=180, width=180, fg='white',bg='#090910', image=btn5_image, compound='top',command=rect_noise)
btn5['font'] = btn_font
btn5.grid(row=2,column=1, pady=(20,10), padx =10)

btn_font = font.Font(size=18)
btn6 = tk.Button(frame3, text='Close', height=180, width=180, fg='white',bg='#090910',command=window.quit, image=btn6_image ,compound='top')
btn6['font'] = btn_font
btn6.grid(row=2, pady=(20,10),padx=10, column=2)

frame3.config(bg='#214252')




frame1.grid(row=0,column=1,pady=(5,95),padx=10)
frame2.grid(row=0,column=0,padx=10,pady=(5,95))
frame3.grid(row=1, column=2,padx=50)





window.mainloop()