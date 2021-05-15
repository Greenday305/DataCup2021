import cv2
import numpy as np

img = cv2.imread("imagenmia.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Esta convierte el color de la imagen a gris
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #Este le hace un blur Gaussiano a la imagen
imgCanny = cv2.Canny(img,100,100) #Canny detecta bordes
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #Dialation es para hacer los bordes más gruesos

cv2.imshow("Imagen Normal",img)
cv2.imshow("Imagen en gris", imgGray)
cv2.imshow("Imagen blurreada con funcion Gaussiana", imgBlur)
cv2.imshow("Canny que detecta bordes", imgCanny)
cv2.imshow("Dialation para bordes más gruesos", imgDialation)
cv2.waitKey(0)