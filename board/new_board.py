import math


class Board:
    def __init__(self, pits_per_player=6, stones_per_pit=4, user_player=None):
        """
        Constructor to make the mancala board. This actually just calls a reset function in order to avoid accidental
        persistence.
        :param pits_per_player: Optional parameter to specify how many pits each player has. Ie the game is customizable
        from the original rules of mancala. Default is 6.
        :param stones_per_pit: Optional parameter to specify how many stones to put in each pit. Ie the game is
        customizable from the original rules of mancala. Default is 4.
        :param user_player: Optional value to indicate which player the user wants to play, if they are playing.
        """
        self.winner = None
        self.game_over = None
        self.total_pits = None
        self.pits_index = None
        self.moves = None
        self.current_player = None
        self.user_player = None
        self.players = None
        self.virtual_board = None
        self.pits_per_player = None
        self.reset(pits_per_player, stones_per_pit, user_player)

    def reset(self, pits_per_player, stones_per_pit, user_player):
        """
        Resets the board and game to remove any idea of persistence. Extremely important due to the min-max function
        creating deep copies
        :param pits_per_player: How many pits each player has. Ie the game is customizable
        from the original rules of mancala. Default is 6.
        :param stones_per_pit: How many stones to put in each pit. Ie the game is
        customizable from the original rules of mancala. Default is 4.
        :param user_player: Value to indicate which player the user wants to play, if they are playing.
        """
        self.user_player = user_player
        self.pits_per_player = pits_per_player
        self.virtual_board = {'player 1 mancala': 0}
        for i in range(1, pits_per_player + 1):
            self.virtual_board[i] = stones_per_pit
        self.virtual_board['player 2 mancala'] = 0
        for i in range(pits_per_player + 1, 2 * pits_per_player + 1):
            self.virtual_board[i] = 0
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.pits_index = (1, self.pits_per_player)
        self.total_pits = pits_per_player * 2 + 2
        self.game_over = False
        self.winner = None

    def valid_move(self, pit):
        """
        Function to determine validity of a move
        :return: Boolean value for whether the move is valid or nor
        """
        # Check the pit is in the range and the pit is non-empty
        if self.current_player == 1:
            if pit < 1 or pit > self.pits_per_player:
                return False
        else:
            if pit < self.pits_per_player + 1 or pit > 2 * self.pits_per_player:
                return False
        if self.virtual_board[pit] == 0:
            return False
        else:
            return True

    def player_two_pit_correction(self, pit):
        """
        Because player two's pits are 7-12, when the user, bot, or random move generator picks a pit, we must change the
        value to match our internal data structure.

        :param pit: the pit entered [1,6] that must be corrected
        :returns: The correct value for the internal data structure
        """
        return pit + self.pits_per_player

    def move(self, pit):
        """
        Actually moves the stones according to the rules of mancala.
        :param pit: The pit that a player has selected
        """
        if self.current_player == 2:
            pit = self.player_two_pit_correction(pit)
        if self.winning_eval():
            self.game_over = True
        elif self.valid_move(pit):
            print("Invalid Move!")
        else:
            stones = self.virtual_board[pit]
            self.virtual_board[pit] = 0
            current_pit = pit
            while stones > 0:
                # Move towards mancala
                current_pit = (current_pit - 2) % 14 + 1
                if current_pit != 0 and current_pit != 14:
                    self.virtual_board[current_pit] += 1
                    stones -= 1
                elif current_pit == 14 and self.current_player == 2:
                    self.virtual_board['player 2 mancala'] += 1
                    stones -= 1
                elif current_pit == 0 and self.current_player == 1:
                    self.virtual_board['player 1 mancala'] += 1
                    stones -= 1
            self.can_capture(self.current_player, current_pit)
            play_again = self.check_for_play_again(self.current_player, current_pit)
            if not play_again:
                self.switch_player()

    def winning_eval(self):
        """
        Determines whether the game is over or not
        :return: Boolean value evaluating to true if the game has been completed
        """
        game_over = True
        for pit, stones in self.virtual_board.items():
            if pit != 'player 1 mancala' or pit != 'player 2 mancala':
                if stones > 0:
                    game_over = False
        return game_over

    def can_capture(self, current_player, ending_pit):
        """
        Checks if the last pit a stone was dropped in is on the player's side. If so, the player can capture the stones
        from opponent's pit across the board
        :param current_player: The player whose turn it currently is
        :param ending_pit: The last pit a stone was dropped as a dictionary key
        """
        if current_player == 1 and 1 <= ending_pit <= self.pits_per_player:
            if self.virtual_board[ending_pit] == 1:
                self.capture(ending_pit)
        elif current_player == 2 and self.pits_per_player + 1 <= ending_pit <= 2 * self.pits_per_player:
            if self.virtual_board[ending_pit] == 1:
                self.capture(ending_pit)

    def capture(self, ending_pit):
        """
        Actually captures the stone from the opponent's opposite pit
        :param ending_pit: The pit in which to the current opponent ended on
        """
        opposite = (2 * self.pits_per_player + 1) - ending_pit
        self.virtual_board[ending_pit] += opposite
        self.virtual_board[opposite] = 0

    def check_for_play_again(self, current_player, ending_pit):
        """
        Determines if the player dropped the last stone in their own store. In that case, the player gets to play again
        :param current_player: The player whose turn it currently is
        :param ending_pit: The last pit a stone was dropped in as a dictionary key
        :return: A boolean value representing whether the player should play again
        """
        if current_player == 1 and ending_pit == 'player 1 mancala':
            return True
        elif current_player == 2 and ending_pit == 'player 2 mancala':
            return True
        else:
            return False

    def determine_winner(self):
        """
        Determines who won the game
        :return: The winner of the game. If the game is a tie, return None
        """
        if (self.virtual_board['player 1 mancala'] > self.virtual_board['player 2 mancala']):
            return 1
        elif (self.virtual_board['player 2 mancala'] > self.virtual_board['player 1 mancala']):
            return 2
        else:
            return None

    def switch_player(self):
        """
        Switches who the current player is
        """
        self.current_player = 3 - self.current_player

    def simple_print(self):
        """
        Simply renders the board as the underlying dictionary data structure.
        """
        print(self.virtual_board)
