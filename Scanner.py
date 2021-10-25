import cv2
import Database_operation as dt
import pyzbar.pyzbar as pyzbar

def Qr_scan():
    img=cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    prev_rollno=0

    while True:
        success, frame= img.read()
        decoded=pyzbar.decode(frame)

        for object in decoded:
            (x,y,w,h)=object.rect
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            a2=dt.database()
            rollno=str(object[0], 'utf-8')
            check=a2.verify(rollno)

            if(check==False):
                if(prev_rollno!=rollno):
                    a2=dt.database()
                    a2.attendance(rollno)
                cv2.putText(frame,"DETECTED",(x,y),font,1,(0,255,0),2)
                prev_rollno=rollno
            else:
                cv2.putText(frame, "INVALID", (x, y), font, 1, (0, 255, 0), 2)


        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

Qr_scan()
dt.database().display_attendance()