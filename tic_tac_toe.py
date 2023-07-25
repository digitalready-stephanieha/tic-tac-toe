# Stephanie Ha
# 7/20/23

import random

# Objective Make a tic-tac-toe game

#Main function 
def tic_tac_toe():
    # make a new empty grid
    grid = init_grid()
    
    print("New Game")
    show_grid(grid)
    
    game_over = False
    
    while not game_over:
    
    # take a user input and place an X at that point
        user = user_input(grid)
        grid = place_marker(grid, "X", user)
        
    # place a computer's move 
        comp = computer_move(grid)
        grid = place_marker(grid, "o", comp)
        print(f'The computer placed an o at position {comp}')
        
    # Show grid 
        show_grid(grid)
        
    # Check if anyone won 
        game_over = check_win(grid)
        
    # Game has ended 
    if game_over == "X":
        print('Congrats you won!')
    elif game_over == "o":
        print('You lost')
    else:
        print('Tie')
    
        
# Features:
# Store the 3 by 3 grid
def init_grid():
    return list(range(1,10))

# Place Xs and Os on the grid
def place_marker(grid, symbol, index):
    grid[index-1] = symbol # replacing grid index with symbol marker
    return grid

# Make a computer to play against
def computer_move(grid):
    while True:
        comp = random.randint(1,9)
        if type(grid[comp-1]) == int:
            return comp
    
# Take in user inputs
def user_input(grid):
    while True: # looping the entire function to ask position again 
        user = input('Select a position from 1-9: ')
        if user.isnumeric() and int(user) >= 1 and int(user) <= 9 and type(grid[int(user)-1]) == int: 
            return int(user)
        else:
            print('Invalid input, try again')
    
# Check if someone wins
def check_win(grid):
    # call winning_row on every possibility
    # if any produce a win, return that symbol 
    # else return False
    
    return winning_row(grid[0:3]) or \
    winning_row(grid[3:6]) or \
    winning_row(grid[6:9]) or \
    winning_row(grid[0:9:3]) or \
    winning_row(grid[1:9:3]) or \
    winning_row(grid[2:9:3]) or \
    winning_row(grid[0:9:4]) or \
    winning_row(grid[2:7:2])
    
#Check if a row has all Xs or Os 
def winning_row(row):
    if row[0] == row[1] and row[1] == row[2]: # transit property
        return row[0]
    else:
        return False
     
# Show the grid to the user 
def show_grid(grid):
    print(f"| {grid[0]} | {grid[1]} | {grid[2]} |\n\
-------------\n\
| {grid[3]} | {grid[4]} | {grid[5]} |\n\
-------------\n\
| {grid[6]} | {grid[7]} | {grid[8]} |")
    
# Check if the game is drawn
def stalemate(grid):
    return all(isinstance(cell, str) for cell in grid)
 
# Restriction/bugs
# What if the game draws?
# Illegal move (1-9)
# Illegal mov (already selected cell)
# How does our computer pick moves? 

if __name__ == "__main__":
    tic_tac_toe()