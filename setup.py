import os
import subprocess
from subprocess import PIPE, Popen

try:
   proc = Popen(['iwconfig'], stdout=PIPE, stderr=subprocess.STDOUT)
except OSError:
   sys.exit(1)
hello = proc.communicate()[0]
for line in hello:
   yes = line.split('\n')
   if len(line) => 1:
      print("len(line) => 1")
   else:
      print("len(line) < 1")
