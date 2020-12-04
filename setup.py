import re

def hello():
    with open('/home/kali/Desktop/list.txt', 'r') as f:
        re.compile('\s+')
        
        f_content = f.read()
        repair = f_content.replace(' ', '').split()
        if len(repair) >= 8:
              print(repair)
        else:
              continue
        
hello()
