#Imports
import operator

#Defining the variables
inputs = []
valid_modifiers = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}
#Restart prompt on error

def restart_prompt(errorMessage):
  print(errorMessage)
  answer = input("Do you want to restart? (y/n): ")
  return answer.lower() == 'y'

def askForInput(inputString):
    while True:
        user_input = input(inputString)
        try:
            user_input = float(user_input)
            return(user_input)
            break  # Exit the loop if valid
        except ValueError:
            if valid_modifiers.get(user_input) != None:
                return user_input
            elif restart_prompt("Invalid input! Please enter numbers only."):
                continue  # Restart the loop
            else:
                break  # Exit the script
            

inputs.append(askForInput("Enter the first value: "))
inputs.append(askForInput("Enter the Modifier: "))
inputs.append(askForInput("Enter the Second value: "))



def eval_binary_expr(op1, oper, op2):
    op1, op2 = float(op1), float(op2)
    return valid_modifiers[oper](op1, op2)

print(eval_binary_expr(*(inputs)))



