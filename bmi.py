height=float(input("enter the height in cm:"))
weight=float(input("enter the weight in KG:"))
bmi=weight/(height/100)**2
print("your BMI is",bmi)
if bmi<18.4:
    print("you are  underweight")
elif bmi<24.9:
    print("you are  healthy") 
elif bmi<29.9:
    print("you are  overweight")
elif bmi<34.9:
    print("you are  severly overweight")   
elif bmi<39.9:
    print("you are  obese")
else:
    print("you are severly obese")    
