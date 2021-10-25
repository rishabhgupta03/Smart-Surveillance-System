import tkinter  as tk, threading

import tkinter.font as font
from PIL import Image, ImageTk
#import tkFont as tkfont

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

       # self.title_font = tkfont.Font(family='Helvetica', size=18, weight='bold', slant='italic')

        self.title("Smart Box Surveillance")
        self.iconphoto(False, tk.PhotoImage(file='Images/Icon-removebg-preview.png'))
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #for F in (StartPage):
        page_name = StartPage
        frame = StartPage(parent=container, controller=self)
        self.frames[page_name] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage )

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        icon = Image.open('Images/Icon.png')
        icon = icon.resize((250, 250), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        label_icon = tk.Label(self, image=icon).pack()
        self.grid(row=0, column=0, padx=(450, 450), pady=20)

        tk.Frame.__init__(self, parent)
        user_name = tk.Label(self, text="User ID").grid(row=0, column=0)
        user_pass = tk.Label(self, text="Password").grid(row=1, column=0)

        Log_in_button = tk.Button(self, text="Log in").grid(row=2, column=1)

        user_name_input_area = tk.Entry(self, width=30).grid(row=0, column=1, pady=3, padx=4)
        user_password_entry_area = tk.Entry(self, width=30, show='*').grid(row=1, column=1, pady=3, padx=4)

        self.grid(row=1, column=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()


