print("What generation are you part of?!")

print()
print("""We are going to ask you a couple questions, based on your answer we will determine what generation you're part of.""")

print()
year = int(input("What is your year of birth?"))

if year >= 1925 and year <= 1946:
  print ("You are part of the traditionalist generation.")
elif year >= 1947 and year <= 1964:
  print ("You are part of the Baby Boomer generation.")
elif year >= 1965 and year <= 1981:
  print ("You are part of the Generation X generation.")
elif year >= 1982 and year <= 1995:
  print ("You are part of the Millenials.")
elif year >= 1996 and year <= 2015:
  print("You are part of Gen Z (the best generation!)")