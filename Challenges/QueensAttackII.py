import math
import os
import random
import re
import sys


# Complete the queensAttack function below.

def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles_set = set([(n - i, j - 1) for i, j in obstacles])

    attackable_positions = 0
    start_position = (n - r_q, c_q - 1)

    def make_count(start_position, move_function, condition_function, attackable_positions, obstacles_set):
        current_position = start_position
        while condition_function(current_position) and not (move_function(current_position) in obstacles_set):
            attackable_positions += 1
            current_position = move_function(current_position)
            print(current_position)
        return attackable_positions

    # right
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0], position[1] + 1),
        lambda position: (position[1] < (n - 1)),
        attackable_positions,
        obstacles_set
    )

    # left
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0], position[1] - 1),
        lambda position: (position[1] > 0),
        attackable_positions,
        obstacles_set
    )

    # up
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] - 1, position[1]),
        lambda position: (position[0] > 0),
        attackable_positions,
        obstacles_set
    )

    # down
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] + 1, position[1]),
        lambda position: (position[0] < (n - 1)),
        attackable_positions,
        obstacles_set
    )

    # up-right
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] - 1, position[1] + 1),
        lambda position: (position[0] > 0) & (position[1] < n - 1),
        attackable_positions,
        obstacles_set
    )

    # up-left
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] - 1, position[1] - 1),
        lambda position: (position[0] > 0) & (position[1] > 0),
        attackable_positions,
        obstacles_set
    )

    # down-right
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] + 1, position[1] + 1),
        lambda position: (position[0] < n - 1) & (position[1] < n - 1),
        attackable_positions,
        obstacles_set
    )

    # down-left
    attackable_positions = make_count(
        start_position,
        lambda position: (position[0] + 1, position[1] - 1),
        lambda position: (position[0] < n - 1) & (position[1] > 0),
        attackable_positions,
        obstacles_set
    )

    return attackable_positions