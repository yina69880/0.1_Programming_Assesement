
def num_check(question, type):

    if type == int:
        error_type = "Please enter a number that is more than zero"
    else:
        error_type = "Please enter an integer that is larger than zero"

    error = "Please enter {} that is more than zero"

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

       except SyntaxError:
           print(error)

# Square
print("***** Square *****")
b = float(input("Base:"))
Perimeter = b * 4
Area = b * b
print("Perimeter of the Square =", Perimeter)
print("Area of the Square = ", Area)
