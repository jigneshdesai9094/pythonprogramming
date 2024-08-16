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
      p=p-((count10-1)*ne)
      d=1
      if(p>=(d*10)):
          d+=1
      if(d-1!=0):
       print("Note {} : {}".format(10,d-1))
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
     
   check(price,50,20)
   
   check(price,100,20)
   
   check(price,500,20)
  
if(price>=50):
   n=count(price,50,1)
   if(price==(n*50)):
     print("---------------")
     print("Note 50 ",n)
     
   check(price,100,50)
   
   check(price,500,50)

if(price>=100):
   n=count(price,100,1)
   if(price==(n*100)):
     print("---------------")
     print("Note 100 ",n)
     
   check(price,500,100)
  