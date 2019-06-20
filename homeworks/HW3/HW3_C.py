#Murad Ali, alixx800, Lab Section 008, Homework 3 Problem C

def main():
    print('Welcome to the installment loan evaluation program')
    print('')
    principal_amount = float(input("Please input the amount of money you will be borrowing: "))
    interest_rate = int(input("Please input the interest rate: "))
    term = int(input("Please input the term for the loan(in years): "))
    if (100 <= principal_amount <= 10000) and (interest_rate <= 15):
        total = face_value(principal_amount, interest_rate, term)
        total1 = float(total)
        time = term * 12
        monthly = '{0: .2f}'.format(total / time)
        print("")
        print("The face value of the loan is: $" + str(total1))
        print("Your monthly payment each month for",time,"is: $" + str(monthly))
    elif (100 <= principal_amount <= 10000) and (interest_rate > 15):
        print('')
        print("Error: The Interest Rate is too high, the maximum is 15 percent.")
    elif (principal_amount < 100):
        print('')
        print("Error: The principal amount is too low, the minimum is 100.")
    elif (principal_amount > 10000):
        print('')
        print("Error: The principal amount is too high, the maximum is 10000.")

def face_value(principal_amount, interest_rate, term):
    total_interest = principal_amount * (interest_rate / 100) * term
    face_value = total_interest + principal_amount
    return face_value

                             
if __name__ == "__main__":
    main()


