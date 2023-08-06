"""
  Игра угадай число, доработанная
  
"""
import game_v2 as g2

def predict_soft(number = 1) -> int:
  """_summary_

  Args:
      number (int, optional): _description_. Defaults to 1.

  Returns:
      int: count - число попыток
  """
  count = 0
  range_value = 10

  while range_value < number:
    count += 1
    range_value += 10

  for i in range(range_value-10,range_value+1):
    count += 1
    if i == number:
      return count

g2.score_game(predict_soft)