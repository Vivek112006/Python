target = int(input("Enter the ending number: "))
n = 1
total_sum = 0  

while n <= target:
    print(f"Found  number: {n}")
    total_sum += n  
    n += 1  

print(f"\nThe total sum of all numbers is: {total_sum}")
