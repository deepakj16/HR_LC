n = 5
#0,1,1,2,3
def fibonacci(n):
    lis = [0,1]

    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
ip = fibonacci(5)

print(ip)

print(list(map(lambda x: pow(x,3), ip)))




'''
Recursive:
# Add your function below
def fib(n):
    # Check the base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return fib(n - 1) + fib(n - 2)
'''