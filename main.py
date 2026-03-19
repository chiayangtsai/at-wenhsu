# windows

from basics import basic_print_usage
from basics import leetcode_find_max
from basics import basic_list_i
from basics import basic_for_loop
from basics import basic_range_usage
from basics import leetcode_shuffle_two_lists


if __name__ == '__main__':  # special meaning for Python execution, but we will talk about it later.
    
    testID = 6
    
    if testID == 0:
        print("hello World")
    elif testID == 1:
        basic_print_usage() #print
    elif testID == 2:
        basic_list_i() #list_i
    elif testID == 3:
        basic_for_loop() # loop : for
    elif testID == 5:
        leetcode_find_max()
    elif testID == 6:
        basic_range_usage() #range
    elif testID == 7:
        leetcode_shuffle_two_lists()
    else:
        print("Not a supported testID = %d" % (testID)  )


'''
------- baseic level -------
Part 1/3 - basics
- loop : for, while (go through) <====
- find min/max, in-place  <===
- bubble sort 
- shuffle, merge two sorted list
- time complexity : O(N) O(N^2)
- range() usage (go through)
- list_ii() : built-in function
- fuction usage
- copy concept : shallow copy, depp copy
- list_iii() : ":"
- call-by-reference, call-by-value
- ..........


Part 2/3 - basic algorithms



Part 3/3 - dynamic programming



------- leetcode 150 study plan -----


------- advanced level -------


'''