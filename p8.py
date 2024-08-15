students=input("How Many Students : ")

num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(students)):
       c=students[i]
       if( not c in num):
           students=input("please,enter valid student:")
           break
       i+=1
    if(i==len(students)):
        break  
p=0
i=1
students=int(students)
while(i<=students):
    m=input("Enter {} Student Marks : ".format(i))
    while(1):
     t=0
     while(t<len(m)):
       c=m[t]
       if( not c in num):
           m=input("please,enter valid student marks")
           break
       t+=1
       
     if(t==len(m)):
        break 
    m=int(m) 
    if(m>100 or m<0):
        print("please,enter valid student marks")
        continue
    if(m>=40):
        p+=1
    i+=1    
print("Percantage of Passing Students {}%".format((p*100)/students))