#!/usr/bin/env python3

import sys, os, time

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'in'), "r")
sys.stdout = open(os.path.join(os.path.dirname(__file__), 'out'), "w")

def hashable(l):
  return tuple(l)

def update_readme(placeholder, value):
  import fileinput
  file = os.path.join(os.path.dirname(__file__), '..', 'README.md')
  for line in fileinput.input(file, inplace=True):
    if line.startswith(placeholder):
      line = value
    print(line, end='')

MAT = []

def take_in():
  for line in sys.stdin:
    line = line.strip()
    MAT.append([int(x) for x in line])

def count_visible_from_at_least_one_direction():
  ORD = [[0 for i in range(len(MAT[0]))] for j in range(len(MAT))]
  
  # row wise
  for i in range(len(MAT)):
    maxm = MAT[i][0]
    ORD[i][0] = 1
    for j in range(1, len(MAT[i])):
      if MAT[i][j] > maxm:
        ORD[i][j] = 1
        maxm = MAT[i][j]
    
  # column wise
  for j in range(len(MAT[0])):
    maxm = MAT[0][j]
    ORD[0][j] = 2
    for i in range(1, len(MAT)):
      if MAT[i][j] > maxm:
        ORD[i][j] = 2
        maxm = MAT[i][j]
      
    
  # reverse row wise
  for i in range(len(MAT)):
    maxm = MAT[i][-1]
    ORD[i][-1] = 3
    for j in range(len(MAT[i]) - 2, -1, -1):
      if MAT[i][j] > maxm:
        ORD[i][j] = 3
        maxm = MAT[i][j]
      

  # reverse column wise
  for j in range(len(MAT[0])):
    maxm = MAT[-1][j]
    ORD[-1][j] = 4
    for i in range(len(MAT) - 2, -1, -1):
      if MAT[i][j] > maxm:
        ORD[i][j] = 4
        maxm = MAT[i][j]
      
  
  ans = 0
  for i in ORD:
    for j in i:
      if j > 0:
        ans += 1
  
  return ans

def max_scenic_score():
  ROW = [[0 for i in range(len(MAT[0]))] for j in range(len(MAT))]
  COL = [[0 for i in range(len(MAT[0]))] for j in range(len(MAT))]
  RROW = [[0 for i in range(len(MAT[0]))] for j in range(len(MAT))]
  RCOL = [[0 for i in range(len(MAT[0]))] for j in range(len(MAT))]

  ans = 0

  for i in range(len(MAT)):
    for j in range(len(MAT[i])):
      # right
      right = 0
      for k in range(j + 1, len(MAT[i])):
        if MAT[i][k] < MAT[i][j]:
          right += 1
        elif MAT[i][k] >= MAT[i][j]:
          right += 1
          break

      # left
      left = 0
      for k in range(j - 1, -1, -1):
        if MAT[i][k] < MAT[i][j]:
          left += 1
        elif MAT[i][k] >= MAT[i][j]:
          left += 1
          break

      # down
      down = 0
      for k in range(i + 1, len(MAT)):
        if MAT[k][j] < MAT[i][j]:
          down += 1
        elif MAT[k][j] >= MAT[i][j]:
          down += 1
          break
      
      # up
      up = 0
      for k in range(i - 1, -1, -1):
        if MAT[k][j] < MAT[i][j]:
          up += 1
        elif MAT[k][j] >= MAT[i][j]:
          up += 1
          break
      
      ans = max(ans, right * left * down * up)

  return ans

def main():
  take_in()
  print(count_visible_from_at_least_one_direction())
  print(max_scenic_score())

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_08}', '{python3_execution_time_08} - ' + execution_time)
  