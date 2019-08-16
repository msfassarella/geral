
#!/bin/bash

while :
do
  vpnAtiva=`ifconfig | grep tun`  #comando certo
  #vpnAtiva=`ifconfig | grep xun` #comando errado para teste

  PING="ping 10.8.0.1 -c 1"     #comando certo
  #PING="ping 192.168.200.250 -c 1"  #comando errado para teste
  #RESPOSTA="Unreachable"
  RESPOSTA="1\spackets\stransmitted,\s0\sreceived"
  pingResposta=`$PING | grep $RESPOSTA`
  echo $pingResposta
  echo $vpnAtiva

  if  [ "$vpnAtiva" ]; then
    echo "VPN CONECTADA"
   #pingResposta=`$PING`
   #echo $pingResposta
    if [ "$pingResposta" ]; then
      echo "perdido"
      nmcli connection down Node01-Devix
      sleep 10
      echo "network restart"
      "/etc/init.d/network-manager restart"
      sleep 20
      nmcli connection up Node01-Devix
    else
      echo "respondeu"
    fi
  else 
   echo "VPN FORA"
   echo ":network restart" 
   "/etc/init.d/network-manager restart"
   sleep 20
   nmcli connection up Node01-Devix
  fi
  echo "fim"
  sleep 60
done




