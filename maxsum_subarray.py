# description: finds max sum sub-array in a given array
# output: maxsum and corresponding sub-array
# assumptions:
#     1. we are only interested in max sum > 0
#     2. ignore zeroes at extremities
# credits: Kandal's algorithm

def maxsum_subarray(arr):

    last_max = max_ending_here = 0
    pos = start = end = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        if not max_ending_here > 0: start = pos + 1
        if last_max < max_ending_here: end = pos
        last_max = max(last_max, max_ending_here)
        pos = pos + 1

    print "input  :", arr
    print "max_sum:", last_max
    if last_max:
        print "sub_array:", arr[start:end+1]
        print "(start: %d, end: %d)" %(start, end)

if __name__ == '__main__':
    a = [10, -3, -4, 2, 24, -6, -10]
    maxsum_subarray( a )
    print
  
    a = [1, -3, -4, 2, 24, -6, -10]
    maxsum_subarray( a )
    print
  
    a = [-1, -2, -5, -7, -10]
    maxsum_subarray( a )
    print
   
    a = [0, 0, 0, 10, -3, -4, 2, 24, 0, 0, 0, -6, -10]
    maxsum_subarray( a )
    print
 
    a = [10, -3, -4, 0, 0, 0, 2, 24, -6, -10]
    maxsum_subarray( a )
    print
 
    a = [0, 0, 0, 0, 0]
    maxsum_subarray( a )
    print
