import pywhatkit
import string



message = open("message.txt", "r")
fones = open("phones.txt", "r")
m = message.read()
for phone in fones:
    print(m)

    print(phone.strip())
    
    pywhatkit.sendwhatmsg_instantly(phone.strip(),m,10,True,4)

