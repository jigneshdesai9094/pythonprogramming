fh=open("file5.txt","a")
fh.write("hello jignesh")
fh.close()

fh=open("file5.txt","a+")
fh.write(",Now i am studing")
print(fh.tell())
print(fh.seek(1))

print("content : \n"+fh.read())
fh.close()
