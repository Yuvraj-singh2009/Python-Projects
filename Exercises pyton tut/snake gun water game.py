import random
computer = [1,2,3]
a = 0
while a != 3:
  user = 0
  comp = 0

  user_choice = int(input("1 for snake,2 for gun, 3 for water: "))
  comp_choice = random.choice(computer)
  if user_choice == comp_choice:
    print("Match draw both lose!")
    print(f"you take {user_choice} and computer take {comp_choice}")
  elif user_choice == 1:
    if comp_choice == 2:
      print("Computer wins")
      print(f"you take {user_choice} and computer take {comp_choice}")
      comp += 1
      
      if comp_choice == 3:
        print("You wins")
        print(f"you take {user_choice} and computer take {comp_choice}")
        user += 1
  elif user_choice == 2:
    if comp_choice == 1:
      print("You wins")
      print(f"you take {user_choice} and computer take {comp_choice}")
      user += 1
      if comp_choice ==3:
        print("Computer wins")
        print(f"you take {user_choice} and computer take {comp_choice}")
        comp += 1
  elif user_choice == 3:
    if comp_choice == 1:
      print("Computer wins")
      print(f"you take {user_choice} and computer take {comp_choice}")
      comp += 1
      if comp_choice == 2:
        print("You win")
        print(f"you take {user_choice} and computer take {comp_choice}")
        user += 1
  a += 1
# print(f"Your points {user} and computer points {comp}")


      
      

