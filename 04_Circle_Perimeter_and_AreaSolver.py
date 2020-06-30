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
print("***** Circle *****")
r = num_check("Radius: ", float)
area = math.pi * (r * r)
circumference = 2 * math.pi * r
print("Circumference of circle = ", circumference)
print("Area of a circle = ", area)