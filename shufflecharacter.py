import random
indexlist=[]
str=input("Enter your name :")
c=len(str)-1;
while(c>=0):
  num = int(random.random()*len(str))
  if(not(num in indexlist)):
    t=str[c]
    str=str[0:c]+str[num]+str[c+1:]
   # print(str,end="  ") 
    str=str[0:num]+t+str[num+1:]
   # print(str,"\n")
    indexlist.append(num)
    c-=1

print(str)