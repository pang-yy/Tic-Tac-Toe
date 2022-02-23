from random import choice
from sys import stdout
from time import sleep

global_game_end = False
global_board = [' ' for position in range(1,10)]

def main():
    printy("Tic Tac Toe by PYY".center(50, "="))
    sleep(0.5)
    user_choice = input("\
1)Play With Computer \n\
2)Play With Friend \n\
Enter 1-2: ")
    print("="*50)
    try:
        user_choice = int(user_choice)
        if user_choice == 1:
            with_pc()
        elif user_choice == 2:
            multiplayer()
        else:
            print("'1' OR '2' Only!")
    except ValueError:
        print("Enter Number Only!")

def multiplayer(game_end=global_game_end, board=global_board):
    print("="*50)
    printy("Win by achieve 3 in a row.")
    printy("Player 1: 'O', Player 2: 'X'")
    print("="*50)
    print("Board Position: ")
    board_description()
    while not(game_end):
        try:
            print("="*50)
            player_1 = input("(Player 1)Enter 1-9: ")
            player_1 = int(player_1)
            board_position = player_1 - 1
            if (player_1 >= 1) and (player_1 <= 9):
                if board[board_position] == " ":
                    board[board_position] = "O"
                    display_board()

                    player_2_can_move = not(board_full())
                    if check_winner():
                        print("="*50)
                        printy("Player 1 Win!")
                        game_end = True
                    elif not(check_winner()) and player_2_can_move:
                        try:
                            player_2 = input("(Player 2)Enter 1-9: ")
                            player_2 = int(player_2)
                            board_position = player_2 - 1
                            if (player_2 >= 1) and (player_2 <= 9):
                                if board[board_position] == ' ':
                                    board[board_position] = "X"
                                    display_board()

                                    if check_winner():
                                        print("="*50)
                                        printy("Player 2 Win!")
                                        game_end = True
                                else:
                                    print("Already Occupied")
                                    print("="*50)
                            else:
                                print("Not In Range")
                                print("="*50)
                        except ValueError:
                            print("Enter Number Only!")
                else:
                    print("Already Occupied")
                    print("="*50)
            else:
                print("Not In Range")
                print("="*50)
            #display_board()
            if not(check_winner()):
                game_end = board_full()
        except ValueError:
            print("Enter Number Only!")
    if not(check_winner()):
        print("="*50)
        printy("Draw!")
    printy("Game ended, thank you for playing.")
    print("="*50)

def with_pc(game_end=global_game_end, board=global_board):
    print("="*50)
    printy("Win by achieve 3 in a row.")
    printy("You: 'O', Computer: 'X'")
    print("="*50)
    print("Board Position: ")
    board_description()
    player_move_counter = 0
    while not(game_end):
        try:
            print("="*50)
            user = input("Enter 1-9: ")
            user = int(user) # change user input to integer
            board_position = user - 1
            if (user >= 1) and (user <= 9): # make sure input is within range
                if board[board_position] == " ": # check whether position is occupied
                    board[board_position] = "O"
                    player_move_counter += 1

                    pc_can_move = bool(available_move())
                    #print(check_winner())
                    if check_winner(): # check user win or not
                        print("="*50)
                        display_board()
                        printy("Wow, You Win!")
                        game_end = True
                    elif not(check_winner()) and pc_can_move:
                        #check if list is empty (if list empty is FALSE)
                        pc_move(available_move=available_move(), num_of_player_move=player_move_counter)
                        if check_winner():
                            print("="*50)
                            display_board()
                            printy("You Lose, as expected LOL.")
                            game_end = True

                else:
                    print("Already Occupied")
                    print("="*50)
            else:
                print("Not In Range")
                print("="*50)
            if not(check_winner()):
                display_board() #display board after every input
                game_end = board_full() #check if board full already
        except ValueError:
            print("Enter Number Only!")
    if not(check_winner()):
        print("="*50)
        printy("Draw!")
    printy("Game ended, thank you for playing.")
    print("="*50)

