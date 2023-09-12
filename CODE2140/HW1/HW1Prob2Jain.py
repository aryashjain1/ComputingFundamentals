num = int(input("Enter an integer number: "))
num_copy = num
num_copy2 = num
num_digits = 0
reverse = 0
while num_copy > 0:
    num_copy //= 10
    num_digits += 1

for i in range(num_digits-1, -1, -1):
    reverse += (num_copy2 % 10) * (10 ** i)
    num_copy2 //= 10
    
if reverse == num:
    print("The integer", num, "is a palindrome!")
else:
    print("The number", num, "isn't a palindrome.")
