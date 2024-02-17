import math
import random

class Board:
    def __init__(self, pits_per_player=6, stones_per_pit=4):
        # Constructor calls reset so we can run this through a loop without persistence 
        self.reset(pits_per_player, stones_per_pit)
        
    def reset(self, pits_per_player, stones_per_pit):
        """
        The psuedo-constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.player_one_side = {
            'mancala' : 0
        }
        self.player_two_side = dict()
        # Exclusive range, but make it one-indexed to support play style better
        for i in range(1, pits_per_player + 1):
            self.player_one_side[i] = stones_per_pit
            self.player_two_side[i] = stones_per_pit
        self.player_two_side['mancala'] = 0
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.pits_index = (1, self.pits_per_player)
        self.total_pits = pits_per_player * 2 + 2
        self.game_over = False
        self.winner = None
        
    def valid_move(self, pit):
        """
        Function to determine validity of a move. Return True if the move is valid
        """
        # Check the pit is in the range and the pit is non empty 
        if self.current_player == 1:
            if pit < self.pits_index[0] or pit > self.pits_index[1]:
                return False
            elif self.player_one_side[pit] == 0:
                return False
            else:
                return True
        else:
            if pit < self.pits_index[0] or pit > self.pits_index[1]:
                return False
            elif self.player_two_side[pit] == 0:
                return False
            else:
                return True

    def random_move_generator(self):
        """
        Function to generate random moves
        """
        pit = random.randrange(self.pits_index[0], self.pits_index[1] + 1)
        self.play(pit)

    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        win = self.winning_eval()
        if win[0] == True:
            # print(win[1])
            pass
        elif self.valid_move(pit) == False:
            # print("INVALID MOVE")
            pass
        else:
            move = self.current_player, " selects ",  pit
            self.moves.append(move)
            if self.current_player == 1:
                # empty the selected pit
                num_stones = self.player_one_side[pit]
                self.player_one_side[pit] = 0
                # distribute the stones towards the player's mancala
                initial_dist = math.floor((num_stones / self.total_pits))
                for key in self.player_one_side:
                    # Dictionaries have the same keys so we can use one for loop to increment everything
                    self.player_one_side[key] += initial_dist
                    self.player_two_side[key] += initial_dist
                # Number of leftover stones that need to go around less than one full time
                leftovers = num_stones % self.total_pits
                # increment or decrement the pit we are depositing into
                moving_pit = pit
                side = self.current_player
                # Check if mancala deposit was last play
                last_played = False
                while(leftovers > 0):
                    if(side == 1):
                        moving_pit -= 1
                    else:
                        moving_pit += 1
                    if(moving_pit < 1 and side == 1):
                        self.player_one_side['mancala'] += 1
                        side = 2
                        leftovers -= 1
                        moving_pit = 0
                        last_played = True
                    elif(moving_pit > 6 and side == 2):
                        self.player_two_side['mancala'] += 1
                        side = 1
                        leftovers -= 1
                        moving_pit = 7
                        last_played = True
                    else:
                        if(side == 1):
                            self.player_one_side[moving_pit] += 1
                        else:
                            self.player_two_side[moving_pit] += 1
                        leftovers -= 1
                        last_played = False
                # Check if the last play was an empty slot own that player's side and steal all the oppposites 
                if(last_played == False and self.player_one_side[moving_pit] == 1 and side == 1):
                    self.player_one_side['mancala'] += self.player_two_side[moving_pit]
                    self.player_two_side[moving_pit] = 0
                    self.player_one_side['mancala'] += 1
                    self.player_one_side[moving_pit] = 0
                # change current player 
                self.current_player = 2
            else:
                # empty the selected pit
                num_stones = self.player_two_side[pit]
                self.player_two_side[pit] = 0
                # distribute the stones towards the player's mancala
                initial_dist = math.floor((num_stones / self.total_pits))
                for key in self.player_two_side:
                    # Dictionaries have the same keys so we can use one for loop to increment everything
                    self.player_one_side[key] += initial_dist
                    self.player_two_side[key] += initial_dist
                # Number of leftover stones that need to go around less than one full time
                leftovers = num_stones % self.total_pits
                # increment or decrement the pit we are depositing into
                moving_pit = pit
                side = self.current_player
                # Check if mancala deposit was last play
                last_played = False
                while(leftovers > 0):
                    if(side == 1):
                        moving_pit -= 1
                    else:
                        moving_pit += 1
                    if(moving_pit < 1 and side == 1):
                        self.player_one_side['mancala'] += 1
                        side = 2
                        leftovers -= 1
                        moving_pit = 0
                        last_played = True
                    elif(moving_pit > 6 and side == 2):
                        self.player_two_side['mancala'] += 1
                        side = 1
                        leftovers -= 1
                        moving_pit = 7
                        last_played = True
                    else:
                        if(side == 1):
                            self.player_one_side[moving_pit] += 1
                        else:
                            self.player_two_side[moving_pit] += 1
                        leftovers -= 1
                        last_played = False
                # Check if the last play was an empty slot own that player's side and steal all the oppposites 
                if(last_played == False and self.player_two_side[moving_pit] == 1 and side == 2):
                    self.player_two_side['mancala'] += self.player_one_side[moving_pit]
                    self.player_two_side['mancala'] += 1
                    self.player_two_side[moving_pit] = 0
                    self.player_one_side[moving_pit] = 0
                # change current player 
                self.current_player = 1
        
    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        player_one_flag = False
        player_two_flag = False
        # Exclusive Range
        for i in range(1, self.pits_per_player + 1):
            if(self.player_one_side[i] != 0):
                player_one_flag = True
            if(self.player_two_side[i] != 0):
                player_two_flag = True
        # If either player has no non-empty pits, the other player gets all the seeds from their side
        if(player_one_flag == False or player_two_flag == False):
            for i in range(1, self.pits_per_player + 1):
                self.player_one_side['mancala'] += self.player_one_side[i]
                self.player_two_side['mancala'] += self.player_two_side[i]
                self.player_one_side[i] = 0
                self.player_two_side[i] = 0
            player_one_sum = self.player_one_side['mancala']
            player_two_sum = self.player_two_side['mancala']
            # End game and check who wins
            self.game_over = True
            if(player_one_sum > player_two_sum):
                self.winner = 1
                return (True, "Player One Won")
            elif(player_two_sum > player_one_sum):
                self.winner = 2
                return (True, "Player Two Won")
            else:
                self.winner = 0
                return (True, "Tie")
        else:
            return (False, None)

    def renderBoard(self):
        print(self.player_one_side)
        print("              ", self.player_two_side)