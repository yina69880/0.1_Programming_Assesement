
def num_check(question, type):

    if type == int:
        error_type = "Please enter a number that is more than zero"
    else:
        error_type = "Please enter an integer that is larger than zero"

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
h = float(int("Height: ", int))
Perimeter = 2 * (b + h)
Area = b*h
print("Perimeter of rectangle =", Perimeter)
print("Area of a rectangle = ", Area)

