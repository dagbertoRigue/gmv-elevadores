# Importando a biblioteca do cv2
import cv2
# Importando o módulo de sistema
import os
# Importando o módulo que trata os caminhos das imagens
from imutils import paths
# Importando o módulo que move arquivo de uma pasta para outra
import shutil




webcam = cv2.VideoCapture(1)

while True:
        # Captura da camera frame por frame
        _, frame = webcam.read()
        cv2.imshow("Imagem WebCam", frame)
        if cv2.waitKey(1) == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()






