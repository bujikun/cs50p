x = float(input("Enter the value of X: "))
y = float(input("Enter the value of Y: "))
# z = round(x + y)  # rounds to the nearest integer
z = round(x / y, 2)
print(f"{z:,.2f}")
