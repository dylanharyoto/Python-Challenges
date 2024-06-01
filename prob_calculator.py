import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    result = []
    if len(self.contents) < num:
      return self.contents
    for i in range(num):
      x = random.choice(self.contents)
      self.contents.pop(self.contents.index(x))
      result.append(x)
    return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  final = []
  compare = []

  for key, value in expected_balls.items():
    for i in range(value):
      if not key in compare:
        compare.append(key)

  result = 0
  for i in range(num_experiments):
    hat_backup = copy.deepcopy(hat)
    final = hat_backup.draw(num_balls_drawn)
    count = 0
    for x in compare:
      if x in final:
        if final.count(x) >= expected_balls[x]:
          count += 1
          if count == len(compare):
            result += 1
      
  return result / num_experiments