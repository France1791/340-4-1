# Display Sum of n natural numbers

n = int(input("Enter a positive integer(n): "))

sum_of_natural_numbers = 0

for i in range(1, n+1):
    sum_of_natural_numbers += i

print(f"The sum of the first {n} natural numbers is {sum_of_natural_numbers}")

# Palindrome
number = int(input("Enter a number: "))
num_str = str(number)
reversed_str = num_str[::-1]

if num_str == reversed_str:
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")

#Pattern
n = 5;
for i in range(n):
    for j in range(i):
        print("* ", end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

    #Pyramid Pattern
n = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, n + 1):
    
    for j in range(n - i):
        print(" ", end="")
   
    for k in range(2 * i - 1):
        print("*", end="")
   
    print()
 
