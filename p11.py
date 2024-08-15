no=input("Enter any valid  integer :")
num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(no)):
       c=no[i]
       if( not c in num):
           no=input("Enter any valid  integer : ")
           break
       i+=1
    if(i==len(no)):
        break 
no=int(no)
for i in range(2,int(no/2+1)):
    if(no%i==0):
        break
if(i==int(no/2)):
    print(no," number is Prime")
else:
    print(no," number is not Prime")