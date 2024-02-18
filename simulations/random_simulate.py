import numpy as np
from board.game_board import Board as Mancala
from random_opponent import random_moves as rm
import streamlit as st


def simulate_mancala_random(num_sims):
    player_one_wins = 0
    player_two_wins = 0
    ties = 0
    wins = np.zeros(num_sims)
    game = Mancala()
    chart = st.line_chart()
    p1_wins_txt = st.text("Percentage of player one wins: ...")
    p2_wins_txt = st.text("Percentage of player two wins: ...")
    ties_txt = st.text("Percentage of ties: ...")
    print("----------------------------------------------")
    print("Simulating...")
    print("----------------------------------------------")
    for i in range(num_sims):
        print("Simulating game {}".format(i+1))
        game.reset(6, 4, None)
        while not game.game_over:
            rm.random_move_generator(game)
        if game.winner == 1:
            player_one_wins += 1
        elif game.winner == 2:
            player_two_wins += 1
        else:
            ties += 1
        wins[i] = player_one_wins
        chart.line_chart({"Player 1 Wins": wins[:i + 1], "Player 2 Wins": i + 1 - wins[:i + 1], "Ties": ties})
    p1_wins_txt.text("Percentage of player one wins: {:.1%}".format(player_one_wins / num_sims))
    p2_wins_txt.text("Percentage of player two wins: {:.1%}".format(player_two_wins / num_sims))
    ties_txt.text("Percentage of ties: {:.1%}".format(ties / num_sims))
    print("----------------------------------------------")
