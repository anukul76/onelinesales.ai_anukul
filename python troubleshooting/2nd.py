def compute(n):
    if n < 10:
        out = n ** 2
    elif n <= 20:    #as 20 be inclusive in
        out=1
        for i in range(1, n-9):       #we have to change it as the factorial loop should start from 1, not 0.
            out *= i
    else:
        lim = n - 20
        out = lim*(lim+1)/2    #the code wasn't right so i changed it
    print(out)


n = int(input("Enter an integer: "))
compute(n)   #we have to call the function 