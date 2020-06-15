
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


# Rectangle
print("***** Rectangle *****")
b = num_check("Base: ", int)
h = num_check("Height: ", int)
Perimeter = 2 * (b + h)
Area = b*h
print("Perimeter of rectangle =", Perimeter)
print("Area of a rectangle = ", Area)

