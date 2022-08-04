import random
import os
numberletter=0
#made by Ata
lttrlist=["q","Q","w","W","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","x","y","z","ö","ç","ı","ğ","ü","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z",1,2,3,4,5,6,7,8,9,0,"!","'","^","+","%","&","/","(",")","=","?","_","-",";"," ","`",">","<","*","|","@"]
lttrlist1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","x","y","z","ö","ç","ı","ğ","ü","A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z",1,2,3,4,5,6,7,8,9,0," "]
foundpass=""
trycount=0

print("made by ataanl")
print("______________")
print("""

""")
    

password=input("Please type the password that you want to test the security of >>")
print("""       BRUTE FORCE TESTING..


""")

x=random.randint(0,92) #0-92 arası rasgele sayı seç
y=lttrlist[x]
while True:
        
        x=random.randint(0,92)
        y=str(lttrlist[x])
        if len(password)==numberletter:
                        print("The password was:",foundpass)
                        print("Took ",trycount," tries to find it.")
                        input()
                        del(password)
                        numberletter = 0
                        password=input("Please type the password that you want to test the security of >>")
                        print("""       BRUTE FORCE TESTING..


                                """)

                        print("____________________________")
        if y==password[numberletter]:
                print(" FOUND",[numberletter],"tries= #",trycount,)
                numberletter+=1
                foundpass+=y
                trycount+=1


                
                
                
                

                
            
            
        else:
                print(y, end=" ")
                trycount+=1
    
    

    
    
    
    
