import cv2 as cv

carregaAlgoritmo = cv.CascadeClassifier('../Haarcascade/haarcascade_frontalface_default.xml')

imagem = cv.imread('../Fotos/imagem2.jpg')

imagemcinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagemcinza, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))

print(faces)

for (x, y, l, a) in faces :
    cv.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

cv.imshow("Faces", imagem)

cv.waitKey()