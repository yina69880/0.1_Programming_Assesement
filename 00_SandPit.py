distances = {"mile": 1609.34,
              "km": 1000,
              "m": 1,
              "cm": 0.01,
              "mm": 0.001
              }
info = input().split(" ")

if info[1] == info [3]: print("{:.2f}".format(float(info[0])))
else: print("{:.2f}".format(float(info[0]) * dict[info[1]] / dict[info[3]]))