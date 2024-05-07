#rock paper scissors
import random   #importing random module

print('===================')
print('Rock Paper Scissors')
print('===================')

player = 0      #initionalizing player & computer             
computer = 0

#taking integer input for player
player = int(input('1)✊ \n2)✋ \n3)✌  \nPick a Number: '))
if player == 1:
    print("\n You chose: ✊")
elif player == 2:
    print("\nYou chose: ✋")
elif player == 3:
    print("\nYou chose: ✌")

#getting a random integer for computer    
computer = random.randint(1,3)
if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3:
    print("CPU chose: ✌")

#all cases  
if player == 1 and computer == 3:
    print("You Win")
elif player == 1 and computer == 2:
    print("You Lost")
    
elif player == 2 and computer == 1:
    print("You Win")
elif player == 2 and computer == 3:
    print("You Lost")
    
elif player == 3 and computer == 2:
    print("You Win")
elif player == 3 and computer == 1:
    print("You Lost")
else:
    print("You Tied")

   
    
