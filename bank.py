import random
import getpass
print("press r for register or press s for signin")
a=input()
b=[]
f={}
def register():
    choice=list(range(1000,10000))
    random.shuffle(choice)
    d=choice.pop()
    print("your unique code :",d)
    e=getpass.getpass("enter the password")
    f.update({d:e})
    print(f)
def signin():
    g=int(input("enter the unique code"))
    h=input("enter the password")
    if g in f and h==f[g]:
        print("login successful")
    else:
        print("login failed")
while a=='r'or a=='s':
    if a=='r':
       print("enter the gmailid")
       c=input()
       if '@gmail.com' in c:
                  if c in b:
                     print("account already exist")
                  else:
                     b.append(c)
                     register()
       else:
            print("enter valid gmailid")
    elif a=='s':
       signin()
    print("r for register or s for sigin or q for quit")    
    a=input()
    
    

