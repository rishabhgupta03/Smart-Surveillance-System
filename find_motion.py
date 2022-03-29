import cv2
from spot_diff import spot_diff
import time
from datetime import datetime
from Email import send_email
import os


def find_motion():

	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)



	check = []
	
	print("waiting for 2 seconds")
	time.sleep(2)
	frame1 = cap.read()

	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	## simultaneuosly recording #
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	rec_name=datetime.now().strftime("%H-%M-%S")
	out = cv2.VideoWriter(f'C:/Users/kunal/PycharmProjects/minor_rough/recordings/{rec_name}.avi', fourcc, 20.0, (640, 480))

	rec_path=os.path.join(os.getcwd(),f'recordings\{rec_name}.avi')


	##face recognition
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
		_, frm2 = cap.read()
		rec_frame=frm2.copy()
		frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)

		diff = cv2.absdiff(frm1, frm2)

		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at it
		contors = [c for c in contors if cv2.contourArea(c) > 25]


		if len(contors) > 5:
			cv2.putText(thresh, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			motion_detected = True
			is_start_done = False

		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				end = time.time()

			end = time.time()


			if (end - start) > 4:
				frame2 = cap.read()
				cap.release()
				cv2.destroyAllWindows()
				x = spot_diff(frame1, frame2, rec_path, rec_name)
				if x == 0:
					print("running again")
					return

				else:
					print("found motion")
					return

		else:
			cv2.putText(thresh, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		cv2.imshow("winname", thresh)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		# face recognition on recording
		gray = cv2.cvtColor(rec_frame, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.3, 2)

		for x, y, w, h in faces:
			cv2.rectangle(rec_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			roi = gray[y:y + h, x:x + w]

			label = recog.predict(roi)

			if label[1] < 100:
				cv2.putText(rec_frame, f"{labelslist[str(label[0])]}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
							3)
			else:
				cv2.putText(rec_frame, "unkown", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

		##recording timestamp writing
		cv2.putText(rec_frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX,0.6, (255, 255, 255), 2)
		out.write(rec_frame)



		if cv2.waitKey(1) == 27:

			break

	return
