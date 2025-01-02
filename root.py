a=int(input("Enter a number :"))
primes_till=[]
for j in range(2,a+1):
    div=[]
    for i in range(2,j):
        if j%i==0:
            div.append(i)
        else:
            pass
    if bool(div):
        pass
    else:
        primes_till.append(j)
print(primes_till)
print("Number of primes till {} are {}".format(a, len(primes_till)))
