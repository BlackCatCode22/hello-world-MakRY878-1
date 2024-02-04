
def incorrect_input (prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a numeric input.")


num1 = incorrect_input("Enter First Number: ")
num2 = incorrect_input("Enter Second Number: ")
num3 = incorrect_input("Enter Third Number: ")


#print("Error, please enter numeric input")
#quit()


print("\n\nYour numbers were: ", "\n",num1, "\n",num2, "\n",num3)
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3


print("\n\nThe largest number is:", largest)


