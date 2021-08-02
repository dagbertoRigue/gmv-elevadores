import cv2 as cv

webcam = cv.VideoCapture(0)
classificadorVideoFace = cv.CascadeClassifier('../Haarcascade/haarcascade_frontalface_default.xml')
classificadorOlho = cv.CascadeClassifier("../Haarcascade/haarcascade_eye.xml")

while True:
    camera, frame = webcam.read()

    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    detecta = classificadorVideoFace.detectMultiScale(cinza)
    for (x, y, l, a) in detecta:
        cv.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)
        pegaOlho = frame[y:y + a, x:x + l]
        OlhoCinza = cv.cvtColor(pegaOlho, cv.COLOR_BGR2GRAY)
        localizaOlho = classificadorOlho.detectMultiScale(OlhoCinza)
        for (ox, oy, ol, oa) in localizaOlho:
            cv.rectangle(pegaOlho, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
    cv.imshow("Imagem WebCam", frame)
    if cv.waitKey(1) == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()










