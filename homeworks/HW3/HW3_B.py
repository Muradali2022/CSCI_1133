#Murad Ali, alixx800, Lab Section 008, Homework 3 Problem B

def main():
    game_num = 1
    game_win1 = 0
    game_win2 = 0
    while game_num < 4:
        game_num = str(game_num)
        print("Game", game_num + str(":"))
        user_input = input("Player1: ")
        user_input2 = input("Player2: ")
        game_num = int(game_num)
        game_num += 1 
        if rock_paper_scissors(user_input, user_input2) == 'W1':
            print("Player 1 Wins!")
            print()
            game_win1 += 1
        elif rock_paper_scissors(user_input, user_input2) == 'W2':
            print("Player 2 Wins!")
            print()
            game_win2 += 1
        else:
            print("It's a tie, nobody wins")
            print()
        if game_win1 == 2:
            print('')
            print("Final Determination: Player 1 won this round. ")
            game_num = 4
        elif game_win2 == 2:
            print('')
            print("Final Determination: Player 2 won this round. ")
            game_num = 4
        elif (game_num == 4) and (game_win1 == 1) and (game_win2 == 1):
            print('')
            print("It is a Tie! No one won this round.")
            game_num = 4 

def rock_paper_scissors (user_input, user_input2):
    if (user_input == 'R') and (user_input2 == 'S'):
        return 'W1'
    elif (user_input == 'S') and (user_input2 == 'P'):
        return 'W1'
    elif (user_input == 'P') and (user_input2 == 'R'):
        return 'W1'
    elif (user_input2 == 'R') and (user_input == 'S'):
        return 'W2'
    elif (user_input2 == 'S') and (user_input == 'P'):
        return 'W2'
    elif (user_input2 == 'P') and (user_input == 'R'):
        return 'W2'


if __name__ == "__main__":
    main()
    
        
    
