height = 1.65
weight = 84

bmi = (85 / 1.64 ** 2)
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

#bmi calculator with interpretations
height = 1.85
weight = 85
bmi = weight /(height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
