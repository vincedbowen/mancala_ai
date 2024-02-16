class MancalBot:
    def minimax_alpha_beta(self, state, depth, alpha, beta, maximizing_player, cur_player):
            if depth == 0 or state.game_over:
                return self.evaluate_state(state), None
            best_move = None
            if maximizing_player:
                value = -math.inf
                # Loop through all possible moves and check if it is valid
                for i in range(1, state.pits_index[1] + 1):
                    if state.valid_move(i):
                        temp_state = copy.deepcopy(state)
                        temp_state.play(i)
                        # continue down the levels of the tree
                        new_val, _ = self.minimax_alpha_beta(temp_state, depth - 1, alpha, beta, False, 3 - state.current_player)
                        # compare moves
                        if new_val > value:
                            value = new_val
                            best_move = i
                        # reset alpha if needed
                        alpha = max(alpha, value)
                        # Actual aplha beta pruning. If the current value is >= beta, we no longer need to look for a maximum val, and can terminate the loop
                        if value >= beta:
                            break
                # Return the tuple that holds the best move and the utility value
                return value, best_move
            else:
                value = math.inf
                # Loop through all possible moves and check if it is valid
                for i in range(1, state.pits_index[1] + 1):
                    if state.valid_move(i):
                        temp_state = copy.deepcopy(state)
                        temp_state.play(i)
                        new_val, _ = self.minimax_alpha_beta(temp_state, depth - 1, alpha, beta, True, 3 - state.current_player)
                        # compare moves
                        if new_val < value:
                            value = new_val
                            best_move = i
                        # Set beta if needed
                        beta = min(beta, value)
                        # Actual aplha beta pruning. If the current value is <= alpha, we no longer need to look for a minimum val and can terminate the loop
                        if value <= alpha:
                            break
                # Return the tuple that holds the best move and the utility value
                return value, best_move

                            
    def best_move(self, state, alpha_beta):
            # Call minimax or minimax with alphabeta
            if(alpha_beta):
                moves = self.minimax_alpha_beta(state, self.depth, -math.inf, math.inf, True, 1)
                # ensure there is no runtime error 
                if(moves[1] != None):
                    state.play(moves[1])
            else:
                moves = self.minimax(state, self.depth, True, 1)
                if(moves[1] != None):
                    state.play(moves[1])
                # self.generate_terminal_state(state, self.depth, 0)
                # pit = self.minimax(True, 1, self.terminal_list, state)
                # # The pit in this case is 
                # state.play(pit + 1)

    def evaluate_state(self, state):
        # Utility function  :- Difference between P1 mancala and p2 mancala
        return (state.player_one_side['mancala'] - state.player_two_side['mancala'])