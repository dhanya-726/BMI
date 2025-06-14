def cal_bmi(weight,height):
    bmi=weight/(height**2)
    return round(bmi,2)

def classify_bmi(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi < 24.9:
        return "Normal weight"
    elif 25<=bmi<29.9:
        return "Overweight"
    elif bmi>29.9:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight=float(input("Enter your weight in kilograms: "))
        height=float(input("Enter your height in meters: "))
        if weight<=0 or height<=0:
            print("Weight and height must be positive numbers.")
            return

        bmi=cal_bmi(weight,height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"You are classified as: {category}")
    except:
        print("Invalid input. Please enter numbers only.")

if __name__=="__main__":
    main()
