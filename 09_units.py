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
units = ['km', 'm', 'cm', 'mm']
square_units = ['km^2', 'm^2', 'cm^2', 'mm^2']
what_unit = string_checker("What units do you want to use: km, m, cm, mm? ", units)
if what_unit in ["mm"]:
    print ('mm^2')