factorial = lambda num: (num * factorial(num-1)) if num > 0 else 1

print(factorial(5))