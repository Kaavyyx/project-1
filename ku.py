import random

def welcome():
    print("lets start the 21 Number Game!")
    print("chooseyour number 1, 2, or 3 to a running total.")
    print("The one who causes the total to exceed 21 loses.")
    print("Let's start!")

def player_move(totalk):
    while True:
        try:
            h = int(input(f"Current total is {totalk}. Your move (1, 2, or 3): "))
            if h in [1, 2, 3]:
                return h
            else:
                print("Invalid move. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(totalk):
    # Computer strategy: choose a random move from 1, 2, or 3
    return random.choice([1, 2, 3])

def body():
    welcome()
    
    total = 0
    while total < 21:
        # Player's turn
        player_move = player_move(total)
        total += player_move
        if total > 21:
            print(f"Player chose {player_move}. Total is now {total}.")
            print("Player loses! The total exceeded 21.")
            break
        
        # Computer's turn
        computer_move = get_computer_move(total)
        total += computer_move
        print(f"Computer chose {computer_move}. Total is now {total}.")
        if total > 21:
            print("Computer loses! The total exceeded 21.")
            break

if __name__ == "__main__":
    body()
