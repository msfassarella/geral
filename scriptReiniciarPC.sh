  GNU nano 2.5.3                                         Arquivo: /opt/devix/scriptReiniciarPC                                                                                            

#!/bin/bash
# Script to test internet conection
# Last revised 12/12/2017
#================================================================
#- IMPLEMENTATION
#-    version         ${SCRIPT_NAME} 1.0
#-    author          Marcelo Fassarella
#-    copyright       Copyright (c) 2017 Devix Tecnologia - All Rights Reserved
#-    license         
#-    script_id       12122017
#-
#================================================================
#  HISTORY
#     2017/12/12 : Script creation
# 
#================================================================
while :
do
    #7200 2h 
    sleep 7200  
    ping www.google.com.br -c 1 >/dev/null;
    if [ "$?" = "0" ] ;
    then
        echo "Conexao ativa";
    else
        echo "Restabelecendo a conexão"
        reboot
    fi
    
done
