import sys

sys.stdin = open("in", "r")
sys.stdout = open("out", "w")

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

def star_one_max_calories(calories):
  max_calories = 0
  for elf_calories in calories:
    total = sum(elf_calories)
    max_calories = max(max_calories, total)
  print(max_calories)

def star_two_sum_of_top_3(calories):
  all_sums = []
  for elf_calories in calories:
    all_sums.append(sum(elf_calories))
  all_sums.sort(reverse=True)
  print(sum(all_sums[:3]))

get_calories()
star_one_max_calories(CALORIES)
star_two_sum_of_top_3(CALORIES)
