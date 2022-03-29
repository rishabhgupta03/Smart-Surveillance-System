import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk

def collect_data(name,ids):


	count = 1


	cap = cv2.VideoCapture(0)

	filename = "haarcascade_frontalface_default.xml"

	cascade = cv2.CascadeClassifier(filename)

	while True:
		_, frm = cap.read()

		gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.4, 1)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
			roi = gray[y:y+h, x:x+w]

			cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
			count = count + 1
			cv2.putText(frm, f"{count}", (20,20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)
			cv2.imshow("new", roi)


		cv2.imshow("identify", frm)

		if cv2.waitKey(1) == 27 or count > 300:
			cv2.destroyAllWindows()
			cap.release()
			train()
			break

def train():
	print("training part initiated !")

	recog = cv2.face.LBPHFaceRecognizer_create()

	dataset = 'persons'

	paths = [os.path.join(dataset, im) for im in os.listdir(dataset)]

	faces = []
	ids = []
	labels = []
	for path in paths:
		labels.append(path.split('/')[-1].split('-')[0])

		ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))

		faces.append(cv2.imread(path, 0))

	recog.train(faces, np.array(ids))

	recog.save('model.yml')

	return

def identify():
	cap = cv2.VideoCapture('0')

	filename = "haarcascade_frontalface_default.xml"

	paths = [os.path.join("persons", im) for im in os.listdir("persons")]
	labelslist = {}
	for path in paths:
		labelslist[path.split('\\')[-1].split('-')[2].split('.')[0]] = path.split('\\')[-1].split('-')[0]

	print(labelslist)
	recog = cv2.face.LBPHFaceRecognizer_create()

	recog.read('model.yml')

	cascade = cv2.CascadeClassifier(filename)

	while True:
		_, frm = cap.read()

		gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.3, 2)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
			roi = gray[y:y+h, x:x+w]

			label = recog.predict(roi)

			if label[1] < 100:
				cv2.putText(frm, f"{labelslist[str(label[0])]}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
			else:
				cv2.putText(frm, "unkown", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

		cv2.imshow("identify", frm)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			cap.release()
			break


class train_entry(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("IDENTIFY")
        self.geometry('520x150')
        self.configure(bg='#AEFEFF')

        container = tk.Frame(self)

        container.config(bg="#AEFEFF")
        container.grid(row=0, column=0, padx=5, pady=(5, 5), sticky="EW")

        self.frames = {}

        for F in (ChoosePage,EnterPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.config(bg="#AEFEFF")
            frame.grid(row=1, padx=(5),pady=(5), sticky="NSEW")

        self.show_frame(ChoosePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class ChoosePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame1=tk.Frame(self)
        label = tk.Label(frame1, text="Select any option ", bg='#AEFEFF')
        label.grid(row=0, columnspan=2)
        label_font = font.Font(size=20, weight='bold', family='Helvetica')
        label['font'] = label_font

        btn_font = font.Font(size=10)

        button1 = tk.Button(frame1, text="Add Member ",bg='#000080',fg="#FDFDFD", command=lambda:controller.show_frame(EnterPage), width=20,height=1)
        button1.grid(row=1, column=0, pady=(10, 10), padx=(5, 5))
        button1['font'] = btn_font

        button2 = tk.Button(frame1, text="Start with known ",bg='#000080',fg="#FDFDFD", command=lambda:identify(), width=20,height=1)
        button2.grid(row=1, column=1, pady=(10, 10), padx=(5, 5))
        button2['font'] = btn_font
        frame1.grid(row=0,column=0,padx=(5),pady=(5),sticky="NW")
        frame1.config(bg="#AEFEFF")

class  EnterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame2=tk.Frame(self)
        tk.Label(frame2, text="Name", bg='#AEFEFF', font=('Helvetica', 10)).grid(row=0,column=0,pady=10)
        tk.Label(frame2, text="Unique ID", bg='#AEFEFF', font=('Helvetica', 10)).grid(row=1,column=0,pady=10)

        self.Person_name= tk.Entry(frame2, width=20)
        self.Person_name.grid(row=0, column=1, pady=10, padx=10)

        self.Person_id = tk.Entry(frame2, width=20)
        self.Person_id.grid(row=1, column=1, pady=10, padx=10)

        Train_button = tk.Button(frame2, text="Start Training", bg='#000080', fg="#FDFDFD", width=20,command=lambda:self.check_input()).grid(row=3, column=1,sticky=tk.NS)
        frame2.grid(row=0,column=0,padx=(5),pady=(5),sticky="NS")
        frame2.config(bg="#AEFEFF")
        self.config(bg="#AEFEFF")

    def check_input(self):
        if(self.Person_name.get()=="" or self.Person_id==""):
            messagebox.showerror("Empty Fields", "All Fields required", parent=self)
        elif(not(self.Person_id.get().isnumeric())):
            messagebox.showerror("ID can only be numeric", parent=self)
        else:
            collect_data(self.Person_name.get(),self.Person_id.get())




def maincall():
	app = train_entry()
	app.resizable(True, True)
	app.mainloop()
	return


