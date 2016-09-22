
weight=(float(input('How much do you weigh in lbs?')))
height=(float(input('What is your height in inches?')))

bmi = 703*(weight/height*2)

if bmi <= 18.5: 
    print('bmi, You are underwight')

elif bmi <= 18.5 and bmi >= 24.9:
    print('bmi, You weigh normal for your height')

elif bmi <= 25 and bmi >= 29.9:
    print('bmi, You are overweight')

else:
    print('bmi, You are obese')