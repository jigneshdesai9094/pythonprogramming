inp = input("two char(branch),yy(year),one char(degree),rollno  ex:CS24M21\nenter format of roll number :  ")
inp=inp.upper()
branch=inp[0:2]
year=inp[2:4]
degree=inp[4:5]
cp=inp[5:]
if(branch=="CS"):
    branch="Computer Science"
    if(degree=="M"):
        degree="MCA"
    elif(degree=="B"):
        degree="BCA"
    else:
        degree="PGDCA"
elif(branch=="ME"):
    branch="Mechanical engineering"
    if(degree=="B"):
        degree="BME"
    else:
        degree="MME"
print("Branch : {} , Year : 20{} , Degree : {} , RollNo : {}".format(branch,year,degree,cp))