import art
from game_data import data
import random
from replit import clear

def choose_pair():
    pair = random.choices(data,k=2)
    first = pair[0]
    second = pair[1]
    return first, second


def compare(a=dict, b=dict):
    key = 'follower_count'
    if a[key] > b[key]:
        return "A"
    elif b[key] > a[key]:
        return "B"
    else:
        return "same"


def play():
    
    right = True
    score = 0

    while right is True:
        print(art.logo)
        if score >= 1:
            print(f"Score is {score}")
        first, second = choose_pair()
        
        print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
        print("")
        print(art.vs)
        print("")
        print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")
        if input("Who has more followers? Type 'A' or 'B': ") == compare(first, second):
            score+=1
            clear()
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")
            right = False


play()