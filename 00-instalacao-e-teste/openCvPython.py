# Primeiros passos :
# Autor : Dagberto Rigue


# 1º. Importar a biblioteca Python OpenCV, atribuindo um nome 'cv' e a biblioteca sys
import cv2 as cv
import sys

# 2º. Carregar a imagem usando a função 'cv.imread'.
# Primeiro argumento : local do arquivo
# Segundo argumento : opcional e especifica a formatação no qual queremos a imagem:
#   IMREAD_COLOR carrega a imagem no formato BGR de 8 bits. Este é o padrão usado aqui;
#   IMREAD_UNCHANGED carrega a imagem como está (incluindo o canal alfa, se houver);
#   IMREAD_GRAYSCALE carrega a imagem com intensidade.
img = cv.imread('componente.png', cv.IMREAD_GRAYSCALE)

# 3°. Opcionalmente, pode ser verificado se a imagem foi carregada corretamente.
if img is None:
    sys.exit("Não foi possível carregar a imagem.")

# 4º. Mostrar a imagem usando a função cv :: imshow .
# O primeiro argumento é o título da janela e o segundo argumento é o objeto cv :: Mat que será mostrado.
cv.imshow("ST-33", img)

# 5º. Para manter a janela aberta, usar a função cv.waitKey.
# Utiliza o parâmetro tempo em milissegundos para determitar quanto tempo a janela permanecerá aberta.
# '0' (zero) indica tempo infinito.
k = cv.waitKey(0)

# 6º.  Usar a função cv.imwrite para salvar a imagem em um arquivo.
# Usar como argumento o caminho do arquivo.

if k == ord("s" or "S"):
    cv.imwrite("componentesSalvos/st_33.png", img)
