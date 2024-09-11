term=input("Enter No of Term : ")
while(True):
   if(term.isnumeric()):
     break
   else:
      term=input("Please enter valid term : ")
term=int(term)
pre='A'
nex='B'
print(pre,"",nex,end=" ")
for i in range(0,term):
   c=nex+pre
   print(c,end=" ")
   pre=nex
   nex=c
  