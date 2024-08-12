c=input("Enter Any Suit with Card : ").lower()
c=c.strip()
suit,card=c.split()
#print(suit," ",card)
if(suit=='diamond' or (suit=='spade' and card=='ace') or card=='king'):
  print("Card is Lucky")
else:
  print("Please,try next time")
