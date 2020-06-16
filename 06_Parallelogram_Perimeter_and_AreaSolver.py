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


print("***** Parallelogram *****")
b = num_check("Base: ", float)
s1 = num_check("Side 1", float)
perimeter = 2 * (b * s1)
print("Perimeter of a Parallelogram = ", perimeter)
b = num_check("Base: ", float)
h = num_check("Height: ", float)
area = b * h
print("Area of a Parallelogram = ", area)