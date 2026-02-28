import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        # Return all balls if draw amount exceeds available
        if num >= len(self.contents):
            all_balls = self.contents[:]
            self.contents.clear()
            return all_balls
        
        # Draw without replacement
        drawn_balls = []
        for _ in range(num):
            # random.randrange ensures a different result on each run
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m_successes = 0

    for _ in range(num_experiments):
        # IMPORTANT: Deepcopy ensures the next experiment has a fresh hat
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Check if drawn balls satisfy expected_balls criteria
        # Logic: If we need 2 red and get 3, it is STILL a success.
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                success = False
                break
        
        if success:
            m_successes += 1

    # Probability = Successful Trials / Total Trials
    return m_successes / num_experiments