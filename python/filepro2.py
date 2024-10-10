
def split_text(text):
    l = text.split()
    
    return l
def join_word(words):
     sen = ""
     for ws in words:
         for w in ws:
              sen+=w+" "
         sen+="\n"

     return sen

def print_words(words):
     for wds in words:
          for ws in wds:
             print(ws,end="\n")

fh1=open("file1.txt","r")
words=[]
count = 0
s=fh1.readline()
while(len(s)>0):
     words.append([])
     words[count]=split_text(s)
     s=fh1.readline()
     count+=1
fh1.close()
print("\nText convert to word : \n")
print_words(words)

sen = join_word(words)
print("\nword to Sentense : \n")
print(sen)
fh1 =open("file3.txt","w")
fh1.write(sen)
fh1.close()



#second way
fh= open("file1.txt","r")
fh2= open("file3.txt","w")
content = fh.readline()
while(len(content)>0):
   s = content.split()
   print(s)
   for i in s:
     fh2.write(i+" ")
   fh2.write("\n")
   content=fh.readline()

fh.close()
fh2.close()
