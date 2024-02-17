from board.mancala_board import Board as mancala
from random_opponent import random_moves as rm
from bot.mancala_bot import Bot
from userInput import user_input as ui

game = mancala()
ui.get_turn_num()
while not game.game_over:
    random_moves = rm.random_move_generator(game)
    pit = ui.get_pit()
    game.play(pit)
    game.render_board()
print(game.winner)