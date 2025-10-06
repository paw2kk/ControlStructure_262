# Fibonacci numbers up to n (max value)

n = int(input("Enter the maximum value: "))

a, b = 0, 1

print("Fibonacci series up to", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
