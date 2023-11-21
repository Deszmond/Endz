print("How many seconds are in a year!")

print()
name = input("What's your name?")

print()
print("H!", name)
print("""we are going to calculate how many seconds are in a year. for this calculation we need to make different considerations on wether we are refering to a leap year or a standard year""")

print()
leap = input("Are we taking into considation leap years? (y/n) ")

print()
if leap == "y" or leap == "Y":
 sec = (60*60*24*366)
 print("There are", sec, "seconds in a year")
elif leap == "n" or leap == "N":
 sec = (60*60*24*365)
 print("There are", sec, "seconds in a year")
else:
 print(name,"Please enter y or n")