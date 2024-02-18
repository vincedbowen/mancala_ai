import math
import copy


class Bot:
    def __init__(self, depth, state, player_num):
        self.player_num = None
        self.state = None
        self.depth = None
        self.reset(depth, state, player_num)

    def reset(self, depth, state, player_num):
        self.depth = depth
        self.state = state
        self.player_num = player_num

    def minimax_alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or state.game_over:
            return self.evaluate_state(state), None
        best_move = None
        if maximizing_player:
            value = -math.inf
            # Loop through all possible random_opponent and check if it is valid
            for i in range(1, 7):
                if ((state.current_player == 1 and state.valid_move(i))
                        or (state.current_player == 2 and state.valid_move(state.player_two_pit_correction(i)))):
                    temp_state = copy.deepcopy(state)
                    temp_state.move(i)
                    # continue down the levels of the tree
                    new_val, _ = self.minimax_alpha_beta(temp_state, depth - 1, alpha, beta, False)
                    # compare random_opponent
                    if new_val >= value:
                        value = new_val
                        best_move = i
                    # reset alpha if needed
                    alpha = max(alpha, value)
                    # Actual alphabeta pruning. If the current value is >= beta, we no longer need to look for a
                    # maximum val, and can terminate the loop
                    if value > beta:
                        break
            # Return the tuple that holds the best move and the utility value
            return value, best_move
        else:
            value = math.inf
            # Loop through all possible random_opponent and check if it is valid
            for i in range(1, 7):
                if ((state.current_player == 1 and state.valid_move(i))
                        or (state.current_player == 2 and state.valid_move(state.player_two_pit_correction(i)))):
                    temp_state = copy.deepcopy(state)
                    temp_state.move(i)
                    new_val, _ = self.minimax_alpha_beta(temp_state, depth - 1, alpha, beta, True)
                    # compare random_opponent
                    if new_val <= value:
                        value = new_val
                        best_move = i
                    # Set beta if needed
                    beta = min(beta, value)
                    # Actual alphabeta pruning. If the current value is <= alpha, we no longer need to look for a
                    # minimum val and can terminate the loop
                    if value < alpha:
                        break
            # Return the tuple that holds the best move and the utility value
            return value, best_move

    def best_move(self, state):
        # Call minimax with alphabeta
        _, best_move = self.minimax_alpha_beta(state, self.depth, -math.inf, math.inf, True, )
        # ensure there is no runtime error
        state.move(best_move)

    def evaluate_state(self, state):
        # Utility function  :- Difference between P1 mancala and p2 mancala
        return state.virtual_board['player 1 mancala'] - state.virtual_board['player 2 mancala']
