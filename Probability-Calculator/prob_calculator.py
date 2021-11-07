import copy
import random
from random import choice
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        for ball in balls:
            self.contents.extend([ball] * balls[ball])
        self.num_balls = len(self.contents)

    def draw(self, turns):
        removed_balls = []
        if turns >= self.num_balls:
            return self.contents
        for i in range(turns):
            chosen_ball = choice(self.contents)
            self.contents.pop(self.contents.index(chosen_ball))
            removed_balls.append(chosen_ball)
        return removed_balls

def compare_balls(expected_balls, balls):
    for key, value in expected_balls.items():
        if balls.count(key) < value:
            return False
    return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_successes = 0
    for n in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        if compare_balls(expected_balls, balls):
            experiment_successes += 1
    return experiment_successes / num_experiments