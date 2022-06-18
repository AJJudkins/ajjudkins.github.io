import math

items = int(input("Enter the number of items: \n"))
box = int(input("Enter the number of items per box: \n"))

boxes = math.ceil(items / box)

print(f"For {items} items, packing {box} items in each box, you will need {boxes} boxes.")
