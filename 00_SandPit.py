# Import goes here...
import math
# If statements!
keep_going = ""
while keep_going == "":

    # Number Checking Function
    def num_check(question, type):
        if type == float:
            err_type = "a number"
        error = "Please enter {} that is more than zero".format(err_type)

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

    # String Checking Function
    def string_checker(question, to_check):
        valid = False
        while not valid:

            response = input(question).lower()

            for item in to_check:
                if response == item:
                    return response
                elif response == item[0]:
                    return item

            print("sorry that is not a valid response. Please choose"
                  " triangle, square, circle, rectangle or parallelogram.")

    # Asks user for prefered shape
    prefered_shape = ["rectangle","triangle","circle","square","parallelogram"]
    shape = string_checker("Please choose between: rectangle, triangle, circle, square, parallelogram: ", prefered_shape)
    print(shape)

    def string_checker(question, to_check):
        valid = False
        while not valid:

            response = input(question).lower()

            for item in to_check:
                if response == item:
                    return response
                elif response == item[0]:
                    return item

            print("sorry that is not a valid response. Please choose between cm, mm or m")
    # Asks user for prefered units
    prefered_units = ["cm","m","mm"]
    units = string_checker("Please choose your units: cm, mm or m: ", prefered_units)
    print(units)

    def string_checker(question, to_check):
        valid = False
        while not valid:

            response = input(question).lower()

            for item in to_check:
                if response == item:
                    return response
                elif response == item[0]:
                    return item

            print("sorry that is not a valid response. Please choose between cm^2, mm^2 or m^2")
    #Asks user for prefered units squared
    prefered_units_squared = ["m^2", "mm^2", "cm^2"]
    units_squared = string_checker("Please choose your units for the area: cm^2, mm^2 or m^2: ", prefered_units_squared)
    print(units_squared)

    # Main Routine goes here...
    if shape == "rectangle":
        # Asks for height and width
        length = num_check("Length: ", float)
        width = num_check("Width: ", float)
        # Find area
        area = length * width
        print("Area: ", area, units_squared)
        # Find perimeter
        perimeter = (length + width) * 2
        print("Perimeter: ", perimeter, units)

        # Initialise Lists
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
        shape_size.append(units_squared)
        shape_size.append(perimeter)
        shape_size.append(units)


        # Add item to the measurement list
        measurement.append(shape_size)

        print(measurement)

        # Calculation History
        calculation_history = [['Area', area], ['Perimeter', perimeter]]

        # Sort by measurement...
        print("**** Items by measurement <highest to lowest> *******")
        for item in calculation_history:
            print(item[0], item[1],)

        print()

        # sort alphabetically
        print("***** Measurements <Alphabetical> *******")
        for item in calculation_history:
            print(item[0], item[1])

    if shape == "triangle":
        # Asks for height and base
        base = num_check("Base: ", float)
        height = num_check("Height: ", float)
        # Asks for area
        area = (base * height) / 2
        print("Area: ", area, units_squared)
        # Asks for 3 sides
        side_one = num_check("Side: ", float)
        side_two = num_check("Side: ", float)
        side_three = num_check("Side: ", float)
        # Asks for perimeter
        perimeter = side_one + side_two + side_three
        print("Perimeter: ", perimeter, units)

        # Initialise Lists
        shape_size = []
        measurement = []

        # Get inputs and add to item_cost list
        shape = ""
        shape_size = []
        shape = area

        # Get the cost
        size = perimeter

        # Add item name and cost to the 'item' list
        shape_size.append(shape)
        shape_size.append(units_squared)
        shape_size.append(size)
        shape_size.append(units)

        # Add item to the expense list
        measurement.append(shape_size)

        print(measurement)

        # Calculation History
        calculation_history = [['Area', shape], ['Perimeter', size]]

        # Sort by measurement...
        calculation_history.sort(key=lambda x: x[1], reverse=1)

        # Output
        print("**** Items by measurement <highest to lowest> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

        print()

        # sort alphabetically
        calculation_history.sort(key=lambda x: x[0])

        print("***** Items <Alphabetical> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

    if shape == "circle":
        # Asks for Radius and diameter
        radius = num_check("Radius: ", float)
        # Find area
        area = radius * radius * math.pi
        print("Area:", area, units_squared)
        # Find Circumference/Perimeter
        circumference = radius * 2 * math.pi
        print("Circumference: ", circumference, units)

        # Initialise Lists
        shape_size = []
        measurement = []

        # Get inputs and add to item_cost list
        shape = ""
        shape_size = []
        shape = area

        # Get the cost
        size = circumference

        # Add item name and cost to the 'item' list
        shape_size.append(shape)
        shape_size.append(units_squared)
        shape_size.append(size)
        shape_size.append(units)

        # Add item to the expense list
        measurement.append(shape_size)

        print(measurement)

        # Calculation History
        calculation_history = [['Area', shape], ['Perimeter', size]]

        # Sort by measurement...
        calculation_history.sort(key=lambda x: x[1], reverse=1)

        # Output
        print("**** Items by measurement <highest to lowest> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

        print()

        # sort alphabetically
        calculation_history.sort(key=lambda x: x[0])

        print("***** Items <Alphabetical> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

    if shape == "square":
        # Asks for side
        side = num_check("Side: ", float)
        # Find area
        area = side * side
        print("Area:", area, units_squared)
        # Find perimeter
        perimeter = side * 4
        print("Perimeter: ", perimeter, units)

        # Initialise Lists
        shape_size = []
        measurement = []

        # Get inputs and add to item_cost list
        shape = ""
        shape_size = []
        shape = area

        # Get the cost
        size = perimeter

        # Add item name and cost to the 'item' list
        shape_size.append(shape)
        shape_size.append(units_squared)
        shape_size.append(size)
        shape_size.append(units)

        # Add item to the expense list
        measurement.append(shape_size)

        print(measurement)

        # Calculation History
        calculation_history = [['Area', shape], ['Perimeter', size]]

        # Sort by measurement...
        calculation_history.sort(key=lambda x: x[1], reverse=1)

        # Output
        print("**** Items by measurement <highest to lowest> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

        print()

        # sort alphabetically
        calculation_history.sort(key=lambda x: x[0])

        print("***** Items <Alphabetical> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

    if shape == "parallelogram":
        # Asks for height and width
        base = num_check("Base: ", float)
        height = num_check("Height: ", float)
        # Find area
        area = base * height
        print("Area:", area, units_squared)
        # Find perimeter
        perimeter = (base + height) * 2
        print("Perimeter: ", perimeter, units)

        # Initialise Lists
        shape_size = []
        measurement = []

        # Get inputs and add to item_cost list
        shape = ""
        shape_size = []
        shape = area

        # Get the cost
        size = perimeter

        # Add item name and cost to the 'item' list
        shape_size.append(shape)
        shape_size.append(units_squared)
        shape_size.append(size)
        shape_size.append(units)

        # Add item to the expense list
        measurement.append(shape_size)

        print(measurement)

        # Calculation History
        calculation_history = [['Area', shape], ['Perimeter', size]]

        # Sort by measurement...
        calculation_history.sort(key=lambda x: x[1], reverse=1)

        # Output
        print("**** Items by measurement <highest to lowest> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

        print()

        # sort alphabetically
        calculation_history.sort(key=lambda x: x[0])

        print("***** Items <Alphabetical> *******")
        for item in calculation_history:
            print("{}: {:.2f} ".format(item[0], item[1]))

    # LOOP OR EXIT THE PROGRAM
    keep_going = input("Press <enter> to continue or any key to quit")
    print()