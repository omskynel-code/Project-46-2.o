print()
print("MAIN")
print()

n = int(input("Enter the sum of a number you will like the answer to: "))

sum = 0
for i in range(n+1):
    sum = sum + i 
print("Sum of first {n} number is :", sum)