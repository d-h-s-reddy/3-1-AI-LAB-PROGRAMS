n=int(input("Enter the value of n to find the factorial and the fobonacci:"))
def Factorial(n):
    product=1
    for i in range(2,(n+1)):
        product*=i
    print("The Fatorial of the given number n is:",product)
def Fibonacci(n):
    f1=0
    f2=1
    sum=0
    for i in range(2,(n+1)):
        sum=f1+f2
        f1=f2
        f2=sum
    print("The fibonacci of the given number is:",sum)
Factorial(n)
Fibonacci(n)
