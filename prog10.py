no=int(input("Enter Any Number"))
print(no,end=" ")
while(no!=1):
    if(no%2==0):
        no=int(no/2)
        print(no,end=" ")
    else:
        no=(no*3)+1
        print(no,end=" ")