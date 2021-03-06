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

# Square
print("***** Square *****")
b = num_check("Base:", int)
Perimeter = b * 4
Area = b * b
print("Perimeter of the Square =", Perimeter)
print("Area of the Square = ", Area)
