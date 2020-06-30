calculation_history = [['Area', 1.0], ['Perimeter', 0.75]]

total = 0

# Add costs...
for item in calculation_history:
    total += item[1]

average = total / len(calculation_history)
print (average)
