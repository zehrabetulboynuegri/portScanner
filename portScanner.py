# -*- coding: utf-8 -*-
import socket
import subprocess
import sys

from datetime import datetime


subprocess.call('clear', shell=True)

# Kullanıcıdan girdiler alınır.
targetHost    = raw_input("Hedef hostname ya da ip giriniz: ")
targetHostIP  = socket.gethostbyname(targetHost)
portRange = raw_input("Taramak istediğiniz port aralığını giriniz(ex: 1-65535): ").split("-")

minVal= int(portRange[0])
maxVal =int(portRange[1])



print "*" * 70
print "Please wait, scanning remote host", targetHostIP  
print "*" * 70

# Taramanın basladığı saati kontrol eder.
t1 = datetime.now()

# Açık portları listeler.

for port in range(minVal,maxVal):         
    try:
            sock = socket.socket()
            sock.connect((targetHostIP, port))
            print "Port {0}:     Open    ".format(port)
            sock.close()
    except socket.error:
        pass



# Zamanı tekrar kontrol eder.
t2 = datetime.now()

# Script çalışma süresi, kontrol edilen sürelerin farkı alınarak hesaplanır.
total =  t2 - t1

# Gecen süreyi ekrana yazar.
print 'Scanning Completed in: ', total