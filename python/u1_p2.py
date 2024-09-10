term=int(input("Enter term : "))
pre='A'
nex='B'
print(pre,"",nex,end=" ")
for i in range(0,term):
   c=nex+pre
   print(c,end=" ")
   pre=nex
   nex=c
  