target = int(input("Enter the ending number: "))
n = 1
total_sum = 0  

while n <= target:
    if n % 2 == 0:
        print(f"Found even number: {n}")
        total_sum += n  
    n += 1  

print(f"\nThe total sum of all even numbers is: {total_sum}")
