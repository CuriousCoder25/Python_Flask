#5/18 lab
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

print("\n Select an operation:: \t")

print("\n1. Add")
print("\n2. Subtract")
print("\n3. Multiply")
print("\n4. Divide\n")
take = int(input())
if take==1:
    print(f" Sum:",num1+num2)
    # print(f"Sum of {num1} and {num2} is: {num1+num2}")  
elif take==2:
    print(f" Difference:", num1-num2)
elif take==3:
    print(f" Product:", num1*num2)
elif take==4:
    print(f" Quiotent: ", num1/num2)
else:
    print("INVALID INPUT")
    
    #using switch case
# match take:
#     case 1:
#         print("\nSum: ",num1+num2)
#     case 2:
#         print("\nDifference: ",num1-num2)
#     case 3:
#         print("\nProduct: ",num1*num2)
#     case 4:
#         print("\n Quiotent: ",num1/num2)
