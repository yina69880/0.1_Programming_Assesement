
def num_check(question, type):

    if type == float:
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
what_shape = num_check('''What shape do you want to calculate the area and perimeter of?
  1. Calculate Cirlce
  2. Calculate Square
  3. Calculate Rectangle
  4. Calculate Triangle
  5. Calculate Trapezium
  6. Calculate Parallelogram
  7. Calculate Rhombus
  Please enter the number associated with the shape: ''', float).strip().lower()

if what_shape in ['1', '1.', 'Cirlce', 'C', 'c', 'circle', 'CIRCLE']:
        print("***** Circle *****")
        r = num_check("Radius: ", float)
        circumference = 2 * math.pi * r
        area = math.pi * (r * r)
        print("Circumference of circle = ", circumference)
        print("Area of a circle = ", area)

elif what_shape in ['2', '2.', 'Square', 'S', 's', 'square', 'SQUARE']:
        print("***** Square *****")
        b = num_check("Base:", float)
        perimeter = b * 4
        area = b * b
        print("Perimeter of the Square = ", perimeter)
        print("Area of the Square = ", area)

elif what_shape in ['3.', '3', 'Rectangle', 'R', 'r', 'rectangle', 'RECTANGLE']:
        print("***** Rectangle *****")
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        perimeter = 2 * (b + h)
        area = b * h
        print("Perimeter of rectangle = ", perimeter)
        print("Area of a rectangle = ", area)

elif what_shape in ['4.', '4', 'Triangle', 'triangle', 'T', 't', 'TRIANGLE' ]:
        print("***** Triangle *****")
        s1 = num_check("Side 1: ", float)
        s2 = num_check("Side 2:", float)
        s3 = num_check("Side 3:", float)
        perimeter = s1 + s2 + s3
        print("Perimeter of triangle = ", perimeter)
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        area = b * h
        print("Area of a triangle = ", area)

elif what_shape in ['5', '5.', 'Trapezium', 'trapezium', 'T', 't', 'TRAPEZIUM']:
        print("***** Trapezium *****")
        a = num_check("Top length: ", float)
        b = num_check("Bottom length: ", float)
        c = num_check("Side 1: ", float)
        d =num_check("Side 2: ", float)
        perimeter = a + b + c + d
        print("Perimeter of a Trapezium = ", perimeter)
        a = num_check("Top length: ", float)
        b = num_check("Bottom length: ", float)
        h = num_check("Height: ", float)
        area = ((a+b)/2)*h
        print("Area of a Trapezium = ", area)

elif what_shape in ['6', '6.', 'Parallelogram', 'parallelogram', 'P', 'p', 'PARALLELOGRAM']:
        print("***** Parallelogram *****")
        b = num_check("Base: ", float)
        s1 = num_check("Side 1", float)
        perimeter = 2 * (b * s1)
        print("Perimeter of a Parallelogram = ", perimeter)
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        area = b * h
        print("Area of a Parallelogram = ", area)

elif what_shape in ['7', '7.', 'Rhombus', 'rhombus', 'R', 'r', 'RHOMBUS']:
        print("***** Rhombus *****")
        s1 = num_check("Side: ", float)
        perimeter = 4 * s1
        print("Perimeter of a Rhombus = ", perimeter)
        D1 = num_check("Diagonal 1: ", float)
        D2 = num_check("Diagonal 2: ", float)
        area = (D1 * D2)/2
        print("Area of a Rhombus = ", area)



