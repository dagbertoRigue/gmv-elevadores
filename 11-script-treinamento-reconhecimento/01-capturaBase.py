# Script para capturar as imagens que serão usadas para gerar um classificador.
# Crie uma pasta nomeada de 'FotosParaClassificador' dentro do projeto

# Importando a biblioteca OpenCV, módulo de sistema, módulo que trata os caminhos das imagens,
# e o módulo que move arquivo de uma pasta para outra
import cv2
import os
from imutils import paths
import shutil

# Definindo a câmera
WebCamera = cv2.VideoCapture(1)

# Iniciando amostra = 1
amostra = 1
# Definindo número de amostras (25 é o mínimo, mas o ideal é trabalhar com aproximadamente de 200)
numeroAmostras = 200
# Solicita o número identificador (usado para separar um item de outro)
id = input("Digite seu identificador: ")

while True:
    # Conecta na câmera
    conectado, imagem = WebCamera.read()
    # Transforma para escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    for (x, y, l, a) in faceDetectadas:
        # Cria o retângulo ao identificar o objeto
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        # Definimos a tecla c para capturar a imagem
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # Ajustando dimensão da imagem para 220x220pxl
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (220, 220))
            # Salva a imagem na pasta 'Fotos' concatenando com o id, o número da amostra e a extensão
            cv2.imwrite("Fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            # Para fins de conferência, imprime a confirmação da captura no log.
            print("[Foto " + str(amostra) + " capturada com sucesso]")
            # Incrementa a variável amostra
            amostra += 1

    # Abre uma janela com a imagem da câmera
    cv2.imshow("Face", imagem)
    # Define a tecla 1 para parar o programa
    cv2.waitKey(1)
    # Se o número da amostra atingir o limite definido para o programa
    if  (amostra >= numeroAmostras + 1):
        break
print("Faces capturadas com sucesso")
#Encerra a janela da câmera
WebCamera.release()
cv2.destroyAllWindows()