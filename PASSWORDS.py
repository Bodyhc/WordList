#CODE BY ABDULLAH M SOLIMAN 
from itertools import product
import string

print("""manikanta
  """)

min_len = int(input("Enter Your Min Len --> :"))
max_len = int(input("Enter Your Max Len --> : "))
counter = 0
print("[+] Loding . . . ")
charter = string.ascii_uppercase+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
file_open = open("WordList.txt","w")

for i in range(min_len,max_len+1):
    for s in product(charter,repeat=i):
        word = "".join(s)
        file_open.write(word)
        file_open.write("\n")
        counter+=1

print("WordList Genrate As {}".format(counter))
