print("GRADE GENERATOR")

print()
print("this a grade generator that will calculate your grade based on your grades in assignments")

print()
name = input("What is your name?")

print()
max_score = int(input("What is the maximum amount of marks that could be scored in the paper"))
score = int(input("What did you score in the paper?"))

grade = (score/max_score)*100
grade = round(grade,0)

if grade >= 90:
  print("\033[32m")
  print(f"{name}, well done! You scored a whopping {grade}%, which is an A*")
  
elif grade >= 80 and grade < 90:
  print("\033[32m")
  print(f"{name}, well done you scored {grade}%, which is an A")
  
elif grade >= 70 and grade < 80:
  print("\033[32m")
  print(f"{name}, you scored {grade}%, which is a B, really good you can push for an A next time!")

elif grade >= 60 and grade < 70:
  print("\033[33m")
  print(f"{name}, you scored {grade}%, which is a C, you can do better than that!")

elif grade >= 50 and grade < 60:
  print("\033[33m")
  print(f"{name}, you scored {grade}%, which is a D, it is well sha")

else:
  print("\033[31m")
  print(f"{name}, you scored {grade}%, which is an U, you need to try harder for the sake of your own life...")