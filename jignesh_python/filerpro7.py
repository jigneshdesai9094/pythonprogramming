#NOTE : replace gujarat programm to use finditer to replace  IMP
import re
fh = open("file8.txt","a+")
def add(name,phone,github):
    fh.write(name+" "+phone+" "+github+"\n")
    fh.flush()
def remove(name,phone,github):
    pattern ="{}\\s{}\\s{}\\s".format(name,phone,github)
    print(pattern)
    fh.seek(0)
    content = fh.read()
    print(content)
    match = re.search(pattern,content)
    if match:
     print(match)
     fh.seek(0)
     pre=fh.read(match.start())
     fh.seek(match.end()+1)
     after = fh.read()
     fh2 = open("file8.txt","w")
     fh2.writelines(pre)
     fh2.writelines(after)
     fh2.close()
     fh.seek(0)
     print("now Content : \n"+fh.read())
    else:
        print("record is Not Found")
def updatePhone(name,phone):
     pattern = "{}\\s\\w+\\s\\w+".format(name)
     fh.seek(0)
     content = fh.read()
     match = re.search(pattern,content)
     if match:
         print(match)
     else:
         print("record is not found")
def updateGithub(name,github):
    pass
def printByName(name):
    pass
def printAll():
    pass
def readAll():
    pass
l=True
while l:
    print("1.ADD")
    print("2.Remove")
    print("3.UpdatePhone")
    print("4.UpdateGithub")
    print("5.printNameoffriend")
    print("6.PrintAll")
    print("7.ReadAll")
    print("8.exit")
    choice  = int(input("Enter your choice"))
    if(choice == 1):
        name = input("Enter Friend Name : ")
        phone = input("Enter Mobile No : ")
        github = input("Enter GitHub Id : ")
        add(name,phone,github)
    elif(choice == 2):
        name = input("Enter Friend Name : ")
        phone = input("Enter Mobile No : ")
        github = input("Enter GitHub Id : ")
        remove(name,phone,github)
    elif(choice == 3):
         name = input("Enter Name : ")
         updatePhone(name)
    elif(choice ==4):
        pass
    elif(choice ==5):
        pass
    elif(choice ==6):
        pass
    elif(choice == 7):
        pass
    elif(choice == 8):
        l=False
    else:
        print("please,enter above one of number choice")
fh.close()

