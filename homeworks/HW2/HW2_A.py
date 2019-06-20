#CSCI1133, Lab Section 008, HW2 Murad Ali, Problem A

import math

def main():
<<<<<<< HEAD
    length = int(input('Please enter the length: '))
    radius = int(input('Please enter the radius: '))
    viscosity = float(input('Please enter the viscosity: '))
    if ((length >= 0) & (radius >= 0) & (viscosity >= 0)):
        p = poiseuille(length, radius, viscosity)
        print ('The resistance is:', p)
    else:
        print ("Failed due to input error. Please make sure your puts are all positive. Exiting program.")


def poiseuille(length, radius, viscosity):
    poiseuille = ((8 * viscosity * length) / (math.pi * (radius**4)))
=======
    length = int(input("Please enter the length: "))
    radius = int(input("Please enter the radius: "))
    viscosity = float(input("Please enter the viscosity: "))
    if ((length >= 0) & (radius >= 0) & (viscosity >= 0)):
        p = poiseuille(length, radius, viscosity)
        print("The resistence is:", p)
    else:
        print("Failed due to input error. Please make sure your inputs are all positive. Exiting program")

def poiseuille(length,radius, viscosity):
    poiseuille = ((8 * viscosity * length) / (math.pi * (radius * 4)))
>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8
    return poiseuille
if __name__ == "__main__":
    main()
    
<<<<<<< HEAD

=======
>>>>>>> 4db8d19e15b78565e911e37440d4706473af13c8
