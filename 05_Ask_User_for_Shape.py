
def num_check(question, type):

    if type == int:
        error_type = "a number"
    else:
        error_type = "an integer"

    error = "Please enter {} that is more than zero \n".format(error_type, type)

    valid = False
    while not valid:
       try:
           response = type(input(question))
           if response <=0:
               print(error)
           else:
               return response

       except ValueError:
           print(error)
import math
# Ask user for what shape?
what_shape = input('''What shape do you want to calculate the area and perimeter of?
  1. Calculate cirlce
  2. Calculate square
  3. Calculate rectangle
  4. Calculate triangle
  5. Calculate pentagon
  Please enter a number associated with the shape: ''').strip().lower()

if what_shape in ['1', '1.']:
        r = num_check("Radius: ", int)
        perimeter = 2 * math.pi * r
        area = math.pi * (r * r)
        print("Perimeter of circle =", perimeter)
        print("Area of a circle = ", area)
elif what_shape in ['2', '2.']:
        b = num_check("Base:", int)
        perimeter = b * 4
        area = b * b
        print("Perimeter of the Square =", perimeter)
        print("Area of the Square = ", area)

elif what_shape in ['3.', '3']:
        b = num_check("Base: ", int)
        h = num_check("Height: ", int)
        perimeter = 2 * (b + h)
        area = b * h
        print("Perimeter of rectangle =", perimeter)
        print("Area of a rectangle = ", area)

elif what_shape in ['4.', '4']:
        s1 = num_check("Side 1: ", int)
        s2 = num_check("Side 2:", int)
        s3 = num_check("Side 3:", int)
        perimeter = s1 + s2 + s3
        print("Perimeter of triangle =", perimeter)
        b = num_check("Base: ", int)
        h = num_check("Height: ", int)
        area = b * h
        print("Area of a triangle = ", area)

