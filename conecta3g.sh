#!/bin/bash
while true;
do
	ping -c1 google.com
	if [ $? -eq 0 ]
	then echo "Conectado!"
	else
		while [ -n $(/sbin/ifconfig wwan0)];
		do
			sleep 1
			echo "aguardando modem..."
		done
		echo "modem encontrado."

		sudo wvdial &

		while [ -n $(/sbin/ifconfig ppp0)];
		do
        		sleep 1
        		echo "aguardando conectar..."
		done
		route add default dev ppp0
	fi
	sleep 10
done
