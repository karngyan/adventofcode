#!/usr/bin/env python3

import sys, os, time

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'in'), "r")
sys.stdout = open(os.path.join(os.path.dirname(__file__), 'out'), "w")

def hashable(l):
  return tuple(l)

def update_readme(placeholder, value):
  import fileinput
  file = os.path.join(os.path.dirname(__file__), '..', 'README.md')
  for line in fileinput.input(file, inplace=True):
    if line.startswith(placeholder):
      line = value
    print(line, end='')

MOVES = []

def take_in():
  for line in sys.stdin:
    line = line.strip()
    MOVES.append(line.split())

class position:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    key = f'{x},{y}'
    self.visited = {key: True}
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __str__(self):
    return str(self.x) + "," + str(self.y)
  
  def is_touching(self, other):
    # overlapping
    if self == other:
      return True

    # adjacent 
    if self.x == other.x and abs(self.y - other.y) == 1:
      return True
    elif self.y == other.y and abs(self.x - other.x) == 1:
      return True
    # diagonal
    elif abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1:
      return True
    
    return False

  def count_visited(self):
    return len(self.visited)

  def move_2(self, direction1, direction2):
    self.move(direction1, False)
    self.move(direction2, False)
    key = f'{self.x},{self.y}'
    self.visited[key] = True

  def move(self, direction, visited = True):
    if direction == 'U':
      self.y += 1
    elif direction == 'D':
      self.y -= 1
    elif direction == 'L':
      self.x -= 1
    elif direction == 'R':
      self.x += 1
    if visited:
      key = f'{self.x},{self.y}'
      self.visited[key] = True

def show_on_graph(head, tail):
  print(head, tail)

def move(number):
  knots = [position(0, 0) for _ in range(number)]
  for move in MOVES:
    direction = move[0]
    steps = int(move[1])
    for _ in range(steps):
      knots[0].move(direction)
      for i in range(1, len(knots)):
        head = knots[i - 1]
        tail = knots[i]
        if head.is_touching(tail):
          continue
        else:
          if head.x == tail.x:
            if head.y > tail.y:
              tail.move('U')
              # print("move tail in direction U", "to", tail)
            else:
              tail.move('D')
              # print("move tail in direction D", "to", tail)
          elif head.y == tail.y:
            if head.x > tail.x:
              tail.move('R')
              # print("move tail in direction R", "to", tail)
            else:
              tail.move('L')
              # print("move tail in direction L", "to", tail)
          else:
            if head.x > tail.x and head.y > tail.y:
              tail.move_2('R', 'U')
              # print("move tail in direction RU", "to", tail)
            elif head.x > tail.x and head.y < tail.y:
              tail.move_2('R', 'D')
              # print("move tail in direction RD", "to", tail)
            elif head.x < tail.x and head.y > tail.y:
              tail.move_2('L', 'U')
              # print("move tail in direction LU", "to", tail)
            elif head.x < tail.x and head.y < tail.y:
              tail.move_2('L', 'D')
              # print("move tail in direction LD", "to", tail)
        # show_on_graph(head, tail)
  return knots[-1].count_visited()

def main():
  take_in()
  print(move(2))
  print(move(10))


if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_09}', '{python3_execution_time_09} - ' + execution_time)
  