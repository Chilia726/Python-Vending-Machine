# Packages

import os
from photos import payment

# Setting up items

A1, A2, A3, A4 = "Pringles", "Cheetos", "Doritos", "Takis"
B1, B2, B3, B4 = "Water", "Pepsi", "Mountain_Dew", "Dr._Pepper"
C1, C2, C3, C4 = "Snickers", "Hershey's", "Sour_Patch_Kids", "Skittles"
D1, D2, D3, D4 = "Arizona", "Red_Bull", "Bang", "Prime"

# See items

os.system('cls')
print("A", A1, A2, A3, A4)
print("B", B1, B2, B3, B4)
print("C", C1, C2, C3, C4)
print("D", D1, D2, D3, D4)

# Payment

pay = str(input("Please put one coin in (p/n): "))

if pay == "p":
    payment()
    os.system('cls')
else:
    exit()
