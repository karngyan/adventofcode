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

PAIRS = []

def take_in():
  import ast
  all = []
  for line in sys.stdin:
    all.append(line.strip())
  for i in range(0, len(all), 3):
    a = ast.literal_eval(all[i])
    b = ast.literal_eval(all[i + 1])
    PAIRS.append((a, b))

def recursive_compare(i, a, b):
  if i < len(a) and i >= len(b):
    return False

  if i >= len(a) and i < len(b):
    return True
  
  if i >= len(a) and i >= len(b):
    # inconclusive
    return None

  left = a[i]
  right = b[i]
  # print(left, right)
  # both are integers
  if isinstance(left, int) and isinstance(right, int):
    if left < right:
      return True
    elif left > right:
      return False
    else:
      return recursive_compare(i + 1, a, b)
  
  # both are lists
  if isinstance(left, list) and isinstance(right, list):
    v = recursive_compare(0, left, right)
    if v is None:
      return recursive_compare(i + 1, a, b)
    return v
  
  # exactly one in int
  if isinstance(left, int) and isinstance(right, list):
    v = recursive_compare(0, [left], right)
    if v is None:
      return recursive_compare(i + 1, a, b)
    return v
  
  if isinstance(left, list) and isinstance(right, int):
    v = recursive_compare(0, left, [right])
    if v is None:
      return recursive_compare(i + 1, a, b)
    return v
  
  return None

def star_one():
  ans = 0
  cnt = 1
  for a, b in PAIRS:
    # print(a, b)
    if recursive_compare(0, a, b):
      # print('in order')
      ans += cnt
    # else:
      # print('not in order')
    cnt += 1
  print(ans)

def compare(a, b):
  v = recursive_compare(0, a, b)
  if v is None:
    return 0
  if v:
    return -1
  return 1

def star_two():
  packets = [[[2]], [[6]]]
  for a, b in PAIRS:
    packets.append(a)
    packets.append(b)
  
  import functools
  packets.sort(key=functools.cmp_to_key(compare))
  p = packets.index([[6]])
  q = packets.index([[2]])
  print((p + 1) * (q + 1))


def main():
  take_in()
  star_one()
  star_two()
  # v = recursive_compare(0, [[1,7,[9,[2,2,5,4,5],4],[[0]]]], [[[[8],9,5,2]],[7],[0,8,[1,3,[6,5,10,2,6],9],9],[[[7,0,6,3]],[[2,1,5,9],7,[4,2,1,7],[3,0,0,10],10],[],[[4,9,3],[]],[]],[4]])
  # if v:
  #   print('in order')
  # else:
  #   print('not in order')


if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_13}', '{python3_execution_time_13} - ' + execution_time)
  