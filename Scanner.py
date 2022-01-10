import cv2
from Database_Operations import  database
import pyzbar.pyzbar as pyzbar

def Qr_scan():
    img=cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX


    while True:
        success, frame= img.read()
        decoded=pyzbar.decode(frame)

        for object in decoded:
            (x,y,w,h)=object.rect
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            a2=database()
            rollno=str(object[0], 'utf-8')
            rollno_l=rollno.split('/')
            print(rollno_l)
            check=a2.verify(rollno_l[0],rollno_l[1])

            if(check==True):

                cv2.putText(frame,"DETECTED",(x,y),font,1,(0,255,0),2)

            else:
                cv2.putText(frame, "INVALID", (x, y), font, 1, (0, 255, 0), 2)


        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

Qr_scan()