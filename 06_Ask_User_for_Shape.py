
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
what_shape = input('''What shape do you want to calculate the area and perimeter of?
  1. Calculate Cirlce
  2. Calculate Square
  3. Calculate Rectangle
  4. Calculate Triangle
  5. Calculate Trapezium
  6. Calculate Parallelogram
  7. Calculate Rhombus
  Please enter a number associated with the shape: ''').strip().lower()

if what_shape in ['1', '1.', 'Cirlce', 'C', 'c', 'circle', 'CIRCLE']:
        print("***** Circle *****")


elif what_shape in ['2', '2.', 'Square', 'S', 's', 'square', 'SQUARE']:
        print("***** Square *****")

elif what_shape in ['3.', '3', 'Rectangle', 'R', 'r', 'rectangle', 'RECTANGLE']:
        print("***** Rectangle *****")


elif what_shape in ['4.', '4', 'Triangle', 'triangle', 'T', 't', 'TRIANGLE' ]:
        print("***** Triangle *****")


elif what_shape in ['5', '5.', 'Trapezium', 'trapezium', 'T', 't', 'TRAPEZIUM']:
        print("***** Trapezium *****")


elif what_shape in ['6', '6.', 'Parallelogram', 'parallelogram', 'P', 'p', 'PARALLELOGRAM']:
        print("***** Parallelogram *****")


elif what_shape in ['7', '7.', 'Rhombus', 'rhombus', 'R', 'r', 'RHOMBUS']:
        print("***** Rhombus *****")

