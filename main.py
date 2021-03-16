first_number=int(input("Enter the first number: \n"))
second_number=int(input("Enter the second number: \n"))
operation=input("What operation will you like to perform? ")
if operation == "division":
  answer=first_number/second_number
  print (f' your {operation} answer is {answer}')
elif operation == "adition":
  answer=first_number + second_number
  print (f' your {operation} answer is {answer}')

elif operation == "substraction":
  answer=first_number - second_number
  print (f' your {operation} answer is {answer}')
elif operation == "multiplication":
  answer=first_number * second_number
  print (f' your {operation} answer is {answer}')

else:
  print("Select and operation please")
 