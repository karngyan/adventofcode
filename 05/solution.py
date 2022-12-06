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


STACKS = []
INSTRUCTIONS = []

def is_number(s):
  try:
    int(s)
    return True   
  except ValueError:
    return False

def apply_instruction(instruction):
  # move 1 from 2 to 3
  v = instruction.split(' ')
  num = int(v[1])
  frm = int(v[3]) - 1
  to = int(v[5]) - 1
  for _ in range(num):
    STACKS[to].append(STACKS[frm].pop())

def apply_instruction_star_two(instruction):
  # move 1 from 2 to 3
  v = instruction.split(' ')
  num = int(v[1])
  frm = int(v[3]) - 1
  to = int(v[5]) - 1
  intermediate_stack = []
  for _ in range(num):
    intermediate_stack.append(STACKS[frm].pop())
  intermediate_stack.reverse()
  for i in intermediate_stack:
    STACKS[to].append(i)
      

def parse_stack_row(row):
  stack_row = []
  for i in range(1, len(row), 4):
    stack_row.append(row[i])
  return stack_row

def take_in():
  for line in sys.stdin:
    if line.startswith('move'):
      INSTRUCTIONS.append(line)
    elif line.strip() == '':
      continue
    else:
      parsed_row = parse_stack_row(line)
      for i in range(len(parsed_row)):
        if len(STACKS) <= i:
          STACKS.append([])
        if parsed_row[i] != ' '  and not is_number(parsed_row[i]):
          STACKS[i].append(parsed_row[i])
  
  for stack in STACKS:
    stack.reverse()


def main():
  take_in()
  for instruction in INSTRUCTIONS:
    apply_instruction_star_two(instruction)
    # apply_instruction(instruction)
  ans = ''
  for stack in STACKS:
    ans += stack[-1]
  print(ans) 

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_05}', '{python3_execution_time_05} - ' + execution_time)
  