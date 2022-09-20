import math


def main():
    temperature = int(input("What is the temperature? \n"))
    temperature_type = input(" Degrees Fahrenheit or Celsius (F/C)? \n")

    if temperature_type.lower() == "f":
        windchill_func()
    else:
        new_temp = celsius_to_fahrenheit(temperature)
        windchill_func(new_temp)


def windchill_func(temperature):
    for number in range(5, 60, 5):
        windchill = 35.74 + (0.621 * (temperature)) - (35.75 * (math.pow(number, 0.16))
                                                       ) + (0.4275 * (temperature * (math.pow(number, 0.16))))
        new_windchill = round(windchill, 2)
        print(
            f"At temperature of {temperature: .1f}, and wind speed of {number} mph, the windchill is: {new_windchill: .2f}F")


def celsius_to_fahrenheit(temperature):
    new_temp = temperature * (9/5) + 32
    return new_temp


if __name__ == "__main__":
    main()
