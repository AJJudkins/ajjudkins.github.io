from datetime import datetime


def main():
    gender = input("What is your gender? [M/F] \n")
    birthday = input("What is your birthday? [YYYY-MM-DD] \n")
    weight = float(input('Enter your weight in lbs: \n'))
    height = float(input('Enter your height in inches: \n'))
    age = compute_age(birthday)
    height_cm = cm_from_in(height)
    weight_kg = kg_from_lb(weight)
    bmi = body_mass_index(height=height, weight=weight)
    bmr = round(basal_metabolic_rate(gender, weight_kg, height_cm, age))
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_kg: .2f}")
    print(f"Height (cm): {height_cm: .1f}")
    print(f"Body mass index: {bmi: .1f}")
    print(f"Basal metabolic rate(kcal/day): {bmr}")
    pass


def compute_age(birth_str):

    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches):
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    bmi = round((10000 * weight) / (height ** 2))
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "f" or gender.lower() == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return bmr


main()
