# Count even and odd numbers in a list

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")

# Count even, odd, and prime numbers in a list

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

even_count = 0
odd_count = 0
prime_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if is_prime(num):
        prime_count += 1

print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
print(f"Prime numbers count: {prime_count}")
