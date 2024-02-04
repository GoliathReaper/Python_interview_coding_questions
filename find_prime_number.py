

def prime_finder(n):
    count = 0
    for i in range(2, 100):
        if n % i == 0:
            count += 1
    if count >= 2:
        return 'not a prime'
    if count == 1:
        return 'prime'


data = []
for i in range(2, 100):
    if prime_finder(i) == 'prime':
        if not 2 or 3 or 4 or 5 or 7 and not i % 2 or 3 or 4 or 5 or 7 == 0:
            data.append(i)

print(data)


# -----------------------------

# Solution

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
