# Import goes here
import math
# Loop statements
keep_going = ""
while keep_going == "":

# String checker
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

# Number checker
    def num_check(question, type):
        if type == float:
            error_type = "a number"
        error = "Please enter {} that is more than zero".format(error_type)

        valid = False
        while not valid:
            try:
                response = type(input(question))

                if response <= 0:
                    print(error)
                else:

                    return response

            except ValueError:
                print(error)

            except SyntaxError:
                print(error)



    # List of shapes
    shapes = ["1", "circle", "2", "square", "3", "rectangle", "4","triangle",
               "5", "parallelogram", "xxx"]

    #   set up loop


        # Ask user for what shape?
    print("1. Calculate Circle\n"
              "2. Calculate Square\n"
              "3. Calculate Rectangle\n"
              "4. Calculate Triangle\n"
              "5. Calculate Trapezium\n"
              "6. Calculate Parallelogram\n"
              "7. Calculate Rhombus\n")


    what_shape = string_checker('''What shape do you want to calculate the perimeter and area and of? ''', shapes)

    units = ['km', 'm', 'cm', 'mm']
    what_unit = string_checker("What units do you want to use: km, m, cm, mm? ", units)

    # if shapes = print shapes
    if what_shape in ['1','circle']:
                print("***** Circle *****")
                r = num_check("Radius: ", float)
                circumference = 2 * math.pi * r
                area = math.pi * (r * r)
                print("Circumference of circle = ", "{:.2f}".format(circumference), what_unit)
                print("Area of a circle = ", "{:.2f}".format(area), what_unit+"^2")
                print()
                # Separate Lists
                shape_size = []
                measurement = []

                # Get inputs and add to shape_size list
                shape = ""
                shape_size = []
                shape = area

                # Get the perimeter
                size = circumference

                # Add item name and cost to the 'item' list
                shape_size.append(area)
                shape_size.append(what_unit)
                shape_size.append(circumference)
                shape_size.append(units)

                # Add item to the measurement list
                measurement.append(shape_size)

                print(measurement)

                # Calculation History
                calculation_history = [['Area', area], ['Circumference', circumference]]
                print()
                # Sort by measurement...
                print("**** Shapes by measurement <highest to lowest> *******")
                for item in calculation_history:
                    print(item[0], item[1], )

                print()

                # sort alphabetically
                print("***** Measurements <Alphabetical> *******")
                for item in calculation_history:
                    print(item[0], item[1])

    elif what_shape in ['2','square']:
                print("***** Square *****")
                b = num_check("Base:", float)
                perimeter = b * 4
                area = b * b
                print("Perimeter of the Square = ", "{:.2f}".format(perimeter), what_unit)
                print("Area of the Square = ", "{:.2f}".format(area), what_unit+"^2")

                # Separate Lists
                shape_size = []
                measurement = []

                # Get inputs and add to shape_size list
                shape = ""
                shape_size = []
                shape = area

                # Get the perimeter
                size = perimeter

                # Add item name and cost to the 'item' list
                shape_size.append(area)
                shape_size.append(what_unit)
                shape_size.append(perimeter)
                shape_size.append(units)

                # Add item to the measurement list
                measurement.append(shape_size)

                print(measurement)

                # Calculation History
                calculation_history = [['Area', area], ['Perimeter', perimeter]]

                # Sort by measurement...
                print("**** Shapes by measurement <highest to lowest> *******")
                for item in calculation_history:
                    print(item[0], item[1], )

                print()

                # sort alphabetically
                print("***** Measurements <Alphabetical> *******")
                for item in calculation_history:
                    print(item[0], item[1])

    elif what_shape in ['3','rectangle']:
                print("***** Rectangle *****")
                b = num_check("Base: ", float)
                h = num_check("Height: ", float)
                perimeter = 2 * (b + h)
                area = b * h
                print("Perimeter of rectangle = ", "{:.2f}".format(perimeter), what_unit)
                print("Area of a rectangle = ", "{:.2f}".format(area), what_unit+"^2")

                # Separate Lists
                shape_size = []
                measurement = []

                # Get inputs and add to shape_size list
                shape = ""
                shape_size = []
                shape = area

                # Get the perimeter
                size = perimeter

                # Add item name and cost to the 'item' list
                shape_size.append(area)
                shape_size.append(what_unit)
                shape_size.append(perimeter)
                shape_size.append(units)

                # Add item to the measurement list
                measurement.append(shape_size)

                print(measurement)

                # Calculation History
                calculation_history = [['Area', area], ['Perimeter', perimeter]]

                # Sort by measurement...
                print("**** Shapes by measurement <highest to lowest> *******")
                for item in calculation_history:
                    print(item[0], item[1], )

                print()

                # sort alphabetically
                print("***** Measurements <Alphabetical> *******")
                for item in calculation_history:
                    print(item[0], item[1])

    elif what_shape in ['4','triangle' ]:
                print("***** Triangle *****")
                s1 = num_check("Side 1: ", float)
                s2 = num_check("Side 2:", float)
                s3 = num_check("Side 3:", float)
                perimeter = s1 + s2 + s3
                print("Perimeter of triangle = ", "{:.2f}".format(perimeter), what_unit)
                b = num_check("Base: ", float)
                h = num_check("Height: ", float)
                area = (b * h)/2
                print("Area of a triangle = ", "{:.2f}".format(area), what_unit+"^2")

                # Separate Lists
                shape_size = []
                measurement = []

                # Get inputs and add to shape_size list
                shape = ""
                shape_size = []
                shape = area

                # Get the perimeter
                size = perimeter

                # Add item name and cost to the 'item' list
                shape_size.append(area)
                shape_size.append(what_unit)
                shape_size.append(perimeter)
                shape_size.append(units)

                # Add item to the measurement list
                measurement.append(shape_size)

                print(measurement)

                # Calculation History
                calculation_history = [['Area', area], ['Perimeter', perimeter]]

                # Sort by measurement...
                print("**** Shapes by measurement <highest to lowest> *******")
                for item in calculation_history:
                    print(item[0], item[1], )

                print()

                # sort alphabetically
                print("***** Measurements <Alphabetical> *******")
                for item in calculation_history:
                    print(item[0], item[1])

    elif what_shape in ['5','parallelogram']:
                print("***** Parallelogram *****")
                b = num_check("Base: ", float)
                s1 = num_check("Side 1: ", float)
                perimeter = 2 * (b + s1)
                print("Perimeter of a Parallelogram = ", "{:.2f}".format(perimeter), what_unit)
                b = num_check("Base: ", float)
                h = num_check("Height: ", float)
                area = b * h
                print("Area of a Parallelogram = ", "{:.2f}".format(area), what_unit+"^2")

                # Separate Lists
                shape_size = []
                measurement = []

                # Get inputs and add to shape_size list
                shape = ""
                shape_size = []
                shape = area

                # Get the perimeter
                size = perimeter

                # Add item name and cost to the 'item' list
                shape_size.append(area)
                shape_size.append(what_unit)
                shape_size.append(perimeter)
                shape_size.append(units)

                # Add item to the measurement list
                measurement.append(shape_size)

                print(measurement)

                # Calculation History
                calculation_history = [['Area', area], ['Perimeter', perimeter]]

                # Sort by measurement...
                print("**** Shapes by measurement <highest to lowest> *******")
                for item in calculation_history:
                    print(item[0], item[1], )

                print()

                # sort alphabetically
                print("***** Measurements <Alphabetical> *******")
                for item in calculation_history:
                    print(item[0], item[1])


    # continue or exit the program
    keep_going = input("Press <enter> to continue or any key to quit: ")
    print()