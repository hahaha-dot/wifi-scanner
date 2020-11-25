#Use it legally
#Don't use for illegal activities
#! /usr/bin/env python3

import pyfiglet
import sys
import time
   
result = pyfiglet.figlet_format("Port-Scanner", font = "slant"  ) 
print(result)
x = "WRITTEN BY WONG SOON HONG"
slowprint(x)
timesleep(1)
sys.stdout.flush()
print("WELCOME", end='\n')
print("Please choose option you want", end='\n')
print("[1] Open port scanner", end='\n')
print("[2] Exit", end='\n')
input = input(int("==>\n"))
if input == 1:
   print("Success to run")
else: 
   sys.exit(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(input("Enter format you want to scan", end='\n'))
special = print("Enter the ip address of target's that you comfirmed")
print("[2] Enter a file that contain ip address to scan")
selection = input(int("==>")
   if selection == 2
      path = input("Enter the file location")
   else:
      pass
real = open(path,'r')
really = real.readlines()
new = input(int("Enter port to scan"))
   for port in range(1,1025): 
      result = sock.connect_ex((special,new))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
                  
                  
