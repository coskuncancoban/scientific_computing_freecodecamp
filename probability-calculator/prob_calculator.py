import copy
import random

#construct the color list of balls.
class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  #use random to draw balls.
  def draw(self, n):
      n = min(n, len(self.contents))
      return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]
      
#use copy and calculate the probability.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  done = 0
  for i in range(num_experiments):
    another_hat = copy.deepcopy(hat)
    balls_drawn = another_hat.draw(num_balls_drawn)
    balls_req = sum([1 for key, value in expected_balls.items() if balls_drawn.count(key) >= value])
    done += 1 if balls_req == len(expected_balls) else 0

  return done / num_experiments
      
