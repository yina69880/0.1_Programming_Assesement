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

# Triangle
print("***** Triangle *****")
# Ask user for sides for perimeter
s1 = num_check("Side 1: ", int)
s2 = num_check("Side 2:", int)
s3 = num_check("Side 3:", int)
perimeter = s1+s2+s3
print("Perimeter of triangle =", perimeter)
#Ask user for base and height
b = num_check("Base: ", int)
h= num_check("Height: ", int)
area = b * h
print("Area of a triangle = ", area)