def count(price,note,n):
    while(price>=(n*note)):
        n+=1
    return n-1

def check(price,note,ne):
  n=count(price,note,1)
  c=n-1
  while(c>0):
      print("----------")
      n=count(note*c,note,1)
      print("Note {} : {} ".format(note,n))
      p=price-(note*n)
      count10=1
      while(p>=(count10*ne)):
        count10+=1
      print("Note {} :{} ".format(ne,count10-1))
      c-=1
      
   
price=int(input("Enter Price"))
if(price>=10):
  n=count(price,10,1)
  print("-----------")
  print("Note 10  : ",n)
  
  check(price,20,10)
  
  check(price,50,10)
  
  check(price,100,10)
  
  check(price,500,10)
if(price>=20):
   n=count(price,20,1)
   if(price==(n*20)):
     print("---------------")
     print("Note 20 ",n)
   
