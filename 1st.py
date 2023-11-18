print("Hello, this is a scripture for every day of the week!")

print()
name = input("What is your name?")
print("Hello!", name)

print()
DOW = input("What is the day of the week?")

if DOW == "Monday" or DOW == "monday":
    print (name, "the scripture for you todays is proverbs 3:5-7, it talks about wisdom!")
    
elif DOW == "Tuesday" or DOW == "tuesday":
    print (name, "the scripture for you todays is John 3:16, Gods grace and love is beautiful!")
    
elif DOW == "Wednesday" or DOW == "wednesday":
    print (name, "the scripture for you todays is Philippians 4:13, because anything is possible with God!")
    
elif DOW == "Thursday" or DOW == "thursday":
    print (name, "the scripture for you todays is 2 Tim 1:7, so we should not fear anything")
    
elif DOW == "Friday" or DOW == "friday":
    print (name, "the scripture for you todays is Psalm 91, God is our protector and shield!")
    
elif DOW == "Saturday" or DOW == "saturday":
    print (name, "the scripture for you todays is Proverbs 10:22, God can bless us remember that!")
    
elif DOW == "Sunday" or DOW == "sunday":
    print("hey", name, "Let us switch it for today.")
    fave = input ("what is your favourite scripture?")
    print (fave,"that's a really nice scripture! Thank you for sharing!",name)
else:
  print("And you are...?")