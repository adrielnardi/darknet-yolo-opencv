import cv2  #importa opencv
import numpy as np #importa operador matemático numpy

cap = cv2.VideoCapture(0) #define variável de captura de vídeo
#obs: 0 é webcam do note, podemos colocar entre "" variável local ip

while True:

	_, frame = cap.read() # cap.read() le a imagem e grava no retorno(_) e no frame em cada segundo

	cv2.imshow("frame", frame) #mostra o frame da camera

	key = cv2.waitKey(1) #espera a resposta em 1 miléssimo de segundo do delay

	if key == 27: #27 é o botão esc do teclado para dar um break e sair do loop
		break

cap.release() #release libera o cap
cv2.destroyAllWindows() #destroi as janelas do windows