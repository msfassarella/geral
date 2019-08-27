#Python3
#Descricao: Funcionamento previsto para o Windows usando Python3
#           O scritp abrirPrograma.bat é colocado para inicializar junto com o Windows.
#           Ele executa o arquivo python executaPrograma.py, que é encarregado de 
#           abrir o programa desejado, aguardar um tempo e depois fecha-lo novamente, 
#           repetindo o ciclo posteriormente
#           

import subprocess
import time

while True:
   subprocess.Popen([r"cmd"])
   subprocess.Popen([r"C:\Program Files\mqttfx\mqttfx.exe"])

   #Arquivo alvo: sneck.exe
   #C:\Program Files (x86)\Snek\snek.vbs

   time.sleep(60*60)          # 60s * 60 = 1h   
   
   #Chama script para finalizar a aplicacao
   subprocess.Popen([r"C:\Users\msf\Desktop\echo.bat"])
   
   time.sleep(30)             #30s
