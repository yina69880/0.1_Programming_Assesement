what_shape = input('''What shape do you want to calculate the area and perimeter of?
  1. Calculate cirlce
  2. Calculate square
  3. Calculate rectangle
  4. Calculate triangle
  5. Calculate pentagon''').strip().lower()
pi = 22/7
if what_shape in ['1', '1.']:
        r = float(input('Enter the radius of the circle:'))
        area = (pi * r) * (pi * r)

    elif what_shape in ['2', '2.']:
        b = float(input("Enter the base:"))
        area = b * b
        perimeter = b * 4
        print()

    elif what_shape in ['3', '3.']:
        b = float(input('Enter the base:'))
        h = float(input('Enter the height:'))
        area = b * h
        perimeter = (2*b) + (2*h)
        print("Perimeter of rectangle =", Perimeter)
        print("Area of a rectangle = ", Area)

    elif what_shape in ['4.', '4']:
        b = float(input('Enter the length of the base:'))
        h = float(input('Enter the height of the pyramid (center of base to vertex of triangles):'))
        area = b * h / 2