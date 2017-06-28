#!/bin/bash

prefix="192.168.95."
ip=2

while read -r name mac
do
   if [[ ${name:0:1} == "b" ]] ; then 
      echo " host $name{"
      echo "    hardware ethernet $mac;"
      echo "    fixed-address $prefix$ip;"
      echo "    option host-name \"eboron$ip\";"
      echo "    filename \"/pxelinux.0\";"
      echo " }"
      ip=$((ip + 1))
   fi
done < ~/boron-MAC.info

