import random

def rollingDice():
  first_roll = random.randint(1, 6)
  second_roll = random.randint(1, 6)
  sum = first_roll + second_roll
  print("The sum of dice is " + str(first_roll) +" + "+ str(second_roll) + " = " + str(sum))
  return sum

sum = rollingDice()

if(sum == 7 or sum == 11):
    print("You won")
elif(sum == 2 or sum == 3 or sum == 12):
    print("You Lost")
elif(sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10):
    goal = sum
    print("Your goal is now " + str(goal))
    sum = rollingDice()
    while(sum):
        if(sum == 7):
            print("You Lost")
            break
        elif(sum == goal):
            print("You won!!!")
            break
        else:
            sum = rollingDice()
