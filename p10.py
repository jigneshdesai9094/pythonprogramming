no=input("Enter Any Number :")
num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(no)):
       c=no[i]
       if( not c in num):
           no=input("Enter Any Number : ")
           break
       i+=1
    if(i==len(no)):
        break 
no=int(no)
print(no,end=" ")
while(no!=1):
    if(no%2==0):
        no=int(no/2)
        print(no,end=" ")
    else:
        no=(no*3)+1
        print(no,end=" ")