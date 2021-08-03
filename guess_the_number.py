import random
'''
Computer will select random number and user will guess it
'''
# def guess(x):
#     random_number = random.randint(1,x)
#     guess = 0

#     while guess != random_number:
#         guess = int(input(f"Guess the number between 1 and {x}: "))

#         if(guess < random_number):
#             print(f"Try larger number than {guess}")
        
#         if(guess > random_number):
#             print(f"Try smaller number than {guess}")
#     print(f"Congratulation!, You guessed the number {random_number} correctly")

# guess(50)

'''
User will select random number and computer tries to guess it
'''

def computer_guess(y):
    low = 1
    high = y
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)??: ").lower()
        # print(feedback)
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Congratulation!, You guessed the number {guess} correctly")

computer_guess(1000)