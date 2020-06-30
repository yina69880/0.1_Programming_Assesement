calculation_history = [['Area', 1.0], ['Perimeter', 0.75]]

# Sort by measurement...
calculation_history.sort(key=lambda x: x[1])

# Output
print("***** Measurements <Most amount to Least amount> *****")
for shape in calculation_history:
    print("{}: {:.2f}m".format(shape[0], shape))
print()

# sort alphabetically
calculation_history.sort(key=lambda x: x[0])

print("***** Items <Alphabetical> *****")
for shape in calculation_history:
    print("{}: {:.2f}m".format(shape[0], shape[1]))