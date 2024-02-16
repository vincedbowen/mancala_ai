from src.python.bot.mancala_bot import Bot as bot
from src.python.board.mancala_board import Board as mancala

game = mancala()
bot = bot(3, game, 2)
game.reset()
while(game.game_over == False):
        bot.reset(3, game, 1)
        bot.best_move(game, True)
        game.random_move_generator()
print(game.winner)
