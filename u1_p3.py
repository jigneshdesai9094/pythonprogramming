def recursively(l,x):
    if(x<len(l)):
      print(l[x],end=" ")
      x+=1
      recursively(l,x)
def recur(l):
    if(l!=[]):
        print(l[0],end=" ")
       # print(l[1:])
        recur(l[1:])
        
l=[10,20,30,40,50,60,70,80,90,100]
#recursively(l,0)
print("\n")
recur(l)