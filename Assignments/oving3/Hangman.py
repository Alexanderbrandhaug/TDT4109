hemmelig_ord = input("Skriv inn det hemmelige ordet: ")
antall_liv = int(input("Hvor mange forsøk får brukeren? "))
asd = hemmelig_ord

while antall_liv > 0:
    bokstav = input("Gjett på en bokstav i ordet: ")
    if bokstav in hemmelig_ord:
        print("Stemmer, bokstaven er i ordet. ")
        print()
        asd = asd.replace(bokstav, "")
        
    else:
        antall_liv -= 1
        print("Det var dessverre feil ")
        print("Du har ", antall_liv, "liv igjen:")
        
    if antall_liv == 0:
        print("Du har dessverre ingen liv igjen. ")
        
        break
    if asd == "":
     print("Du vant!! ")
     break
         
        



    
    
    
