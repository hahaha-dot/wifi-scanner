#Use it legally
#Don't use for illegal activities

import logging
logging.getlogger("scapy.runtime").setLevel("logging.ERROR")
import sys

if len(sys.argv) !=4 :
   print("Usage: %s target startport endport" % sys.argv[0])
   sys.exit(0)
   
target = str(sys.argv[1])
startport = int(sys.argv[2])
endport = int(sys.argv[3])
print("Scanning" + target + "for its open TCP port")

if startport=endport
   endport+=1

for x in range(startport,endport):
   packet = IP(dst=target)/TCP(dport=x,flags='S')
   response = sr1(packet,timeout=0.5,verbose=0)
   if response.haslayer(TCP) and response.getlayer(TCP).flag==0x12
      print('Port ' + str(x) +' is openl')
  sr(IP(dst=target))/TCP(dport=response.sport,flag='R'),timeout=0.5,verbose=0
  
print("Scan is complet\n")
    