def pc_move(available_move, num_of_player_move, board=global_board):
    moved = False
    # TODO : AVOID 2 WINNING POSITION
    #        Eg: 
    #           O| |X
    #           -----
    #            |X| 
    #           -----
    #           O| |O
    # TODO : PRIOTISE THE POSITION THAT WILL WIN, INSTEAD OF BLOCKING PLAYER

    # first stage : avoid 2 possible winning position
    # if num_of_player_move == 2:
    #     if (board[0]=='O' and board[8]==' '):# impossible to have 3 move at this stage but just in case
    #         random_move = 8
    #         moved = True
    #     elif (board[2]=='O' and board[7]==' '):
    #         random_move = 7
    #         moved = True
    #     elif (board[7]=='O' and board[2]==' '):
    #         random_move = 2
    #         moved = True
    #     elif (board[8]=='O' and board[0]==' '):
    #         random_move = 0
    #         moved = True

    #second stage : PRIOTISE THE POSITION THAT WILL WIN, INSTEAD OF BLOCKING PLAYER

    #third stage : avoid player 3 in a row
    if not(moved): 
        if ((board[1]==board[2]!=' ' and board[0]==' ') or (board[3]==board[6]!=' ' and board[0]==' ') or (board[4]==board[8]!=' ' and board[0]==' ')):
            if board[0] == ' ':
                random_move = 0
                moved = True
        if ((board[0]==board[2]!=' ' and board[1] == ' ') or (board[4]==board[7]!=' ' and board[1] == ' ')):
            random_move = 1
            moved = True
        elif ((board[0]==board[1]!=' ' and board[2] == ' ') or (board[5]==board[8]!=' ' and board[2] == ' ') or (board[4]==board[6]!=' ' and board[2] == ' ')):
            random_move = 2
            moved = True
        elif ((board[0]==board[6]!=' ' and board[3] == ' ') or (board[4]==board[5]!=' ' and board[3] == ' ')):
            random_move = 3
            moved = True
        elif ((board[1]==board[7]!=' ' and board[4] == ' ') or (board[0]==board[8]!=' ' and board[4] == ' ') or (board[3]==board[5]!=' ' and board[4] == ' ')):
            random_move = 4
            moved = True
        elif ((board[2]==board[8]!=' ' and board[5] == ' ') or (board[3]==board[4]!=' 'and board[5] == ' ')):
            random_move = 5
            moved = True
        elif ((board[0]==board[3]!=' ' and board[6] == ' ') or (board[7]==board[8]!=' ' and board[6] == ' ') or (board[2]==board[4]!=' ' and board[6] == ' ')):
            random_move = 6
            moved = True
        elif ((board[1]==board[4]!=' ' and board[7] == ' ') or (board[6]==board[8]!=' ' and board[7] == ' ')):
            random_move = 7
            moved = True
        elif ((board[0]==board[4]!=' ' and board[8] == ' ') or (board[2]==board[5]!=' ' and board[8] == ' ') or (board[6]==board[7]!=' ' and board[8] == ' ')):
            random_move = 8
            moved = True
    #fouth stage : to do better move
    if not(moved):
        if 4 in available_move:
            random_move = 4
        elif (0 in available_move) or (2 in available_move) or (6 in available_move) or (8 in available_move):
            candidate_move = []
            if 0 in available_move:
                candidate_move.append(0)
            if 2 in available_move:
                candidate_move.append(2)
            if 6 in available_move:
                candidate_move.append(6)
            if 8 in available_move:
                candidate_move.append(8)
            random_move = choice(candidate_move)
        elif (1 in available_move) or (3 in available_move) or (5 in available_move) or (7 in available_move):
            candidate_move = []
            if 1 in available_move:
                candidate_move.append(1)
            if 3 in available_move:
                candidate_move.append(3)
            if 5 in available_move:
                candidate_move.append(5)
            if 7 in available_move:
                candidate_move.append(7)
            random_move = choice(candidate_move)
        else:
            random_move = choice(available_move)
    board[random_move] = "X"

def check_winner(board=global_board):# todo: use it to check whether one side won
    winner = False
    if ((board[0]==board[1]==board[2]) and board[0] != ' ') or ((board[3]==board[4]==board[5]) and board[3] != ' ') or ((board[6]==board[7]==board[8]) and board[6] != ' '):
        winner = True
    elif ((board[0]==board[3]==board[6]) and board[0] != ' ') or ((board[1]==board[4]==board[7]) and board[1] != ' ') or ((board[2]==board[5]==board[8]) and board[2] != ' '):
        winner = True
    elif ((board[0]==board[4]==board[8]) and board[0] != ' ') or ((board[2]==board[4]==board[6]) and board[2] != ' '):
        winner = True
    else:
        winner = False
    return winner

def available_move(board = global_board):
    available_list = []
    for count, position in enumerate(board):
        if position == " ":
            available_list.append(count)
    return available_list

def board_full(board = global_board):
    available = 9
    for position in board:
        if position != ' ':
            available -= 1
    if available == 0:
        return True

def printy(text, delay=0.05):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(delay)
    print()

def board_description():
    print(f"\
        1|2|3 \n\
        ----- \n\
        4|5|6 \n\
        ----- \n\
        7|8|9 \
    ")

def display_board(board = global_board):
    print(f"\
        {board[0]}|{board[1]}|{board[2]} \n\
        ----- \n\
        {board[3]}|{board[4]}|{board[5]} \n\
        ----- \n\
        {board[6]}|{board[7]}|{board[8]} \
    ")

main()
