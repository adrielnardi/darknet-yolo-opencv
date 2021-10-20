# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:05:27 2021
@author: sandr
"""
#Instale utilizando o Python 
# utilizando o Anaconda.
#Desta forma, já serão inclusos os
# pacotes mais importantes de Data Science.
#Importe a biblioteca CpenCV
#conda install opencv
import cv2

#Em seguida a primeira coisa é inicializar a webcam.
#Isso pode ser feito utilizando o comando 
# cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

#Para exibir o conteúdo da webcam em tempo real,
# você precisamos colocar os comandos de
# exibição da imagem capturada pela web cam
# dentro de um while loop:
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    
    #Agora, vamos capturar a imagem
    # a partir de sua webcam. 
    #Isso pode ser feito a partir do método
    # cap.read
    ret, frame = cap.read()
    
    #A imagem que esta sendo capturada
    # esta armazenada em frame.
    #Agora para visualizar esta imagem,
    # basta chamar a função imshow 
    # combinada com waitKey que já está
    # no while
    cv2.imshow('frame', frame)

#Quando você digitar a letra q
# seu código sairá do while
cap.release()
#O destry irá fechar a execução
# da webcam e encerrar seu codigo
cv2.destroyAllWindows()
cv2.waitKey(1)
