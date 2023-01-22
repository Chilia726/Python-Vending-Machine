# Packages

from PIL import Image
import os

# Setting up items

A1, A2, A3, A4 = "Pringles", "Cheetos", "Doritos", "Takis"
B1, B2, B3, B4 = "Water", "Pepsi", "Mountain Dew", "Dr. Pepper"
C1, C2, C3, C4 = "Snickers", "Hershey's", "Sour Patch Kids", "Skittles"
D1, D2, D3, D4 = "Arizona", "Red Bull", "Bang", "Prime"

# See items

os.system('cls')
print("A", A1, A2, A3, A4)
print("B", B1, B2, B3, B4)
print("C", C1, C2, C3, C4)
print("D", D1, D2, D3, D4)

# Payment

pay = str(input("Please put one coin in (p/n): "))


# Snack selection


def payment():
    snack = input("Please select your snack: ")
    if snack == "A1":
        filename = "photos/Pringles.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "A2":
        filename = "photos/Cheetos.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "A3":
        filename = "photos/Doritos.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "A4":
        filename = "photos/Takis.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "B1":
        filename = "photos/Water.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "B2":
        filename = "photos/Pepsi.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "B3":
        filename = "photos/MtnDew.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "B4":
        filename = "photos/DrP.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "C1":
        filename = "photos/Snickers.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "C2":
        filename = "photos/Hershey's.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "C3":
        filename = "photos/SourPatchKids.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "C4":
        filename = "photos/Skittles.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "D1":
        filename = "photos/Arizona.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "D2":
        filename = "photos/RedBull.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "D3":
        filename = "photos/Bang.webp"

        img = Image.open(filename)

        img.show()
    elif snack == "D4":
        filename = "photos/Prime.webp"

        img = Image.open(filename)

        img.show()
    else:
        print("Invalid")


if pay == "p":
    payment()
    os.system('cls')
else:
    exit()
