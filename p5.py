blood=('A-','A+','B-','B+','O-','O+','AB-','AB+')
while(1):
 person1=input("Enter Person1 Blood Group : ").upper()
 if(person1 in blood):
  break
while(1):
  person2=input("\n\nEnter Person2 Blood Group : ").upper()
  if(person2 in blood):
    break
if(person1==person2):
   print(person1,"  and ",person2," blood group is match")
else:
   print(person1," and ",person2," blood group is not match")