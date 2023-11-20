myBill = float(input("What was the bill?: "))

print()
tip = float(input("How much would you like to tip?(15%,18% or 20%) insert as number without the percentage"))

if tip == 15 or tip == 18 or tip == 20:
 print("Thank you for your tip!")
  
 print()
 numberOfPeople = int(input("How many people?: "))
 factor = (1+(tip / 100))
 answer = ((myBill*factor) / numberOfPeople)
 answer = round(answer, 2)
 print("You all owe", answer)
else:
 print("error, please try again. Remember a tip can only be 15%,18% or 20% :)")