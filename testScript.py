#!/bin/python

prefix = "192.168.95."
ip = 2
f = open("boron-MAC.info", "r")
for line in f:
   if (line[0] == "b"):
      line = line.split()
      print "host " + line[0] + " {"
      print "   hardware ethernet " +  line[1] + ";"
      print "   fixed-address " + prefix + str(ip) + ";"
      print "   option host-name \"e" + line[0] + "\";"
      print "   filename \"/pxelinux.0\";"
      print "}"
      ip+=1
   

