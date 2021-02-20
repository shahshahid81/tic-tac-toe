from math import ceil
from random import random

def get_single_block():
    return "   |"

def print_board(board):
    header = " " + "_" * 11
    top_row = "|" + get_single_block() * 3
    bottom_row = "|" + "___|" * 3
    marker_rows = [2,5,8]
    print(header)
    for i in range(1,10):
        if i % 3 == 0:
            print(bottom_row)
        elif i in marker_rows:
            middle_row = "|"
            board_position_lower_bound = i-2 
            board_position_upper_bound = i+1 
            for board_position in range(board_position_lower_bound, board_position_upper_bound):
                single_block = get_single_block()
                if board[board_position] != False:
                    marker = "X" if board[board_position] == 1 else "0"
                    single_block = single_block[0] +  marker + single_block[2:]
                middle_row += single_block
            print(middle_row) 
        else:
            print(top_row)

def check_if_player_has_won(current_player,total_moves,board):
    if total_moves < 5:
        return False
    win_conditions = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,5,9],
        [3,5,7],
        [1,4,7],
        [2,5,8],
        [3,6,9]
    ]
    for win_condition in win_conditions:
        first_block = win_condition[0] - 1
        second_block = win_condition[1] - 1
        third_block = win_condition[2] - 1 
        if board[first_block] == current_player and  board[second_block] == current_player and board[third_block] == current_player:
            return True
    return False
    

def select_player_turn_randomly():
    return ceil(random() * 2)

def print_current_player(current_player):
    print(f"Current Player: {current_player}")

def print_incorrect_value_error():
    print("Entered value is incorrect. Enter value between 1 and 9. Enter Exit to exit:")

def print_already_selected_value_error():
    print("Value selected already. Please select another one.")

def is_player_input_valid(player_input,board):
    if not(player_input == "exit" or player_input.isdigit()):
        print_incorrect_value_error()
        return False
    if player_input.isdigit():
        player_input = int(player_input) 
        if not (player_input >= 1 and player_input <= 9):
            print_incorrect_value_error()
            return False
        elif not board[player_input - 1] == False:
            print_already_selected_value_error()
            return False
    return True

def start_game():
    board = [False] * 9
    total_moves = 0
    # Can add option for entering player name [Need to refactor code to reflect this change]
    current_player = select_player_turn_randomly()
    while not total_moves == 9:
        print_current_player(current_player)
        player_input = input("Select between 1 and 9.Enter Exit to exit:")
        if not is_player_input_valid(player_input,board):
            continue
        if player_input == "exit":
            exit_game()
            break
        else:
            board[int(player_input) - 1] = current_player
            total_moves +=1
            print_board(board)
            if check_if_player_has_won(current_player,total_moves,board):
                # Can add option to restart game
                print(f'Player {current_player} has won the game')
                break
            current_player = 2 if current_player == 1 else 1

def exit_game():
    print("You have exited the game.")

start_game()