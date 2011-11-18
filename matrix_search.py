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

def print_matrix(matrix):
  for row in matrix:
    print row

def search_matrix(matrix, num):
  row = 0
  col = len(matrix[0]) - 1
  steps = []

  while row < len(matrix) and col >= 0:
    steps.append(matrix[row][col])
    if num == matrix[row][col]:
      return True, row, col, steps
    if num < matrix[row][col]: col = col - 1
    if num > matrix[row][col]: row = row + 1   # note: col might have changed

  return False, row, col, steps

if __name__ == '__main__':
  print_matrix(M)
  num = int(raw_input("Enter num to search for: "))

  (found, row, col, steps) = search_matrix(M, num)
  if found:
    print "%d found at (%d, %d) after %d steps: %s" \
          %(num, row, col, len(steps), steps)
  else:
    print "%d not found after %d steps: %s" %(num, len(steps), steps)

