#CSCI1133, Lab Section 008, HW2 Murad Ali, Problem C

def calories_short(height, weight, heart_rate, age, time):
    calories_burned = (((age * .074) + (heart_rate * .4472) - (weight * .05741) - 20.4402) * (time/4.184))
    return(calories_burned)

<<<<<<< HEAD
    
def calories_tall(height, weight, heart_rate, age, time):
    calories_burned1 = (((age * .02017) + (heart_rate * .6309) - (weight * .09036) - 55.0969) * (time/4.184))
=======
def calories_tall(height, weight, heart_rate, age, time):
    calories_burned1 = (((age * .02017) + (heart_rate * .6309) - (weight * .0936) - 55.0969) * (time/4.184))
>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8
    return(calories_burned1)

def main():
    height = float(input("Please input the height of the person (for example, 5.6 means 5 feet 6 inches): "))
    weight = int(input("Please input the body weight of person, in pounds: "))
<<<<<<< HEAD
    heart_rate = int (input("Please input the average heart rate of the person during the workout, in beats per minute: "))
    age = int(input("Please input the age of the person, in years: "))
    time = int(input("Please input the duration of the workout of the person, in minutes: "))
    print('')
    print('You entered the following information: ')
=======
    heart_rate = int(input("Please input average heart rate of the person during the workout, in beats per minute: "))
    age = int(input("Please input the age of the person, in years: "))
    time = int(input("Please input the duration of the workout of the person, in minutes: "))
    print('')
    print("You entered the following information: ")
>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8
    print("Height: ", height)
    print("Body weight: ", weight)
    print("Age: ", age)
    print("Average heart rate: ", heart_rate)
    print("Duration of workout: ", time)
<<<<<<< HEAD
    if height <= 5.6:
        cal_short = calories_short(height, weight, heart_rate, age, time)
        cal_short1 = int(cal_short + 1)
        print("The number of calories burned for this short person is", cal_short1, "calories.")
    else: 
        cal_tall = calories_tall(height, weight, heart_rate, age, time)
        cal_tall1 = int(cal_tall + 1)
        print("The number of calories burned for this tall person is", cal_tall1, "calories.")
   
        
=======
    if height > 5.6:
        cal_tall = calories_tall(height, weight, heart_rate, age, time)
        cal_tall1 = int(cal_tall + 1)
        print("The number of calories burned for this tall person is", cal_tall1, "calories.")
    else:
        cal_short = calories_short(height, weight, heart_rate, age, time)
        cal_short1 = int(cal_short + 1)
        print("The number of calories burned for this short person is", cal_short1, "calories.")
>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8

if __name__ == "__main__":
    main()
    
<<<<<<< HEAD
        
=======

>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8
    
