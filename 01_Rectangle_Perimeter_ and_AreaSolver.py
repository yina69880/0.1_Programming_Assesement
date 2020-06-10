# Rectangle
print("***** Rectangle *****")
b = float(input("Base:"))
h = float(input("Height:"))
Perimeter = 2 * (b + h)
Area = b*h
print("Perimeter of rectangle =", Perimeter)
print("Area of a rectangle = ", Area)


def num_checker(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":

            for letter in response:
                if letter.isdigit():
                 has_errors = "yes"
                 break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# #Main routine goes here

source = num_checker("What is the recipe name?",
                   "Please enter an integer more than zero",
                   "yes")




