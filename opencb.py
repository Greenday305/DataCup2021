import cv2

img = cv2.imread("C:/Users/davis/OneDrive/Escritorio/Progra nuevo/Python libreria de trabajo/OpenCV/imagenmia.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)

#cap = cv2.VideoCapture()

lec = 1
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

