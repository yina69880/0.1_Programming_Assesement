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


print("***** Trapezium *****")
a = num_check("Top length: ", float)
b = num_check("Bottom length: ", float)
c = num_check("Side 1: ", float)
d = num_check("Side 2: ", float)
perimeter = a + b + c + d
print("Perimeter of a Trapezium = ", perimeter)
a = num_check("Top length: ", float)
b = num_check("Bottom length: ", float)
h = num_check("Height: ", float)
area = ((a + b) / 2) * h
print("Area of a Trapezium = ", area)
