#!/usr/lib/dev python
#_*_coding="utf-8"_*_
from ftplib import FTP
import socket 
import os 
import time 
#Creamos variables 

CLA="\x1b[5;30;42m"
CLV="\x1b[5;30;42m"
CLR="\x1b[5;31;40m"
CLC="\x1b[3;33;40m"
ZR="\x1b[0m"
print "%s\t\t//////////////////////////////////////////%s"%(CLC,ZR)
print "%s\t\t///Autor:sn0b3nz correo:s4ndr01@tuta.io///%s"% (CLC,ZR)
print "%s\t\t//////////////////////////////////////////%s"%(CLC,ZR)
def conecion():
     print '%sConectando dominio%s'%(CLA,ZR)
     sockets=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sockets.connect(("www.sitio.com",80))
     print ""
     f="i"
     if f == "i": 
         #ingresando manualmente la direccion del ftp
         ftpl=raw_input(ftp@serve> ')
         ftp=FTP(ftpl)
         #ftp.connect()
         print "ingrese datos"
         xfor=raw_input('user#root> ')
         xfor2=raw_input('password#root> ')
         ftp.login (xfor,xfor2)
         #ftp=FTP(host,user,passw)
         print "Conectado a ftp"
         try:   
            #creamos una carpeta 
            ftp.mkd('carpeta')
         except:
            #si ya exige entonces omite
            #abre carpeta  o cambia de directorios 
            ftp.cwd('carpeta')
            #muestras directorios 
            ftp.dir()
            #cierra conexion
            ftp.close()
          #ejecuta si hay algun error 

#llamamos al la funcion actual 
if __name__=="__main
       #se ejecuta 
       conecion()
      #if ="i":
          # print "[%s+%s]Error"% (CLR,ZR
