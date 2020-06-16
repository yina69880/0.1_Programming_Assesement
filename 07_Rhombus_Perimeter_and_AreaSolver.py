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

print("***** Rhombus *****")
s1 = num_check("Side: ", float)
perimeter = 4 * s1
print("Perimeter of a Rhombus = ", perimeter)
D1 = num_check("Diagonal 1: ", float)
D2 = num_check("Diagonal 2: ", float)
area = (D1 * D2)/2
print("Area of a Rhombus = ", area)
