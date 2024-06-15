from art import logo
import random


def generate_number():
    nubmer = random.randint(1, 100)
    return nubmer

def choose_dificulty():
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return dificulty

def play_game():
    
    num = generate_number()
    print(f"Pss correct number is {num}")
    
    attempts = 0
    difficulty = choose_dificulty()
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10

    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        if guess < num:
            print("To low")
        elif guess > num:
            print("To high")
        elif guess == num:
            print("Congratulations you win")
            return
        
        attempts-=1 

    if attempts == 0:
        print("you loose try next")


def main():
    print(logo)
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
    play_game()
    while(input("Wanna play 1 more?'yes' or 'no': ")) == "yes":
        print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
        play_game()


if __name__ == '__main__':
    main()

