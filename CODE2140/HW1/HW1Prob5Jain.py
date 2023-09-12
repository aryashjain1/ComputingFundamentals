predicted_pi = 0
k = 0
while k <= 10:
    predicted_pi += ((-1) ** k) / (2 * k + 1)
    print(f'{k}\t\t{4*predicted_pi:.6f}')
    k += 1