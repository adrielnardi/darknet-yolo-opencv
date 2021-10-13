# biblioteca opencv
import cv2

# inicializar a webcam
cap = cv2.VideoCapture(0)

# exibi o conteúdo capturado das imagens , tornando a tela em tempo real
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    # captura da imagem
    ret, frame = cap.read()
    #exibe a imagem que esta armazenada em frame
    cv2.imshow("frame",frame)

# apertando q o programa sai
cap.release()
cv2.destroyAllWindows()
cv2.waiKey(1)

