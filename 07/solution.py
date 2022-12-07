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

CMDS = []
GRAPH = {}
ANSWER = 0
VIS = {}

'''
  directories -> size
  make a tree of directories
  and do a dfs to find this size
'''

def take_in():
  cmd = ''
  out = ''
  dir_stack = []
  for line in sys.stdin:
    line = line.strip()
    if line.startswith('$'):
      # cmd can be either cd or ls
      if '$ ls' in line:
        cmd = 'ls'
      elif '$ cd' in line:
        dir = line.split(' ')[2]
        if dir == '..':
          dir_stack.pop()
        else:
          dir_stack.append(dir)
        cmd = 'cd'
    else:
      if cmd == 'ls':
        # ls
        out += line
        current_dir = hash(hashable(dir_stack))
        if current_dir not in GRAPH:
          GRAPH[current_dir] = []
        if line.startswith('dir'):
          dir = line.split(' ')[1]
          dir_hash = hash(hashable(dir_stack + [dir]))
          if (dir_hash, 0) not in GRAPH[current_dir]:
            GRAPH[current_dir].append((dir_hash, 0))
        else:
          size = int(line.split(' ')[0])
          file = line.split(' ')[1]
          file_hash = hash(hashable(dir_stack + [file]))
          if (file_hash, size) not in GRAPH[current_dir]:
            GRAPH[current_dir].append((file_hash, size))

def dfs(node):
  global ANSWER, VIS
  if node not in GRAPH:
    return 0
  if node in VIS:
    return VIS[node]

  ans = 0

  for child in GRAPH[node]:
    ans += child[1]
    ans += dfs(child[0])
  
  if ans <= 100000:
    ANSWER += ans
  
  VIS[node] = ans
  return ans

def main():
  take_in()
  sys.setrecursionlimit(10000)
  # for node in GRAPH:
  #   print(node, *GRAPH[node])
  root = hash(hashable(['/']))
  dfs(root)
  print(VIS[root])
  DISK_SPACE = 70000000
  NEEDED_SPACE = 30000000
  CURRENT_UNUSED_SPACE = DISK_SPACE - VIS[root]
  MORE_SPACE_NEEDED = NEEDED_SPACE - CURRENT_UNUSED_SPACE

  print(ANSWER)

  MINIMUM_DIR_SIZE_TO_DELETE = 1e9+10
  for val in VIS.values():
    if val >= MORE_SPACE_NEEDED:
      MINIMUM_DIR_SIZE_TO_DELETE = min(MINIMUM_DIR_SIZE_TO_DELETE, val)

  print(MINIMUM_DIR_SIZE_TO_DELETE)

if __name__ == '__main__':
  start = time.process_time()
  main()
  end = time.process_time()
  execution_time = str((end - start) * 1000) + " ms"
  update_readme('{python3_execution_time_07}', '{python3_execution_time_07} - ' + execution_time)
  