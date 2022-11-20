# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#########################################################################################
## --> Task 1
#########################################################################################

for i in range(0,3):
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    if num1 == num2:
        print("They are equal !")
    if num1 > num2:
        print("Number 1 is bigger !")
    if num1 != num2:
        print("Number 1 is not equal to Number 1")
    if num1 >= num2:
        print("Number 1 is bigger or equal to Number 2 !")
    if num1 <= num2:
        print("Number 2 is bigger or equal to Number 1 !")
    if num1 % 2 == 0:
        print("Number 1 is even")
    else:
        print("Number 1 is odd")
        print("Number 1 and Number 2 are even")
    
#########################################################################################
## --> Task 2 ### If statement way to do it !
#########################################################################################

given_month = input("Give me a month and i tell you how many days it has (end=quit) : ").lower().strip()

if given_month == "january": 
    print (f"The month [{given_month}] has 31 days")
elif given_month == "february": 
    print (f"The month [{given_month}] has 28 days")
elif given_month == "march": 
    print (f"The month [{given_month}] has 31 days")
elif given_month == "april": 
    print (f"The month [{given_month}] has 30 days")
elif given_month == "may": 
    print (f"The month [{given_month}] has 31 days")   
elif given_month == "june": 
    print (f"The month [{given_month}] has 30 days")   
elif given_month == "july": 
    print (f"The month [{given_month}] has 31 days")   
elif given_month == "august": 
    print (f"The month [{given_month}] has 31 days")
elif given_month == "september": 
    print (f"The month [{given_month}] has 30 days")   
elif given_month == "october": 
    print (f"The month [{given_month}] has 31 days")
elif given_month == "november": 
    print (f"The month [{given_month}] has 30 days")
elif given_month == "december": 
    print (f"The month [{given_month}] has 31 days")   
else:
    print ("Man, no such month on my planet!")


#########################################################################################
## --> Task 2 ### using a dictionary !!!
#########################################################################################

months = {
    "january": 31,  "januar": 31,       "gennaio": 31,
    "february": 28, "februar": 28,      "febbraio": 28,
    "march": 31,    "märz": 31,         "marzo": 31,
    "april": 30,    "april": 30,        "aprile": 30,
    "may": 31,      "mai": 31,          "maggio": 31,
    "june": 30,     "juni": 30,         "giugno": 30,
    "july": 31,     "juli": 31,         "luglio": 31,
    "august": 31,   "august": 31,       "agosto": 31,
    "september": 30,"september": 30,    "settembre": 30,    
    "october": 31,  "oktober": 31,      "ottobre": 31,
    "november": 30, "november": 30,     "november": 30,
    "december": 31, "de_zember": 31,    "dicembre": 31,
    
    "jan": 31,                          "gen": 31,
    "feb": 28,                          "feb": 28,
    "mar": 31,
    "apr": 30,
    "may": 31,      "mai": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,      "okt": 31,
    "nov": 30,
    "dec": 31,      "dez": 31,

    }
given_month = ""
while True:
    given_month = input("Give me a month and i tell you how many days it has (end=quit) : ").lower().strip()
    
    if given_month == "end": break
    
    if given_month in months:
        print (f"The month " + given_month.capitalize() + " has": 0, months[given_month], "days")
    else:
        print ("Man, no such month on my planet!")