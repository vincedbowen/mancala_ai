import random


def random_move_generator(board):
    """
    Function to generate random moves
    """
    pit = random.randrange(board.pits_index[0], board.pits_index[1] + 1)
    board.play(pit)
