# calculator
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def display_operations():
  for symbol in operations:
      print(symbol)


def main(answer):
  if answer == None:
    answer = int(input("What's the first number ? : "))
  
  display_operations()

  operation_symbol = input("Pick an operation from the line above: ")  

  num = int(input("What's the next number ? : "))

  calculation_function = operations[operation_symbol]
  
  answer = calculation_function(answer, num)

  print(f"the answer is {answer}")

  rep = input("Type 'y' to continue calculating, or type 'n' to exit.: ")

  if rep in "yes":
    return main(answer)
  else:
    return answer
    
    

print(logo)
print(f"the result is {main(None)}")
