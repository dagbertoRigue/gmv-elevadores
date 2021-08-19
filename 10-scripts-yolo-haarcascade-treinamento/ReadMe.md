Treinamento para gerar o Haarcascade de objeto.
Precisa-se de imagens negativas e imagens negativas.

Utiliza-se uma imagem do objeto para ser sobreposta a todas as imagens negativas.

Após, rodar o arquivo 'info' que irá gerar todas as imagens positivas.

Todas as imagens deverão ser tratadas para a escala de cinza.

O conjunto de imagens principal é o conjunto de imagens negativas.


1. Collect Dataset
	-positive and negative
2. Create a folder 'pos' with positive images
3. Create a folder 'neg' with negative images
4. Use the Haar trainer GUI to train
	- specify the path
	- set stages
	- set width and height

Execute : 
01-TransformaNegativas.py (Gera as imagens Negativas)
02-TransformaPositivas.py (Gera as imagens Positivas)
03-CriaArquivoInfo.py ( Gera o arquivo bg.txt)

Abra o terminal (Ubuntu)
Execute : 
opencv_createsamples -img mask.jpg -bg bg.txt -info info/info.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1300

opencv_createsamples -info info/info.lst -num 1300 -w 20 -h 20 -vec positives.vec

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 650 -numNeg 900 -numStages 10 -w 20 -h 20

opencv_traincascade -data data -vec positives.vec -bg bg.txt -precalcValBufSize 256 -precalcIdxBufSize 256 -numPos 1200 -numNeg 1000 -nstages 20 -minhitrate 0.999 -maxfalsealarm 0.5 -w 50 -h 50 -nonsym -baseFormatSave

Rodar o programa e verificar a eficiência.






















