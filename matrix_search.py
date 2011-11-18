##
# description: searches for an element in a matrix
# complexity : worst case of m + n, where m: #rows, n: #cols
##

import sys

M = [
    [ 1,  3,  6,  9, 13],
    [ 3,  7, 10, 11, 15],
    [ 7,  8, 12, 19, 25],
    [14, 19, 21, 32, 46],
    [51, 53, 64, 76, 81]
    ]

if __name__ == '__main__':
  for row in M:
    print row

  print
  num = int(raw_input("Enter num to search for: "))

  row = 0
  col = len(M[0]) - 1
  num_steps = 0
  steps = []

  while row < len(M) and col >= 0:
    num_steps = num_steps + 1
    steps.append(M[row][col])
    if num == M[row][col]:
      print "%d found at (%d, %d) in %d steps: %s" %(num, row+1, col+1, num_steps, ' -> '.join([str(x) for x in steps]))
      sys.exit()
    if num < M[row][col]: col = col - 1
    if num > M[row][col]: row = row + 1   # note: col might have changed

  print "%d not found after %d steps: %s" %(num, num_steps, ' -> '.join([str(x)
for x in steps]))
