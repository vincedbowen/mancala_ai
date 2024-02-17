from src.python.bot.mancala_bot import Bot as bot
from src.python.board.mancala_board import Board as mancala
from src.python.moves import random_moves

game = mancala()
bot = bot(3, game, 2)
while not game.game_over:
    bot.reset(3, game, 1)
    bot.best_move(game, True)
    random_moves.random_move_generator(game)
    game.render_board()
print(game.winner)