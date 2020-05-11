import cv2
import numpy as np
cap = cv2.VideoCapture(1)
x = 100
y = 100
minrad = 15
a1 = 0.85
a2 = 1.25
e1 = 0.85
e2 = 1.25
aspect_ratio=0
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
    lowerball = np.array([28, 63, 44])
    upperball = np.array([100, 255, 255])

    kernal = np.ones((2, 2), np.uint8) / 4
    mask = cv2.inRange(hsv, lowerball, upperball)
    mask = cv2.erode(mask, kernal, iterations=4)
    mask = cv2.dilate(mask, kernal, iterations=6)
    mask = cv2.erode(mask, kernal, iterations=2)
    mask = cv2.filter2D(mask, -1, kernal)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    resgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(resgray, 127, 255, 0)
    conts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for c in conts:
        if len(conts)>0:
            m = cv2.moments(c)
            area = m['m00']
            if area >1000:
                 (x, y), r1 = cv2.minEnclosingCircle(c)
                 x=int(x)
                 y= int(y)
                 if(x is None or y is None):
                     pass
                 else:
                     #cv2.rectangle(frame, (x-100,y-100), (x+100,y+100), (0, 255, 0), 2)
                     newframe=frame[(y-100):(y+100), (x-100):(x+100)]
                     if newframe is None:
                         pass
                     else:
                         hsv = cv2.cvtColor(newframe, cv2.COLOR_BGR2HLS_FULL)
                         lowerball = np.array([28, 63, 44])
                         upperball = np.array([100, 255, 255])

                         kernal = np.ones((2, 2), np.uint8) / 4
                         mask = cv2.inRange(hsv, lowerball, upperball)
                         mask = cv2.erode(mask, kernal, iterations=4)
                         mask = cv2.dilate(mask, kernal, iterations=6)
                         mask = cv2.erode(mask, kernal, iterations=2)
                         mask = cv2.filter2D(mask, -1, kernal)
                         res = cv2.bitwise_and(newframe, newframe, mask=mask)
                         #gray = cv2.cvtColor(newframe, cv2.COLOR_BGR2GRAY)
                         #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.95, 300, param1=250, param2=20,minRadius=10, maxRadius=60)
                         #if circles is not None:
                             #detectedcircles = np.uint16(np.around(circles))
                             #for (x1, y1, r) in detectedcircles[0, :]:
                                #a=(r/r1)
                                 #if (a>0.8 and a<1.1):
                                     #cv2.circle(newframe, (x1, y1), r, (0, 255, 255), 3)
                                     #cv2.putText(newframe, '*BALL DETECTED*', (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5,(25, 2, 100), 1)
                     contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
                     HSV1 = cv2.bitwise_and(newframe, newframe, mask=mask)

                     for i in range(0, len(contours)):
                         if len(contours) > 1:
                             (x1, y1), radius = cv2.minEnclosingCircle(contours[i])
                             center = (int(x1), int(y1))
                             radius = int(radius)
                             x2, y2, w, h = cv2.boundingRect(contours[i])
                             aspect_ratio = float(w) / h
                             area1 = np.pi * radius * radius
                             area2 = cv2.contourArea(contours[i])
                             if (area1 != 0 and area2 != 0):
                                 e = area1 / area2
                             else:
                                 e = 0

                         if (aspect_ratio > a1 and aspect_ratio < a2 and e > e1 and e < e2 and minrad < radius):
                             frame = cv2.circle(newframe, center, radius, (255, 0, 0), 2)
                             frame = cv2.putText(newframe, "BALL DETECTED", (500, 25), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5, color=(0, 0, 255), thickness=2)

                     else:
                         pass

    cv2.imshow("frame", newframe)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
