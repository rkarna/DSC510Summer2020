'''
DSC 510 T302
Purpose of Program: Calculate cost of installing fiber optics cable installation
Programming Assignment Week 2 - Programming Assignment 1.2
Author Rajasekharreddy Karna
06/13/2020
'''

print('Welcome to Python World') #Display company welcome message for user.
print ('') #Give a space line
cost_per_ft = float (0.87) #Defining cost of cable installation per feet
company_name = input('Please enter your company name: ') #Retrieve the company name from the user.
print ('') #Give a space line
print ('Welcome Mr. employee of', company_name, '. We are glad you visiting Python World.') #Printing another welcome message for user.
print ('') #Give a space line
len_of_cable = input("Please enter length of fiber optic cable you are looking to be installed: ") # Letting user to enter length of cable to install

#Defining the function to verify user entered data is numeric or not, if not numeric, letting user to re-enter valid data
def Check_On_Cable_Length(len_of_cable):
    while True:
        try:
            float (len_of_cable) #Verify user entered data is float (numeric with or without decimals)
            Install_Cost(len_of_cable) #Upon confirmation with entered data is numeric, calling Install Cost calculation function
            break  # Breaking function not to re-run
        except ValueError:
            print("Please enter valid length of fiber optic cable. Example: 100, 150, 200, etc. Try again!")  # Printing error message if user entered data is not numeric
            print('')  # Give a space line
            len_of_cable = input("Please enter length of fiber optic cable you are looking to be installed: ")  # Letting user to re-enter length of cable to install
            return Check_On_Cable_Length(len_of_cable) # Running function again to letting user to enter valid data this time

#Defining the Install Cost calculation function
def Install_Cost(len_of_cable):
            total_cost = {'Installation for:', len_of_cable, 'feet cable cost is = $', float(len_of_cable) * cost_per_ft} #Printing the total installation cost for user entered cable length
            print('') #Give a space line
            Print_Receipt(len_of_cable)

#Defining the Print Receipt function
def Print_Receipt(len_of_cable):
    print('***Quote from Python World - Print Receipt***') #Printing generic message
    print('       Client Company Name: ',company_name) #Printing client company name
    print('       Number of feet of fiber cable to be installed: ',len_of_cable) #Printing client entered length of cable to be installed
    print('       Installation Cost per feet: ', cost_per_ft) #Printing installation cost per feet for client reference
    print('       Total Cost: ', float(len_of_cable) * cost_per_ft) #Printing Total cost of installation
    print('')  # Give a space line
    print('Dear Customer, Total cost for installation of', len_of_cable, 'feet fiber optics cable is = $', float(len_of_cable) * cost_per_ft) #Printing total cost in a legible format
    print('')  # Give a space line
    print('***Thank You***') #Printing Thank You message

#Main Program to call the function
Check_On_Cable_Length(len_of_cable)