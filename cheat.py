print("This calculator will tell you the answers. You're such a cheater.")

shape = input("Specify what kind of shape you want to see the stats of. (Square, rectangle, parallelogram, triangle, circle.)" )


shape.lower()
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481
a = 0
a2 = 0
per = 0
per2 = 0
d = 0
b = float(input("Type the base(radius) of your %s here: "%shape))
if shape == "circle":
    pass
if shape == "parallelogram":
    sl = float(input("What is the side length of your"))

if not (shape == "square" or "circle"):
    h = float(input("Type the height of your %s here: "%shape))


if shape == "square":
    a = b**2
    a2 = a / 10000
    per = b * 4
    per2 = per / 100

elif shape == "rectangle":
    a = b*h
    a2 = a / 10000
    per = (b * 2) + (h * 2)
    per2 = per / 100

elif shape == "circle":
    d = b*2
    a = pi * (b**2)
    a2 = a / 10000
    per = pi * d
    per2 = per / 100

elif shape == "triangle":
    a = (b * h) / 2
    a2 = a / 10000
    per = b * 3
    per2 = per / 100

elif shape == "parallelogram":
    a = b * h
    a2 = a / 10000
    per


print("Stats:")
print("Area:")
print(str(a) + " cm^2")
print(str(a2) + " m^2")
print("Perimeter (Circumference):")
print(str(per) + " cm")
print(str(per2) + " m")



