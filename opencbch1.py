import cv2

""" img = cv2.imread("imagenmia.jpg")

cv2.imshow("Mi imagen",img)
cv2.waitKey(0) """

cap = cv2.VideoCapture("callfaitel.mp4")
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    if img is not False:
    	cv2.imshow("Video", img)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break
    else:
    	break

lec = 0
#Leer de camara:
if lec == 1:
    cv2.namedWindow("Camarilla")
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        cv2.imshow("Camarilla", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # Se cierra si le picas a ESC
            break
    vc.release()
    cv2.destroyWindow("Camarilla")

