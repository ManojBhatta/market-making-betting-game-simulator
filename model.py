"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    return sum(p * v for p, v in zip(probabilities, values))

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    take_threshold =  expected_value(range(1, sides + 1), [1/sides]*sides)
    reroll_faces, take_faces = [], []

    for s in range(1, sides +  1 ):
        if s < take_threshold:
            reroll_faces.append(s)
        else:
            take_faces.append(s)
    value = 0.5 * take_threshold + 0.5 * sum(take_faces) / len(take_faces)
    return {"value":value, "reroll_faces":reroll_faces}

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

