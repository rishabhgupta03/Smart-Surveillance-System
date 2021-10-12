import tkinter  as tk, threading
import imageio
import tkinter.font as font
from PIL import Image, ImageTk

video_path="starting.mp4"
video=imageio.get_reader(video_path)

def stream(label_1):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label_1.config(image=frame_image)
        label_1.image = frame_image

if __name__=="__main__":
    window=tk.Tk()
    window.title("Smart Box Surveillance")
    window.iconphoto(False,tk.PhotoImage(file='Images/Icon-removebg-preview.png'))
    window.geometry('1080x760')


    frame1=tk.Frame(window)
    label_1=tk.Label(frame1)
    label_1.pack()
    thread=threading.Thread(target=stream,args=(label_1,))
    thread.daemon=1
    thread.start()
    frame1.pack()
    window.mainloop()




