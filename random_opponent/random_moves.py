import random


def random_move_generator(board):
    """
    Function to generate random random_opponent
    """
    pit = random.randrange(board.pits_index[0], board.pits_index[1] + 1)
    board.play(pit)
