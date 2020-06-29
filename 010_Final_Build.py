import math


def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Apologies, that is not a valid response")

def num_check(question, type):

    if type == float:
        error_type = "a number"

    error = "Please enter {} that is more than zero\n".format(error_type, type)

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(error)
            continue
        try:
            response = eval(response)
            response = float(response)

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

        except SyntaxError:
            print(error)

        except NameError:
            print(error)



shapes = ["1","circle", "2", "square","3", "rectangle", "4", "triangle",
                   "5", "parallelogram"]
# Ask user for what shape?
what_shape = string_checker('''What shape do you want to calculate the perimeter and area and of?
  1. Calculate Cirlce
  2. Calculate Square
  3. Calculate Rectangle
  4. Calculate Triangle
  5. Calculate Parallelogram
  Please choose a shape:
  ''', shapes)



if what_shape in ['1','circle']:
        print("***** Circle *****")
        r = num_check("Radius: ", float)
        circumference = 2 * math.pi * r
        area = math.pi * (r * r)
        print("Circumference of circle = ", "{:.2f}".format(circumference))
        print("Area of a circle = ", "{:.2f}".format(area))

elif what_shape in ['2','square']:
        print("***** Square *****")
        b = num_check("Base:", float)
        perimeter = b * 4
        area = b * b
        print("Perimeter of the Square = ", "{:.2f}".format(perimeter))
        print("Area of the Square = ", "{:.2f}".format(area))

elif what_shape in ['3','rectangle']:
        print("***** Rectangle *****")
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        perimeter = 2 * (b + h)
        area = b * h
        print("Perimeter of rectangle = ", "{:.2f}".format(perimeter))
        print("Area of a rectangle = ", "{:.2f}".format(area))

elif what_shape in ['4','triangle' ]:
        print("***** Triangle *****")
        s1 = num_check("Side 1: ", float)
        s2 = num_check("Side 2:", float)
        s3 = num_check("Side 3:", float)
        perimeter = s1 + s2 + s3
        print("Perimeter of triangle = ", "{:.2f}".format(perimeter))
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        area = (b * h)/2
        print("Area of a triangle = ", "{:.2f}".format(area))

elif what_shape in ['5','parallelogram']:
        print("***** Parallelogram *****")
        b = num_check("Base: ", float)
        s1 = num_check("Side 1: ", float)
        perimeter = 2 * (b * s1)
        print("Perimeter of a Parallelogram = ", "{:.2f}".format(perimeter))
        b = num_check("Base: ", float)
        h = num_check("Height: ", float)
        area = b * h
        print("Area of a Parallelogram = ", "{:.2f}".format(area))


