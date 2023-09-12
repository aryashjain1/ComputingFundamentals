for hyp in range(1, 1001):
    for side1 in range(1, 1001):
        for side2 in range(1, 1001):
            if ((side1**2 + side2**2) == hyp**2):
                print(side1, ",", side2, ", and", hyp, "is a pythagorean triple")
