#DSC 510
#Week 2 Programming Assignment 1.2
#Programming Assignment Week 2
#Author Avishek Roy
#06/13/2020

if __name__ == '__main__':

    # Variable for per feet cost
    cost_per_feet = 0.87
    # Username Entry
    username = input("Enter username:")
    # Welcome message
    print('Welcome ' + username)
    # Username Entry
    company = input('Which Company you work for:')
    # Total number of feet Entry
    Length_Cable = float(input('Please enter number of feet of fiber optic cable to be installed:'))
    # Calculation
    total_cost = Length_Cable * cost_per_feet
    # Print of Reciept
    print('Receipt of sale')
    print('Name:' + str(username))
    print('Company name: ' + str(company))
    print('Amount to be charged: ' + str(total_cost) + '$')

