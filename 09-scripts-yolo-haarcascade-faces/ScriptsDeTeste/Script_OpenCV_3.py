import cv2 as cv

carregaFace = cv.CascadeClassifier('../Haarcascade/haarcascade_frontalface_default.xml')
carregaEye = cv.CascadeClassifier('../Haarcascade/haarcascade_eye.xml')

imagem = cv.imread('../Fotos/imagem8.jpg')
imagemcinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemcinza)

print(faces)

for (x, y, l, a) in faces :
    leitura = cv.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)
    localEye =leitura[y:y+a, x:x + l]
    localEyeGray = cv.cvtColor(localEye, cv.COLOR_BGR2GRAY)
    detectado = carregaEye. detectMultiScale(localEyeGray, scaleFactor= 1.3, minNeighbors=9)

    for (ox, oy, ol, oa) in detectado :
        cv.rectangle(localEye, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv.imshow("Detecta a face e os olhos.", imagem)

cv.waitKey()