import random
import sys
#Array of possible fortunes
fortune_list = ['The fortune you seek is in another cookie',
                'A closed mouth gathers no feet.',
                'A conclusion is simply the place where you got tired of thinking.',
                'A cynic is only a frustrated optimist.',
                'A foolish man listens to his heart. A wise man listens to cookies.' ]
#user input
Answer = str.lower(input(("Would you like to know your fortune? Yes or No?")))

#takes user input and corresponds it to corresponding responses
if Answer == "no":
    print(input("Come back when you want you future told..."))
elif Answer == "yes":
    print(input(random.choice(fortune_list)))
else:
    print("Listen to my question next time!")
    break:
