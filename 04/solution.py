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


ASSIGNMENT_PAIRS = []

def take_in():
  for line in sys.stdin:
    line = line.strip()
    first, second = line.split(',')
    a, b = first.split('-')
    c, d = second.split('-')

    ASSIGNMENT_PAIRS.append((int(a), int(b), int(c), int(d)))

def find_number_of_pairs_full_contained():
  total = 0
  for pair in ASSIGNMENT_PAIRS:
    a, b, c, d = pair
    if a >= c and b <= d:
      total += 1
    elif c >= a and d <= b:
      total += 1
  return total

def find_number_of_pairs_partially_contained():
  total = 0
  for pair in ASSIGNMENT_PAIRS:
    a, b, c, d = pair
    if (a >= c and a <= d) or (b >= c and b <= d):
      total += 1
    elif (c >= a and c <= b) or (d >= a and d <= b):
      total += 1
  return total

def main():
  take_in()
  print(find_number_of_pairs_full_contained())
  print(find_number_of_pairs_partially_contained())

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_04}', '{python3_execution_time_04} - ' + execution_time)
  