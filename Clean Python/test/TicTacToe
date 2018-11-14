#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:33:32 2018

@author: superlamer
"""

"""
This is a tic tac toe game 
Two players can play on the same computer
"""

from  IPython.display import clear_output
import random
import os
import sys

def cls():
    return lambda: os.system('clear')

def print_board(position):
    clear_output()
    cls()
    print("{0:s}".format(31 *"-"))
    print("{separator}{row1col1:>5}{separator:>5}{row1col2:>5s}{separator:>5}{row1col3:>5s}{separator:>5}".format(
            separator="|",
            row1col1=position['row1col1'],
            row1col2=position['row1col2'],
            row1col3=position['row1col3']))
    print("{0:s}".format(31 *"-"))
    print("{separator}{row2col1:>5}{separator:>5}{row2col2:>5s}{separator:>5}{row2col3:>5s}{separator:>5}".format(
            separator="|",
            row2col1=position['row2col1'],
            row2col2=position['row2col2'],
            row2col3=position['row2col3']))
    print("{0:s}".format(31 *"-"))
    print("{separator}{row3col1:>5}{separator:>5}{row3col2:>5s}{separator:>5}{row3col3:>5s}{separator:>5}".format(
            separator="|",
            row3col1=position['row3col1'],
            row3col2=position['row3col2'],
            row3col3=position['row3col3']))
    print("{0:s}".format(31 *"-"))
    
    
def check_score(position):
    if position['row1col1'] != "" and position['row1col1'] == position['row1col2'] == position['row1col3']: 
        return (True, position['row1col1'].upper())
    elif position['row2col1'] != "" and position['row2col1'] == position['row2col2'] == position['row2col3']: 
        return (True, position['row2col1'].upper())
    elif position['row3col1'] != "" and position['row3col1'] == position['row3col2'] == position['row3col3']: 
        return (True, position['row3col1'].upper()) 
    elif position['row1col1'] != "" and position['row1col1'] == position['row2col2'] == position['row3col3']: 
        return (True, position['row1col1'].upper())
    elif position['row3col1'] != "" and position['row3col1'] == position['row2col2'] == position['row1col3']: 
        return (True, position['row3col1'].upper())
    
    return (False, "")


def player_move(player, position):
    x = y = -1
    
    new_position = position
    
    while (x and y <= 0) or (x and y > 3):
        print("Enter column and row numbers separated by space.\nRow: Col:")
        x, y = map(int, input().split())
    
        update_cell = f"row{x}col{y}"
        
        if position[update_cell] != "":
            print(f"Cell at row: {x} col: {y} is already taken by: {position[update_cell]}")
            x = y = -1
        
    update_cell = f"row{x}col{y}"
    new_position[update_cell] = player
        
    return new_position
       
def congratulate_winner(player):
    print(f"Congratulations! Player {player} won!")
    

def check_full_board(position):
    return " " in position.values()
    

def choose_player_marker():
    markers = ("X", "O")
    first_player_marker = ""
    second_player_marker = ""
    
    while first_player_marker not in markers:
        first_player_marker = (input(f"Player 1, choose your markers \"{markers[0]}\" or \"{markers[-1]}\":")).upper()
    
    
    if (first_player_marker == markers[0]):
        second_player_marker = markers[-1]
    else:
        second_player_marker = markers[0]
    
    print(f"Player 1 will be: {first_player_marker}. Player 2 will be: {second_player_marker}")
    return (first_player_marker, second_player_marker)


def choose_who_goes_first():  
    return random.randint(0,2)

def restart_game():
    game_on()
    

def game_on():
    first_player, second_player = choose_player_marker()
    position = {'row1col1':'', 'row1col2':'', 'row1col3':'', 'row2col1':'', 'row2col2':'', 'row2col3':'', 'row3col1':'', 'row3col2':'', 'row3col3':''}
    game_over = False
    current_player = (first_player if choose_who_goes_first() == 0 else second_player)
    print_board(position)
    
    while not game_over:
        
        print(f"Player \"{current_player.upper()}\" turn" )
        new_position = player_move(current_player, position)
        print_board(new_position)
        is_winner = check_score(new_position)
        
        if is_winner[0]:
            congratulate_winner(is_winner[-1])
            game_over = True
        else:
            if current_player == first_player:
                current_player = second_player
            else:
                current_player = first_player
                
            if check_full_board(new_position):
                print("Board is full. It is a draw!")
                game_over = True
                
         
        position = new_position
        new_position = None
        
    another_game = ""
    while another_game != "y" and another_game != "n":
        another_game = (input("Play another game \"(Y)es\" or \"(N)o\"?"))[0].lower()
        
    if another_game == 'y':
        restart_game()
    else:
        print("Goodbye!")
        sys.exit(0)
        
game_on()