# Q1. Variables, Data Types and Operators

print("\n--- Q1: Variables, Data Types and Operators ---")

name = "Anas"
age = 19
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

num1 = 20
num2 = 10

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

print("Greater Than:", num1 > num2)
print("Equal:", num1 == num2)
print("Logical AND:", num1 > 5 and num2 > 5)


# Q2. Print Numbers from 1 to 10 Using For Loop

print("\n--- Q2: For Loop ---")

for i in range(1, 11):
    print(i)


# Q3. Print Numbers from 1 to 10 Using While Loop

print("\n--- Q3: While Loop ---")

i = 1

while i <= 10:
    print(i)
    i += 1


# Q4. Print Even Numbers from 1 to 20

print("\n--- Q4: Even Numbers ---")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Q5. Print Odd Numbers from 1 to 20

print("\n--- Q5: Odd Numbers ---")

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# Q6. Calculate Sum of Numbers from 1 to 10

print("\n--- Q6: Sum of Numbers ---")

total = 0

for i in range(1, 11):
    total += i

print("Total Sum:", total)


# Q7. Multiplication Table

print("\n--- Q7: Multiplication Table ---")

number = int(input("Enter a number for table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Q8. Factorial of a Number

print("\n--- Q8: Factorial ---")

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial is not possible for negative numbers")
else:
    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)


# Q9. Break Statement

print("\n--- Q9: Break Statement ---")

for i in range(1, 11):
    if i == 6:
        break

    print(i)


# Q10. Continue Statement

print("\n--- Q10: Continue Statement ---")

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


# Q11. Reverse Counting Using While Loop

print("\n--- Q11: Reverse Counting ---")

i = 10

while i >= 1:
    print(i)
    i -= 1


# Q12. Check Positive, Negative or Zero Using If Else

print("\n--- Q12: Conditional Statements ---")

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# Q13. Find Largest of Three Numbers

print("\n--- Q13: Largest of Three Numbers ---")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest Number:", a)
elif b >= a and b >= c:
    print("Largest Number:", b)
else:
    print("Largest Number:", c)


# Q14. Count Digits in a Number Using While Loop

print("\n--- Q14: Count Digits ---")

number = abs(int(input("Enter a number: ")))

count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("Total Digits:", count)


# Q15. Print a Star Pattern

print("\n--- Q15: Star Pattern ---")

for i in range(1, 6):
    print("*" * i)


# ASSIGNMENT COMPLETED

print("\nAssignment 3 Completed Successfully!")