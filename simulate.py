from userInput.user_input import get_num_sims as gms
from board.game_board import Board as Mancala
from random_opponent import random_moves as rm
import numpy as np


def simulate_mancala():
    num_sims = gms()
    player_one_wins = 0
    player_two_wins = 0
    ties = 0
    num_moves = np.zeros(num_sims)
    game = Mancala()
    for i in range(num_sims):
        game.reset(6, 4, None)
        print("Simulating game ", i + 1)
        while not game.game_over:
            rm.random_move_generator(game)
        print(game.winner)
        if game.winner == 1:
            player_one_wins += 1
        elif game.winner == 2:
            player_two_wins += 1
        else:
            ties += 1
        num_moves[i] = (len(game.moves))

    print("Percentage of player one wins: {:.1%}".format(player_one_wins / num_sims))
    print("Percentage of player two wins: {:.1%}".format(player_two_wins / num_sims))
    print("Percentage of ties: {:.1%}".format(ties / num_sims))
    print("Average number of moves: {:.2f}".format(num_moves.mean()))


def main():
    simulate_mancala()


if __name__ == '__main__':
    main()
