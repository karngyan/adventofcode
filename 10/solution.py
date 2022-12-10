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

INSTRUCTIONS = []

class instruction:
  def __init__(self, operation, argument):
    self.operation = operation
    self.argument = argument
  
  def __str__(self):
    return self.operation + " " + str(self.argument)

class register:
  def __init__(self):
    self.cycle = 0
    self.value = 1
  
  def process_instructions(self, instructions):
    for inst in instructions:
      if inst.operation == 'noop':
        self.cycle += 1
        yield self.cycle, self.value
      elif inst.operation == 'addx':
        self.cycle += 1
        yield self.cycle, self.value

        self.cycle += 1
        yield self.cycle, self.value
        self.value += inst.argument

def take_in():
  for line in sys.stdin:
    line = line.strip()
    v = line.split()
    operation = v[0]
    argument = 0
    if len(v) > 1:
      argument = v[1]
    INSTRUCTIONS.append(instruction(operation, int(argument)))

def split_in(x, num):
  chunks, chunk_size = len(x), len(x)//num
  return [x[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

def star_one():
  reg = register()
  ans = 0
  for cycle, x in reg.process_instructions(INSTRUCTIONS):
    # 20th, 60th, 100th, 140th, 180th, and 220th cycle
    # print(cycle, x)
    if cycle in [20, 60, 100, 140, 180, 220]:
      ans += (cycle * x)
  print(ans)

def star_two():
  reg = register()
  crt = ''
  for cycle, x in reg.process_instructions(INSTRUCTIONS):
    cycle = cycle % 40
    if cycle == 0:
      cycle = 40
    # print(cycle, x)
    if cycle in [x, x+1, x+2]:
      crt += '#'
    else:
      crt += '.'

  scrt = split_in(crt, 6)
  for s in scrt:
    print(s)

'''
##..##..#..##...##.##..##..##..##..##...
........................................
........................................
........................................
........................................
........................................

'''

def main():
  take_in()
  star_one()
  star_two()


if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_10}', '{python3_execution_time_10} - ' + execution_time)
  