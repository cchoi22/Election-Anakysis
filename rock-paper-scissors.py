# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
print(computer_choice)
if computer_choice == user_choice: 
    print('You tied')

elif computer_choice =='p' and user_choice == 'r': 
    print('Computer Wins')
elif computer_choice =='p' and user_choice == 's':
    print('User wins')
elif computer_choice =='r' and user_choice == 'p':
    print('User Wins')
elif computer_choice =='r' and user_choice == 's':
    print('Computer Wins')
elif computer_choice =='s' and user_choice == 'r':
    print('Computer Wins')
elif computer_choice =='s' and user_choice == 'p':
    print('Computer Wins')
else: 
    print('pelase enter valid option')
