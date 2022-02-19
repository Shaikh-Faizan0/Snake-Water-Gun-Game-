import random
computer = ['s' , 'w' , 'g']

chances =10
no_of_chances = 0
computer_point=0
human_point= 0

print("\t\t\t snake , water , gun Game\n\n")
print("s for snake\n w for water \n g for gun\n")

#making the game in while loop
while no_of_chances<chances :
      _input = input( 'snake , water , gun:')
      _random = random.choice(computer)
      if _input==_random :
          print("Tie Both 0 point to each \n")
        #if usere inpute s
      elif _input=="s" and _random=="g":
          computer_point=computer_point+1
          print(f"your gusse {_input} and computer gusse is {_random}\n")
          print("compute win 1 point \n")
          print(f"computer_point is {computer_point} and you point is {human_point}\n")
      elif _input== "s" and _random=="w":
          human_point=human_point+1
          print(f"your gusse {_input}and computer gusse is {random}\n")
          print("human wins 1 point \n")
          print(f"computer_pointer is {computer_point} and your points is {human_point}\n")
        #if usser inpute g
      elif _input == "g" and _random == "s":
          human_point = human_point + 1
          print(f"your gusse{_input}and computer gusse is {_random}\n")
          print("human wins 1 point \n")
          print(f"computer_point is {computer_point}and you point is {human_point}\n")
      elif _input == "g" and _random == "w":
          computer_point = computer_point + 1
          print(f"your gusse{_input} and computer gusse is {_random}\n")
          print("compute win 1 point \n")
          print(f"computer_point is {computer_point} and you point is {human_point}\n")
        #if usser inpute w
      elif _input == "w" and _random == "g":
          human_point = human_point + 1
          print(f"your gusse{_input} and computer gusse is {_random}\n")
          print("human wins 1 point \n")
          print(f"computer_point is {computer_point} and you point is {human_point}\n")
      elif _input == "w" and _random == "s":
          computer_point = computer_point + 1
          print(f"your gusse{_input} and computer gusse is {_random}\n")
          print("compute win 1 point \n")
          print(f"computer_point is {computer_point} and you point is {human_point}\n")
      else:
          print("you are inpute is wrong")

      no_of_chances = no_of_chances + 1
      print(f"{chances - no_of_chances} is left out of {chances} \n")

print("game over")
if computer_point==human_point:
    print("tie")
elif computer_point > human_point :
    print("you loss")
else:
    print("you win")
print(f"your points is {human_point} and computers points is {computer_point}")
