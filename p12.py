birth={"Jignesh":'30/03/11',"Rahul":'1/02/01',"Mehul":'10/01/24',"Hitesh":'15/08/22',"Akshay":'2/02/08'}

while(1):
   mno=input("Enter Month No : ")
   if(mno in ('0','1','2','3','4','5','6','7','8','9','10','11','12')):
      break
if(len(mno)==1):
   mno="0"+mno 
check=0
for key,value in birth.items():
    start=value.index('/')

    if(value[start+1:start+3]==mno):
       print(key,"",value)
       check+=1
if(check==0):
   print("\nNot Birthdate on this month")


