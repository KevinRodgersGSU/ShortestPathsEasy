import math
a = int(input("Enter first x coordinate: "))
b = int(input("Enter first y coordinate: "))
c = int(input("Enter second x coordinate: "))
d = int(input("Enter second y coordinate: "))
HW = int(math.dist([a],[c]) + math.dist([b],[d]))
print("Shortest Paths = ",math.comb(HW,2))
