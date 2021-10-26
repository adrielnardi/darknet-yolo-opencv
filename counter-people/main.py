import numpy as np
import cv2

def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

detects = []

posL = 150
offset = 30

xy1 = (20, posL)
xy2 = (300, posL)


total = 0

''
    cv2.line(frame,xy1,xy2,(255,0,0),3)

    cv2.line(frame,(xy1[0],posL-offset),(xy2[0],posL-offset),(255,255,0),2)

    cv2.line(frame,(xy1[0],posL+offset),(xy2[0],posL+offset),(255,255,0),2)

    contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)

        area = cv2.contourArea(cnt)
        
        if int(area) > 3000 :
            centro = center(x, y, w, h)

            cv2.putText(frame, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
            cv2.circle(frame, centro, 4, (0, 0,255), -1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            if len(detects) <= i:
                detects.append([])
            if centro[1]> posL-offset and centro[1] < posL+offset:
                detects[i].append(centro)
            else:
                detects[i].clear()
            i += 1

    if i == 0:
        detects.clear()

    i = 0

    if len(contours) == 0:
        detects.clear()

    else:

        for detect in detects:
            for (c,l) in enumerate(detect):


                if detect[c-1][1] < posL and l[1] > posL :
                    detect.clear()
                    up+=1
                    total+=1
                    cv2.line(frame,xy1,xy2,(0,255,0),5)
                    continue

                if detect[c-1][1] > posL and l[1] < posL:
                    detect.clear()
                    down+=1
                    total+=1
                    cv2.line(frame,xy1,xy2,(0,0,255),5)
                    continue

                if c > 0:
                    cv2.line(frame,detect[c-1],l,(0,0,255),1)

    cv2.putText(frame, "TOTAL: "+str(total), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
    cv2.putText(frame, "SUBINDO: "+str(up), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),2)
    cv2.putText(frame, "DESCENDO: "+str(down), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
