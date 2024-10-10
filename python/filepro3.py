#1.way
# fh = open("file4.txt","r")
# content = fh.read()
# content=content.replace("gujarat","gujrat")
# fh.close()
# fh = open("file4.txt","w")
# fh.write(content)
# fh.close()

#2.way
# fh = open("file4.txt","r")
# c = fh.readline()
# content=""
# while(len(c)>0):
#      content+=c.replace("gujrat","gujarat")
#      c=fh.readline()
# fh.close()
# fh = open("file4.txt","w")
# fh.write(content)
# fh.close()

#3.way
def all_occurance(content):
    indexes = []
    index = content.find("gujarat")
    while(index!=-1):
        indexes.append(index)
        print(index)
        index = content.find("gujarat",index+1)
    return indexes
fh = open("file4.txt","r+")
content = fh.read()
if(content.find("\n")>=0):
    print(content)
    print(content.find("\n"))
    print("contain \n")
else:
    print("not contain \n")

for i in all_occurance(content):
     fh.seek(i)
     fh.write(" gujrat ")
fh.close()




# indexes = [0]
# def all_occurance(line):
#     index = line.find("gujarat")
#     while(index!=-1):
#         indexes.append((len(indexes)-1)+index)
#         index=line.find("gujarat",index+1)
# fh = open("file6.txt","r+")
# content = fh.readline()
# while(len(content)>0):
#     all_occurance(content)
#     content = fh.readline()
# for i in indexes:
#     fh.seek(i)
#     fh.write("gujrat ")
# fh.close()
