#DSC 510
#Week 2 Programming Assignment 1.2
#Programming Assignment Week 2
#Sri Renganathan Sankaranarayanan
#06/13/2020
#the purpose of the program, assignment number, and your name.

print("### Week 2 Programming Assignment 1.2 ####")
print('\n')
print("### 06/13/2020 ###")
print('\n')


print("### Good Day ! Welcome to our OFC Quote Estimate Site ####")

##Obtain user Input here

company_name=input("please enter your company Name: ")
length_req=input("please provide the length of the cable installation required(enter number of feet) :")
length=float(length_req)

# Calculate the cost by multiplying 0.87 to the requested feet of OFC

total_cost=length * 0.87

## Publish result
print("Total_Cost for",company_name, " to install", length, " feet of OFC Cable (Calculated for .87/feet): $" + str(total_cost))

## Thank the User and conclude

print("We appreciate the business and opportunity to service", company_name, ". Please contact our customer service with this estimate to proceed further on the OFC install")


