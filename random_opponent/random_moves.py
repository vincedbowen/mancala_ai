import random


def random_move_generator(board):
    """
    Function to generate random random_opponent
    """
    pit = random.randrange(1, 7)
    board.move(pit)
