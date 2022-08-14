# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:53:33 2022

@author: HP
"""

import numpy as np
import random

random.seed(1)

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board

def possibilities(board):
    return list(zip(*np.where(board == 0)))

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

board = create_board()

for i in range(6):
    for player in [1, 2]:
        random_place(board, player)

print(board)

def row_win(board, player):
    if np.any(np.all(board==player, axis=1)):
        return True
    else:
        return False
    
def col_win(board, player):
    if np.any(np.all(board==player, axis=0)):
        return True
    else:
        return False
                
def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        return True
    else:
        return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner 

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

results = [play_strategic_game() for i in range(1000)]
print(results.count(1))