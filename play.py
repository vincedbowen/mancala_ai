from board.game_board import Board as mancala
from random_opponent import random_moves as rm
from bot.mancala_bot import Bot
from userInput import user_input as ui

game = mancala()
ui.get_turn_num()
while not game.game_over:
    pit = ui.get_pit()
    game.move(pit)
    game.simple_print()
print(game.winner)