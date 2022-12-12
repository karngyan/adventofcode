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

GRID = []

class Node:
  def __init__(self, row, col):
    self.row = row
    self.col = col
  
  def __str__(self):
    return str(self.row) + "," + str(self.col)
  
  def __eq__(self, other):
    return self.row == other.row and self.col == other.col


def movable(frm, to, reverse=False):
  if reverse:
    frm, to = to, frm

  # elevation of S is a, elevation of E is z
  if to == 'S':
    to = 'a'
  elif to == 'E':
    to = 'z'
  
  if frm == 'S':
    frm = 'a'
  elif frm == 'E':
    frm = 'z'
  
  if to < frm:
    return True
  return abs(ord(to) - ord(frm)) <= 1

def take_in():
  for line in sys.stdin:
    line = line.strip()
    GRID.append(line)
  
  # a < b < c < d .. < z

def find_nodes(char):
  nodes = []
  for row in range(len(GRID)):
    for col in range(len(GRID[row])):
      if GRID[row][col] == char:
        nodes.append(Node(row, col))
  return nodes

def get_adjacent_nodes(node):
  nodes = []
  row = node.row
  col = node.col
  # up, down, left, right and movable
  if row > 0 and movable(GRID[row][col], GRID[row - 1][col], reverse=True):
    nodes.append(Node(row - 1, col))
  if row < len(GRID) - 1 and movable(GRID[row][col], GRID[row + 1][col], reverse=True):
    nodes.append(Node(row + 1, col))
  if col > 0 and movable(GRID[row][col], GRID[row][col - 1], reverse=True):
    nodes.append(Node(row, col - 1))
  if col < len(GRID[0]) - 1 and movable(GRID[row][col], GRID[row][col + 1], reverse=True):
    nodes.append(Node(row, col + 1))
  return nodes

def smallest_distance(frm):
  s = find_nodes(frm)[0]

  from collections import deque
  q = deque()
  used = {}
  d = {}
  p = {}

  q.append(s)
  used[str(s)] = True
  d[str(s)] = 0
  p[str(s)] = None

  while len(q) > 0:
    u = q.popleft()
    adjacent_nodes = get_adjacent_nodes(u)
    # print(u, adjacent_nodes)
    for v in adjacent_nodes:
      if not str(v) in used:
        used[str(v)] = True
        d[str(v)] = d[str(u)] + 1
        p[str(v)] = u
        q.append(v)

  return d

def main():
  take_in()
  # changing logic to find the shortest path from E to all other nodes
  # this changes movable logic a bit i.e. add support for reverse check
  d = smallest_distance('E')
  dist_to_s = d[str(find_nodes('S')[0])]
  print(dist_to_s)

  for node in find_nodes('a'):
    key = str(node)
    if key in d:
      dist_to_s = min(dist_to_s, d[key])
  
  print(dist_to_s)

  

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_12}', '{python3_execution_time_12} - ' + execution_time)
  