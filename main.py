# windows

from basics import * 


if __name__ == "__main__":
    # special meaning for Python execution, but we will talk about it later.
    testID = 17

    if testID == 0:
        print("hello World")
    elif testID == 1:
        basic_print_usage()  # print
    elif testID == 2:
        basic_list_i()  # list_i
    elif testID == 3:
        basic_for_loop()  # loop : for
    elif testID == 5:
        basic_range_usage()  # range
    elif testID == 6:
        leetcode_shuffle_two_lists()
    elif testID == 7:
        basic_while_loop()  # while
    elif testID == 8:
        leetcode_find_max()
    elif testID == 9:
        leetcode_merge_two_sorted_lists()
    elif testID == 10:
        basic_swap()  # swap, unpack
    elif testID == 11:
        leetcode_bubble_sort()  # bubble sort
    elif testID == 12:
        basic_time_complexity()  # time complexity / space complexity
    elif testID == 14:
        leetcode_numbers_histogram()
    elif testID == 15:
        basic_list_ii() # built-in functions
    elif testID == 16:
        leetcode_stock_trade_i() #sliding window
    elif testID == 17:
        basic_copy_concept() #copy
    else:
        print("Not a supported testID = %d" % (testID))


"""
------- basic level -------
Part 1/3 - basics
- sliding window i  <== HW
- list_iii() : ":"
- copy concept : shallow copy, depp copy
- call-by-reference, call-by-value
- sliding window ii
- string, ASCII code, KES
- leetcode : histogram ii


Part 2/3 - basic algorithms
- dict : look-up table (LUT) / Hash table
- practice : two sum
- leetcode : roman to integer, integer to roman
- sliding window iii : longest sub string
- digit : decimal
- digit : binary

Part 3/3 - dynamic programming
- dynamic programming : recursive programming
- sort()
....


------- leetcode 150 study plan -----


------- advanced level -------


"""
