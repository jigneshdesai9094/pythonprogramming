term=input("enter any natural number : ")
num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(term)):
       c=term[i]
       if( not c in num):
           term=input("please,enter valid number")
           break
       i+=1
    if(i==len(term)):
        break   
sum=0
term=int(term)
for i in range(1,term+1):
    sum=sum+i
    
print("First Way : {0} natural number sum is : {1}".format(term,sum))
sum=int(term*(term+1)/2)
print("Second Way : {0} natural number sum is: {1}".format(term,sum))