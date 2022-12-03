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

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def find_common_letter_point(line):
  f_half = line[:len(line)//2]
  s_half = line[len(line)//2:]
  f_half_map = {}
  for letter in f_half:
    if letter in f_half_map:
      f_half_map[letter] += 1
    else:
      f_half_map[letter] = 1
  
  for letter in s_half:
    if letter in f_half_map:
      return letters.index(letter) + 1
  
  return 0

def solve_star_one():
  total = 0
  for line in sys.stdin:
    line = line.strip()
    val = find_common_letter_point(line)
    # print(val)
    total += val
  return total

def find_common_letter_point(a, b, c):
  for letter in a:
    if letter in b and letter in c:
      return letters.index(letter) + 1
  return 0

def solve_star_two():
  total = 0
  three = []
  for line in sys.stdin:
    line = line.strip()
    three.append(line)
    if len(three) == 3:
      val = find_common_letter_point(three[0], three[1], three[2])
      total += val
      three = []
  return total

def main():
  print(solve_star_two())



if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_03}', '{python3_execution_time_03} - ' + execution_time)
  