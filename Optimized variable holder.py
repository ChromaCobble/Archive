
#optimized variable holder
lis = [] #variable name holder
qcount = 6 #variable count [changable]  <---- Change here
# *** variable name list generator ***
letters=["a","b","c","d""f","g"]
numbers=[1,2,3,4,5,6,7,8,9]
biglist=[]
for letter in letters:
    for number in numbers:
        biglist.append(str(letter)+str(number))
# *** variable name list generator ***

for y in range(1, qcount+2):
    lis.append(biglist[y-1]) # adds to the list the number with a from 1 to variable count
for x in range(1, len(lis)): #a for loop to use every variable in lis

    inp = input(">>") # the available variable that the value is going to be set to
    vars()[lis[x-1]] = inp #makes the __dict__ attribute of the lis items to the user input called "inp"

print(a1,a2,a3,a4) # Remove here (Debug feature)
input() # Remove here (Debug feature)


#Ata Anıl Altıntaş













