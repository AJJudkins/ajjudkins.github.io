age = int(input('What is your age? '))
maximum = (220 - age)
low = (maximum * .65)
high = (maximum * .85)
print(f"When you exercise to strengthen your heart,\
 you should keep your heart rate between{low: .0f} and{high: .0f} beats per minute.")
