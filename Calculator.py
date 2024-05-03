#Defining the variables
input1 = None
Input2 = None
Operator = None

#Restart prompt on error

def restart_prompt(errorMessage):
  print(errorMessage)
  answer = input("Do you want to restart? (y/n): ")
  return answer.lower() == 'y'

def askForNumberInput(inputString):
    while True:
        number = input(inputString)
        try:
            number = float(number)
            return(number)
            break  # Exit the loop if valid
        except ValueError:
            if restart_prompt("Invalid input! Please enter numbers only."):
                continue  # Restart the loop
            else:
                break  # Exit the script

input1 = askForNumberInput("Enter the first value: ")
input2 = askForNumberInput("Enter the second value: ")

print(input1, input2)
