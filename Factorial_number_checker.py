
# 7 for 7 multiply 6 = 42 * 5
# reverse the number multiply the number store it in variable n-1 and n * previous answer

def factorial_generator(n):
    reverse = list(reversed(range(1, n)))
    number = n
    answer = n
    for i in reverse:

        print(f'{i}x{answer} = {i*answer}')
        answer = i * answer
    number -= 1
# factorial_generator(5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

