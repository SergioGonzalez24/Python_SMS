from email import message
from time import sleep


import time
# with open("phones.txt") as r:
#     phones = r.readlines()
    
#     for phone in phones:
#         print(phone.strip())
#         sleep(1)
        
with open("message.txt") as r:
    message = r.read()
    
    print(message)
    
    
fones = open("phonesTest.txt", "r")
for phone in fones:
    print(phone.strip())
    sleep(1)