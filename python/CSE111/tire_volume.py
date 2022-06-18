import math
from datetime import datetime

date_and_time = datetime.now()


width = int(input('Enter the width of the tire in mm (ex 205): '))
aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
volume = (math.pi * width ** 2 * aspect *
          (width * aspect + 2540 * diameter)) / (10000000000)

with open("volumes.txt", "at") as volume_file:
    print(f"{date_and_time:%Y-%m-%d}", file=volume_file, end="")
    print(f" {width}, {aspect}, {diameter}", file=volume_file, end="")
    print(f" {volume: .2f}", file=volume_file)
