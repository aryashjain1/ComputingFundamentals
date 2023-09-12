def fahrenheit(temperature):
    return (9/5) * temperature + 32

print("Celcius\t\tFahrenheit")
for i in range(-10, 101):
    print(f'{i}\t\t{fahrenheit(i):.2f}')