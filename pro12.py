
def takeday():
    while(True):
     d=input("Enter day :")
     if(len(d)==1):
        d="0"+d
        return d
     elif(int(d)>31 or int(d)<1):
       print("Please Enter Valid Day :")
     else:
        return d
months={
1:"January",
2: "February",
3: "March",
4: "April",
5: "May",
6:"June",
7: "July",
8: "August",
9: "September",
10:"October",
11 :"November",
12:"December"
}
print("Enter Birthdate DD-MM-YYYY format")
d=takeday()
print(" day ",d)
while(True):
    m=int(input("Enter Month"))
    d1=int(d)
    print((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)and d1>31)
    print(m==2 and d1>29)
    print((m==4 or m==6 or m==9 or m==11) and d1>30)
    if(m>12 or m<1):
      print("Please,Enter valid Month : ")
    elif(((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)and d1>31) or (m==2 and d1>29) or ((m==4 or m==6 or m==9 or m==11) and d1>30 )):
      print("Invalid day, please enter valid day")
      d=takeday()
      d1=int(d)
    else:
        break
y=input("Enter Year")
for i in months.keys():
    if(m==i):
      print("BIRTHDATE : {}-{}-{}".format(d,months[i],y))