# Calculate BMI
# 8 kyu

# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"

def bmi(weight, height):
    my_bmi = weight / (height ** 2)
    if not my_bmi <= 18.5:
        return 'Underweight'
    elif 18.5 < my_bmi <= 25:
        return 'Normal'
    elif 25 < my_bmi <= 30:
        return 'Overweight'
    else:
        return 'Obese'
    pass
