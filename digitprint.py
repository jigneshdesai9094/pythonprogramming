def digitprint(no): 
  if(1==no):
    print("One")
  elif(2==no):
    print("Two")
  elif(3==no):
    print("Three")
  elif(4==no):
     print("Four")
  elif(5==no):
     print("Five")
  elif(6==no):
     print("Six")
  elif(7==no):
    print("Seven")
  elif(8==no):
     print("Eight")
  elif(9==no):
     print("Nine")
  elif(10==no):
     print("Ten")
  elif(11==no):
     print("Eleven")
  elif(12==no):
     print("Twelve")
  elif(13==no):
      print("Thirteen")
  elif(14==no):
      print("Fourteen")
  elif(15==no):
      print("Fifteen")
  elif(16==no):
      print("Sixteen")
  elif(17==no):
      print("Seventeen")
  elif(18==no):
      print("Eighteen")
  elif(19==no):
      print("Nineteen")
  elif(20==no):
      print("Twenty",end="")
  elif(30==no):
      print("Thirty")
  elif(40==no):
      print("Fourty")
  elif(50==no):
       print("Fifty")
  elif(60==no):
       print("Sixty")
  elif(70==no):
       print("Seventy")
  elif(80==no):
       print("Eighty")
  elif(90==no):
       print("Ninety")
  elif(0==no):
       print("Zero")

  
def towdigiteval(no):
    l=int(no%10)
    u=no-l
    digitprint(u)
    digitprint(l)
def threedigiteval(no):
    u=int(no/100)
    digitprint(u)
    print(" Hundred")
    l=no-(u*100)
    if(l!=0):
      if(l<=20 or (l%10==0 and l<100)):
        digitprint(l)
      else:
        towdigiteval(l)
def fourdigiteval(no):
    u=int(no/1000)
    digitprint(u)
    print(" Thousand")
    l=no-(u*1000)
    if(l!=0):
         if(l<=20 or (l%10==0 and l<100)):
             digitprint(l)
         else:
             threedigiteval(l)
no=int(input("Enter Any Number under 99999 : "))
if(no<=20 or (no%10==0  and no<100)):
    digitprint(no)
elif(len(str(no))==3):
    threedigiteval(no)
elif(len(str(no))==4):
     fourdigiteval(no)
elif(len(str(no))==5):
     u=int(no/1000)
     if(u<=20 or (u%10==0  and u<100)):
      digitprint(u)
     else:
      towdigiteval(u)
     print(" Thousand")
     l=no-(u*1000)
     if(l!=0):
        if(l<=20 or (l%10==0 and l<100)):
             digitprint(l)
        else:
            threedigiteval(l)
     
elif(len(str(no))==2):
   towdigiteval(no)