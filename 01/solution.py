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

CALORIES = []

def get_calories():
  if len(CALORIES) != 0:
    return CALORIES
  
  calories = []
  for line in sys.stdin:
    if line == "\n":
      CALORIES.append(calories)
      calories = []
    else:
      calories.append(int(line))

  CALORIES.append(calories)
  return CALORIES

def max_calories(calories):
  max_calories = 0
  for elf_calories in calories:
    total = sum(elf_calories)
    max_calories = max(max_calories, total)
  print(max_calories)

def sum_of_top_three(calories):
  all_sums = []
  for elf_calories in calories:
    all_sums.append(sum(elf_calories))
  all_sums.sort(reverse=True)
  print(sum(all_sums[:3]))

def main():
  get_calories()
  max_calories(CALORIES)
  sum_of_top_three(CALORIES)

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_01}', '{python3_execution_time_01} - ' + execution_time)
  