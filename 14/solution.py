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

BLOCKED = {}
MAX_Y = 0

def is_blocked(x, y, infinite_line_y = None):
  if infinite_line_y is not None:
    if y == infinite_line_y:
      return True
  return (x, y) in BLOCKED

def take_in():
  global MAX_Y, BLOCKED
  for line in sys.stdin:
    line = line.strip()
    line = line.split(' -> ')

    for i in range(len(line) - 1):
      frm = line[i].split(',')
      frm = (int(frm[0]), int(frm[1]))

      to = line[i + 1].split(',')
      to = (int(to[0]), int(to[1]))

      if frm[0] == to[0]:
        # vertical
        if frm[1] < to[1]:
          # down
          for i in range(frm[1], to[1] + 1):
            BLOCKED[(frm[0], i)] = True
            MAX_Y = max(MAX_Y, i)
        else:
          # up
          for i in range(to[1], frm[1] + 1):
            BLOCKED[(frm[0], i)] = True
            MAX_Y = max(MAX_Y, i)
      else:
        # horizontal
        if frm[0] < to[0]:
          # right
          for i in range(frm[0], to[0] + 1):
            BLOCKED[(i, frm[1])] = True
            MAX_Y = max(MAX_Y, frm[1])
        else:
          # left
          for i in range(to[0], frm[0] + 1):
            BLOCKED[(i, frm[1])] = True
            MAX_Y = max(MAX_Y, frm[1])
  

def simulate_one_unit_sand(sx, sy, max_y, infinite_line_y = None):
  x = sx
  y = sy
  while True:
    # try down, down-left, down-right
    if is_blocked(x, y + 1, infinite_line_y):
      if is_blocked(x - 1, y + 1, infinite_line_y):
        if is_blocked(x + 1, y + 1, infinite_line_y):
          # blocked
          BLOCKED[(x, y)] = True
          return (x, y)
        else:
          x += 1
          y += 1
      else:
        x -= 1
        y += 1
    else:
      y += 1
    
    if y > max_y:
      # flowed out
      return None

def star_one():
  ans = 0
  while simulate_one_unit_sand(500, 0, MAX_Y) is not None:
    ans += 1
  print(ans)

def star_two():
  ans = 1
  while simulate_one_unit_sand(500, 0, MAX_Y + 3, MAX_Y + 2) != (500, 0):
    ans += 1
  print(ans)

def main():
  take_in()
  # star_one()
  star_two()


if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_14}', '{python3_execution_time_14} - ' + execution_time)
  
