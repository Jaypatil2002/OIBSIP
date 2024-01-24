def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m**2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18:
        return "You are underweight"
    elif 18 <= bmi < 25:
        return "You are heightful"   
    elif 25 <= bmi < 30:
        return "You are overweight"    
    else:
        return "You are Obese"    

weight = float(input("Enter your weight in kilograms: "))        
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
bmi_category = classify_bmi(bmi_result)

print(f"Your BMI is : {bmi_result: .2f}")
print(f"Classification : {bmi_category}")