# windows

def leetcode_fin_max():
    #Q: find the maximum value in a given list "a"
    a = [3, 6, -1, 7, 5, 4]

    max_value = a[0]
    for x in a:
        if x > max_value:
            max_value = x
    print(max_value)

    return


if __name__ == '__main__':  # special meaning for Python execution, but we will talk about it later.
    testID = 9
    if testID == 0:
        print("hello World")
    elif testID == 1:
        pass # print
    elif testID == 2:
        leetcode_fin_max()
    else:
        print("Not a supported testID = %d" % (testID)  )


'''
------- baseic level -------
Part 1/3 - basics
- if-else logic / and / or <===
- print() usage
- list_i() : basic operation, combine, +=
- loop : for, while (go through)
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