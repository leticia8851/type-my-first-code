#multiplication and Division Timetable
number = int(input("Enter a number: "))
print("\nMultiplication Table")
for i in range(1,13):
    print(number, "x", i, "=", number * i)
print("\nDivision Table")
for i in range(1, 13):
    print(number * i, "/", number, "=", i)