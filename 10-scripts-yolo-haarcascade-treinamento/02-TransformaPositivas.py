# Importando a biblioteca do cv2
import cv2
# Importando o módulo de sistema
import os
# Importando o módulo que trata os caminhos das imagens
from imutils import paths
# Importando o módulo que move arquivo de uma pasta para outra
import shutil

# Definindo uma função para o programa
def listPosImagem():
    # Criando uma lista dos itens contidas no diretório informado
    imagePath = list(paths.list_images('images/componente'))
    # Implementando um contador que será usado para percorrer a lista de imagens
    cont = 1

    # Cria um diretório 'neg' caso ainda não exista
    if not os.path.exists('pos'):
        os.makedirs('pos')
    # Para cada item 'i' da lista faça :
    for i in imagePath:
        # Copie a imagem, renomeie com o número atual do contador
        shutil.copy(i, i.replace(i, "pos/"+str(cont)+".png"))
        # Altere a imagem para a escala de cinza
        img = cv2.imread("pos/" + str(cont) + ".png", cv2.IMREAD_GRAYSCALE)
        # Redimensione a imagem para 200x200
        resized_image = cv2.resize(img, (200, 200))
        # Salva a imagem renomeada, em escala de cinza e redimensionada
        cv2.imwrite("pos/" + str(cont) + ".png", resized_image)

        # Imprime para conferência durante os testes
        print(i.replace(i, "pos/" + str(cont) + ".png"))

        # Incrementa o contador
        cont += 1


listPosImagem()