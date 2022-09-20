# year = int(input("What is the year of interest?"))
import csv

with open('le.csv') as file:
    file_content = csv.reader(file)
    for life_expectnacy in file_content:
        print(life_expectnacy)
