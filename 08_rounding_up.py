import math

# rounding function
def round_up(amount, round_to):
    # rounds amount UP to the specified amount (round_to)
    return int(round_to * round(math.ceil(amount) / round_to))


print("{}".format(round_up))
print("{:.2f}".format(round_up))