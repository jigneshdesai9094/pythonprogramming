term=input("enter any  number  of term: ")
num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(term)):
       c=term[i]
       if(not c in num):
           term=input("please,enter valid number of term ")
           break
       i+=1
    if(i==len(term)):
        break   
term=int(term)
pre=1
next=0
sum=0
print("Fibonacci Series : ")
for i in range(term):
    sum=pre+next
    print(sum,end=" ")
    pre=next
    next=sum