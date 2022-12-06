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

LINES = []

def take_in():
  for line in sys.stdin:
    line = line.strip()
    LINES.append(line)

def find_index_last_four_char_are_distinct():
  ans = []
  for s in LINES:
    for i in range(len(s) - 13):
      if len(set(s[i:i+14])) == 14:
        ans.append(i + 14)
        break
  return ans


def main():
  take_in()
  print(find_index_last_four_char_are_distinct())

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_06}', '{python3_execution_time_06} - ' + execution_time)
  