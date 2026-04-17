# windows

from basics import * 


if __name__ == "__main__":
    # special meaning for Python execution, but we will talk about it later.
    testID =24

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
        leetcode_stock_trade_iii()
    elif testID == 18:
        basic_copy_concept() #copy : shallow copy, deep copy
    elif testID == 19:
        basic_list_iii() # :
    elif testID == 20:
        basic_call_by_reference() # call by reference, call by value
    elif testID == 21:
        basic_string_ascii() # string, ascii
    elif testID == 22:
        leetcode_alphabet_histogram() #KES, LUT
    elif testID == 23:
        basic_dict() #dict, look-up table (LUT)
    elif testID == 24:
        leetcode_two_sum() 
    elif testID == 30:
        basic_decimal_digit() #deciaml
    elif testID == 31:
        leetcode_reverse_digits()
    else:
        print("Not a supported testID = %d" % (testID))


"""
------- basic level -------


Part 2/3 - basic algorithms
- practice : two sum  <==== HW0416
- leetcode : roman to integer, integer to roman
- sliding window iii : longest sub string
- digit : decimal
- digit : binary

<-     able to start AI coding  : Cursor/Claude Code  -> light introduction

Part 3/3 - dynamic programming
- dynamic programming : recursive programming
- sort()
....


------- leetcode 150 study plan -----


------- advanced level -------


"""
