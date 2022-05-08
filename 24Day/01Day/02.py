#2
sum = 1
def factorial(x):
    if (x==1):
        return 1

    return x * factorial(x-1)

#print(factorial(8))

n = int(input())
fact = 1
i = 1
while(i<=n):
    fact = fact * i
    i = i+1

print(fact)

