print('''
                             _
                          _dP"9b_
                        _dP"   "9b_
                      _dP"       "9b_
                    _dP"           "9b_
        8888888888888888888     8888888888888888888
        88      _dP"     88     88     "9b_      88
        88      "9b_     88     88     _dP"      88
        88  _      9b_   88     88   _dP"     _  88
        88_d8b_     "9b_ 88     88 _dP"     _d8b_88
        88P" "9b_     "9b88     8_dP"     _dP" "988
      _d88     "9b_     "9P     9P"     _dP"     88b_
    _dP"88       "9b_                 _dP"       88"9b_
  _dP"  8888888888888b               dP"88888888888  "9b_
_dP"                                                   "9b_
"9b_                                                   _dP"
  "9b_  8888888888888P             9b_8888888888888  _dP"
    "9b_88       _dP"               "9b_         88_dP"
      "988     _dP"                   "9b_       88P"
        88b_ _dP"       _dP     8d_     "9b_   _d88
        88"98P"       _dP"8     889b_     "9b_dP"88
        88          _dP" 88     88 "9b_          88
        88        _dP"   88     88   "9b_        88
        88       9b_     88     88     _dP       88
        8888888888888888888     8888888888888888888
                    "9b_           _dP"
                      "9b_       _dP"
                        "9b_   _dP"
                          "9b_dP"
                             "
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")