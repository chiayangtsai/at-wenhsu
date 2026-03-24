# windows

from basics import basic_print_usage
from basics import leetcode_find_max
from basics import basic_list_i
from basics import basic_for_loop
from basics import basic_range_usage
from basics import leetcode_shuffle_two_lists
from basics import basic_while_loop
from basics import leetcode_merge_two_sorted_lists

if __name__ == '__main__':  # special meaning for Python execution, but we will talk about it later.
    
    testID = 8
    
    if testID == 0:
        print("hello World")
    elif testID == 1:
        basic_print_usage() #print
    elif testID == 2:
        basic_list_i() #list_i
    elif testID == 3:
        basic_for_loop() # loop : for
    elif testID == 5:
        basic_range_usage() #range
    elif testID == 6:
        leetcode_shuffle_two_lists()
    elif testID == 7:
        basic_while_loop() #while 
    elif testID == 8:
        leetcode_find_max()
    elif testID == 9:
        leetcode_merge_two_sorted_lists()
    else:
        print("Not a supported testID = %d" % (testID)  )


'''
------- baseic level -------
Part 1/3 - basics
- in-place concept <==
- time complexity : O(N) O(N^2)
- shuffle, merge two sorted list
- bubble sort 
- list_ii() : built-in function <== start leetcode from "easy"
- fuction usage
- copy concept : shallow copy, depp copy
- list_iii() : ":"
- call-by-reference, call-by-value
- ..........


Part 2/3 - basic algorithms
- 


Part 3/3 - dynamic programming



------- leetcode 150 study plan -----


------- advanced level -------


'''