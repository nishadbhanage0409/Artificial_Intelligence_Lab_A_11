sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total/500)*100

print("Total Marks =", total,"/500")
print("Percentage =", percentage, "%")

if percentage >= 75:
    print("Grade: Distinction")

elif percentage >= 65:
    print("Grade: First Class")

elif percentage >= 40:
    print("Grade: Second Class")

else:
    print("Grade: Fail")


