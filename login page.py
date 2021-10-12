import tkinter  as tk, threading
import imageio
import tkinter.font as font
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart Box Surveillance")
window.iconphoto(False, tk.PhotoImage(file='Images/Icon-removebg-preview.png'))






frame_image2 = ImageTk.PhotoImage(Image.open("Images/Icon.png"))
label_2=tk.Label(window,image=frame_image2)
label_2.image = frame_image2
label_2.grid(row=0,column=1,pady=(10,10))

user_name=tk.Label(window,text="Username").grid(row=1,column=1)

user_pass=tk.Label(window,text="Password").grid(row=2,column=1)

Log_in_button=tk.Button(window,text="Log in").grid(row=3,column=1)

user_name_input_area = tk.Entry(window,width = 30).grid(row=1,column=2, pady=3)

user_password_entry_area = tk.Entry(window,width = 30).grid(row=2,column=2,pady=3)



window.mainloop()
