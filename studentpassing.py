
students=int(input("How Many Students : "))
p=0
i=1
while(i<=students):
    m=int(input("Enter {} Student Marks : ".format(i)))
    if(m>100 or m<0):
        print("please,enter valid student marks")
        continue
    if(m>=40):
        p+=1
    i+=1    
print("Percantage of Passing Students {}%".format((p*100)/students))
    