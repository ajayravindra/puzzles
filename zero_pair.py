from random import random
from math import fabs

def abs(n):
    return int(fabs(n))

def bigrand():
    return int(10000000*random())

# Thank you, Mr. Knuth
def sample(arr, n):
    if not (arr and n):
        print "give me something to work with here"
        return None
    arr_size = len(arr)
    result = list()
    n_more = n
    idx = 0
    while idx < arr_size:
        if bigrand() % (arr_size-idx) < n_more:
            result.append(arr[idx])
            n_more -= 1
        idx += 1
    return result

# takes in a list of integers and returns (a list of) pairs whose sum = 0
# assumptions: integers don't repeat

def zero_pairs(arr):
    if not arr:
        print "(hash version): input array is empty, hence no zero pairs"
        return None

    results = list()    # of tuples
    watchdog = dict()   # of ints found in arr
    for i in arr:
        ii = abs(i)
        if i and -i in watchdog: results.append((ii, -ii))
        else: watchdog[i] = 1

    return results

def zero_pairs_brute_force(arr):
    if not arr:
        print "(brute force): input array is empty, hence no zero pairs"
        return None

    result = list()  # of tuples
    for i in arr:
        ii = abs(i)
        if i and -i in arr and (ii, -ii) not in result:
            result.append( (ii, -ii) )
    return result

##
# function: verify
#
# input : 
#   'a' is a list of integers
#   'b' is a list of tuples
#
# verification steps:
#    v1. tuples in 'b' are of the form (i, -i)
#    v2. for tuples (i, -i) in 'b', 'i' and '-i' are present in 'a'
#    v3. all tuples (i, -i) are present in 'b'
##
def verify(a, b):
    # check if all tuples in 'b' are of the form (i, -i)
    v1 = v2 = v3 = "pass"   # test case passes

    if b and not a:
        print "(v): tuples found where none were expected"
        v2 = "fail"

    if not b and not a:
        print "(v): the input array list and tuple list were empty"

    result = zero_pairs_brute_force(a)

    if a and not b and result:
        print "(v): the following (valid) tuples were not found"
        print result
        v3 = "fail"
        
    if a and b:
        for tup in b:
            if tup[0] != -tup[1]:
                v1 = "fail"
                print tup, "is invalid"
            if not (tup[0] in a and tup[1] in a):
                print "(v): at least one of", tup, "was not found in 'a'"
                v2 = "fail"

        for tup in result:
            if not tup in b:
                print "(v): ", tup, "was not found in 'b'"
                v3 = "fail"

    print "(v): v1 = %s, v2 = %s, v3 = %s" %(v1, v2, v3)

def test_zero_pairs():
    a = list()
    print "\ntest 1: empty array" %a
    res = zero_pairs(a)
    verify(a, res)

    a = range(-10, 11)
    print "\ntest 2: array = (-10, -9, .., 9, 10)"
    res = zero_pairs(a)
    verify(a, res)

    a = range(-10, 11)
    # let's pick N numbers in the list at random
    a = sample(a, 10)
    print "\ntest 3: array = %s" %a
    res = zero_pairs(a)
    verify(a, res)

    a = range(-100000, 100000)
    a = sample(a, 10000)
    print "\ntest 4: array = something really large"
    res = zero_pairs(a)
    verify(a, res)

if __name__ == '__main__':
    test_zero_pairs()
