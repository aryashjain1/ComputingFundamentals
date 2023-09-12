primes = [True] * 15000
for i in range(2, len(primes)):
    if primes[i]:
        print(i, end = ', ')
        for j in range(i+1, len(primes)):
            if j % i == 0:
                primes[j] = False