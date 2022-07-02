#!/bin/bash

echo "Translator Service Started"

/usr/bin/python3 /home/ubuntu/Translator/listen.py firsttime
sleep 5

while true
do
	/usr/bin/python3 /home/ubuntu/Translator/listen.py later
	sleep 5
done

