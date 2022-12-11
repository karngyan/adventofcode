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

MOD = 17 * 3 * 5 * 7 * 11 * 19 * 2 * 13

class Monkey:
  def __init__(self, id, items, operation, test_divisible_by, throw_to_true, throw_to_false):
    self.id = id
    self.items = items
    # 'old +/-/*// number'
    self.operation = operation
    self.test_divisible_by = test_divisible_by
    self.throw_to_true = throw_to_true
    self.throw_to_false = throw_to_false
    self.number_of_items_processed = 0
  
  def __str__(self):
    items = ', '.join(map(str, self.items))
    return f'Monkey {self.id}: {items}'
  
  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, index):
    if index >= len(self.items):
      return
    self.items.pop(index)

  def process_item(self, index, log = False, ignore_divide = False):
    if index >= len(self.items):
      return -1

    self.number_of_items_processed += 1
    item = self.items[index] % MOD
    if log: print(f"Monkey inspects item {item}")
    operation = self.operation.replace('old', str(item))
    result = eval(operation) % MOD
    if log: print(f"Worry level increases to {result} ; operation {operation}")
    if not ignore_divide: result //= 3
    if log: print(f"Monkey divides by 3 to get {result}")
    if log: print(f"Monkey throws item {result} to Monkey {self.throw_to_true if result % self.test_divisible_by == 0 else self.throw_to_false}")
    
    # test
    self.items[index] = result % MOD
    if result % self.test_divisible_by == 0:
      return self.throw_to_true
    else:
      return self.throw_to_false
  

MONKEYS = []

def get_monkey(id, data):
  srow = data[1].split(': ')
  items = list(map(int, srow[1].split(', ')))
  srow = data[2].split(': ')
  operation = srow[1][6:]
  srow = data[3].split(': ')
  test_divisible_by = int(srow[1].split(' ')[-1])
  srow = data[4].split(': ')
  throw_to_true = int(srow[1].split(' ')[-1])
  srow = data[5].split(': ')
  throw_to_false = int(srow[1].split(' ')[-1])

  return Monkey(id, items, operation, test_divisible_by, throw_to_true, throw_to_false)

def take_in(): 
  global MOD 
  data = []
  index = 0
  id = 0
  for line in sys.stdin:
    if index == 6:
      monkey = get_monkey(id, data)
      id += 1
      MONKEYS.append(monkey)
      data = []
      index = 0
      continue
    
    index += 1
    data.append(line.strip())

  monkey = get_monkey(id, data)
  # MOD *= monkey.test_divisible_by
  MONKEYS.append(monkey)


def levels_by_rounds(rounds, ignore_divide = False):
  for _ in range(rounds):
    for i in range(len(MONKEYS)):
      l = len(MONKEYS[i].items)
      MONKEYS[i].items = MONKEYS[i].items[::-1]
      for j in range(l - 1, -1, -1):
        throw_to = MONKEYS[i].process_item(j, log = False, ignore_divide = ignore_divide)
        MONKEYS[throw_to].add_item(MONKEYS[i].items[j])
        MONKEYS[i].remove_item(j)
      MONKEYS[i].items = MONKEYS[i].items[::-1]

  all = []
  for i in range(len(MONKEYS)):
    all.append(MONKEYS[i].number_of_items_processed)
  
  all.sort()
  print(all[-1] * all[-2])

def main():
  take_in()
  # levels_by_rounds(20)
  levels_by_rounds(10000, ignore_divide = True)

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_11}', '{python3_execution_time_11} - ' + execution_time)
  