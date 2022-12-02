#!/usr/bin/env python3

import sys, os, time

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'in'), "r")
sys.stdout = open(os.path.join(os.path.dirname(__file__), 'out'), "w")

def update_readme(placeholder, value):
  import fileinput
  file = os.path.join(os.path.dirname(__file__), '..', 'README.md')
  for line in fileinput.input(file, inplace=True):
    if line.startswith(placeholder):
      line = value
    print(line, end='')

points_map = { 'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3, 'R': 1, 'P': 2, 'S': 3 }
magic_map = {
  'X': 'R',
  'Y': 'P',
  'Z': 'S',
  'A': 'R',
  'B': 'P',
  'C': 'S',
  'R': 'R',
  'P': 'P',
  'S': 'S'
}

def get_points(opp, you):

  points = points_map[you]
  opp = magic_map[opp]
  you = magic_map[you]
  if opp == 'R':
    if you == 'R':
      points += 3
    elif you == 'P':
      points += 6
    else:
      points += 0
  elif opp == 'P':
    if you == 'R':
      points += 0
    elif you == 'P':
      points += 3
    else:
      points += 6
  else:
    if you == 'R':
      points += 6
    elif you == 'P':
      points += 0
    else:
      points += 3

  return points

def get_points_fixed_end(opp, what):

  whats = ''
  if what == 'X':
    whats = 'lose'
  elif what == 'Y':
    whats = 'draw'
  else:
    whats = 'win'

  opp = magic_map[opp]
  what_to_do_map = {
    'R': {
      'draw': 'R',
      'win': 'P',
      'lose': 'S'
    },
    'P': {
      'draw': 'P',
      'win': 'S',
      'lose': 'R'
    },
    'S': {
      'draw': 'S',
      'win': 'R',
      'lose': 'P'
    }
  }

  you = what_to_do_map[opp][whats]
  return get_points(opp, you)

def get_strategy_with_points():
  total = 0
  for line in sys.stdin:
    opp, you = line.split()
    # print(opp, you)
    points = get_points(opp, you)
    # print(points)  
    total += points

  return total

def get_strategy_with_points_fixed_end():
  total = 0
  for line in sys.stdin:
    opp, you = line.split()
    # print(opp, you)
    points = get_points_fixed_end(opp, you)
    # print(points)  
    total += points

  return total

def main():
  # print(get_strategy_with_points())
  print(get_strategy_with_points_fixed_end())

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_02}', '{python3_execution_time_02} - ' + execution_time)
  