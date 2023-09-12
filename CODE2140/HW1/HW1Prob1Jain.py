total_miles = 0
total_gallons = 0
gals = float(input("Enter the number of gallons used (any negative number to end): "))

while gals > 0:
    miles = float(input("Enter the number of miles driven: "))
    print(f'The miles/gallon for this tank was {miles/gals:.6f}')
    total_gallons += gals
    total_miles += miles
    gals = float(input("Enter the number of gallons used (any negative number to end): "))

print(f'The overall average miles/gallon for the above tankfuls was {total_miles/total_gallons:.6f}')