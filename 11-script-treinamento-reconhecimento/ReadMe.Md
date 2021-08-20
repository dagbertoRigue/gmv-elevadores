# Reconhecimento com Python e OpenCV

1. Instalar VisualStudio com os devidos pacotes para desenvolvimento em Python.
 - Acesse : https://visualstudio.microsoft.com/pt-br/ e baixe a versão atual para o sistema operacional.

2. Instale o Pycharm (instalação padrão - Community).
 - Acesse : https://www.jetbrains.com/

3. Instale opencv e opencv_contrib via cmd.
 - Abra o cmd;
 - Verifique a versão do pip : pip -V (a versão mínima suportada é a 19.3);
 - Caso a versão do pip seja inferior a 19.3, atualize : pip install --upgrade pip;
 - Instale o OpenCV: pip install opencv;
 - Instale a versão contrib : pip install opencv_contrib_python (acredito que, essa versão seja a completa e que não precise da operação anterior, 
   mas como eu já tinha executado o 'pip install opencv' antes e deu certo, descrevi aqui, dessa forma).

4. Teste a instalação das ferramentas.
 - Abra o Pycharm;
 - Crie um novo projeto e nele crie um arquivo teste.py;
 - Digite : 
	import cv2
	help(cv2.faces)
 - Run o programa. O log deverá trazer muitas informações, e finalizar o processo sem erros.

=============================================================================================

------- Passos para executar esse projeto -------
1. Instalar Cascade Train GUI :
   - Acesse : https://amin-ahmadi.com/cascade-trainer-gui/
   - Baixe a versão para o sistema operacional e faça a instalação padrão.
2. Preparar os dados para treinamento :
   - Criar conjunto de imagens positivas
   - Criar conjunto de imagens negativas
3. Exrcutar o script 'capturaBase'



Sequência dos scripts :
1. capturaBase.py

Continua...


























