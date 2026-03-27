def basic_time_complexity():
    """
        #     time
    A   10     1
        20     4
        30     9
        40    16

    B   10     2
        20     4
        30     6
        40     8

    time complexity :
        A : O(N^2)
        B : O(N)

    if the execution time increase is irrelevant to input data size
       => O(N^0) = O(1)  : O-one

    """
    """
    input data size N

    # time complexity : O(N^2)
    for i in ...N
        for j in ... N
            ....


    # time complexity : O(N)
    for i in ...N <== N
        ....

    for j in ....N <== N
        .....


    # time complexity : O(N^2)
    for i in ...N <== N
        ....
    
    for j in ....N       <== N^2
        for k in ...N
        .....
    
            

    """

    return


def basic_while_loop():
    """
    for : very useful to "one container" loop structure
        for x in [.....]  : stop when all elements were iterated

    while : general purpose loop structure
        while "satisfied condition" :
            ....

    """
    data = [3, 1, 5, 4, 2]
    # Q: print out the elements in data one-by-one
    for x in data:
        print(x)

    print("----")

    i = 0
    while i < len(data):  # i is 5 < 5
        print(data[i])  # data[9], data[1], data[2]....data[4]
        i = i + 1  # i => 5
    print("----")

    # Q: find the maximum of the list "nums", use "while"
    nums = [3, 1, 5, 4, 2]
    i = 0
    max_value = nums[0]
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]
        i = i + 1
    print(max_value)

    return


def basic_for_loop():
    a = [3, 1, 5, 4, 2]
    #     0  1  2  3  4 <== len(a)-1

    # Q: print out the elements one by one in a
    for x in a:
        print(x)

    # Q: print out the elements one by one in a
    for i in [0, 1, 2, 3, 4]:
        print(a[i])
    print("------------")
    a = [3, 1, 5, 4, 2]
    #   0  1  2  3  4
    # Q: Reset all elements to -1
    # a = [-1, -1, -1, -1, -1]
    for i in [0, 1, 2, 3, 4]:
        a[i] = -1
    print(a)

    # Q: Give a list a, find the maximum value.
    a = [5, 1, 4, 2, 7, 5]
    # NOTE : size of a is fixed number 6
    max_value = a[0]
    for x in a:
        if max_value < x:
            max_value = x
    print(max_value)

    # Q: sum up all eleemnts in a, and print out the sum value
    a = [-1, 3, 0, 2, 5]
    sum = 0
    for x in a:
        sum = sum + x
    print(sum)

    sum = 0
    for i in range(0, len(a), 1):
        sum = sum + a[i]
    print(sum)

    # Q: Give a list a, find the minimum value.
    a = [-1, 3, 0, 2, 5]
    min_value = a[0]
    for x in a:
        if x < min_value:
            min_value = x
    print(min_value)

    # Q: Give a list a, find the minimum value., use index to access the list
    a = [-1, 3, 0, 2, 5]

    min_value = a[0]
    for i in [0, 1, 2, 3, 4]:
        if a[i] < min_value:
            min_value = a[i]
    print(min_value)


def basic_range_usage():
    """
    [3, 4, 5, 6, 7]  <== range( 3 , 8 , 1 )
    [4, 5, 6, 7] <== range( 4, 8, 1)
    [0, 1, 2, 3, 4]  <== range( 0, 5, 1)

    range( starting integer boundary , ending integer boundary  , step )
           ^^^^^^^^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^
              inclusive                     exclusive
    range( starting integer boundary , ending integer boundary)
     = range( starting integer boundary , ending integer boundary  , 1)

    range( ending integer boundary)
     = range( 0 , ending integer boundary  , 1)



    """
    tmp = [3, 1]
    a = list(tmp)  # [] <=== deep copy
    print(a)

    #!Q: [3, 4, 5, 6, 7]
    res = range(3, 8, 1)
    print(res)
    res = list(res)
    print(res)

    # Q: [6, 7, 8]
    res = range(6, 9, 1)
    res = range(6, 9)
    print(list(res))

    # Q: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = range(0, 10, 1)
    print(list(res))

    # Q: [2, 4, 6, 8, 10]
    res = range(2, 11, 2)
    print(list(res))

    # Q: [7, 6, 5, 4, 3]
    res = range(7, 2, -1)
    print(list(res))

    # Q: [5, 4, 3, 2, 1, 0]
    res = range(5, -1, -1)
    print(list(res))

    # Q: Give a, print out the "list of indexes"
    a = [3, 1, 5, 4, 2, 9, 8]
    #    0  1  2  3  4  5  6
    # => [0, ..........., len(a)-1]
    res = range(0, len(a), 1)  # range(len(a))
    print(list(res))

    return


def leetcode_merge_two_sorted_lists():
    print("------- v0 ---------")
    # Q: Given two sorted lists a and b, merge these two lists to c which is also sorted
    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # HW0323
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c += [a[i]]
            i = i + 1
        else:
            c += [b[j]]
            j = j + 1
    while i < len(a):
        c += [a[i]]
        i = i + 1
    while j < len(b):
        c += [b[j]]
        j = j + 1
    print(c)
    # b[0]<a[0]-->b[0]   []
    # b[1]<a[0]-->b[1]
    # a[0]<b[2]-->a[0]
    # a[1]<b[2]-->a[1]
    # b[2]<a[2]-->b[2]
    # a[3]<b[3]-->a[3]
    #
    print("------- v1 ---------")
    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        # ..
        if i < len(a) and j < len(b):  # 兩個都有
            if a[i] < b[j]:
                c += [a[i]]
                i = i + 1
            else:
                c += [b[j]]
                j = j + 1
        else:  # 其中一個沒有
            if j == len(b):  # explicit
                c += [a[i]]
                i = i + 1
            else:
                c += [b[j]]
                j = j + 1
    print(c)

    print("------- v2 ---------")
    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        # ..
        if (i < len(a) and j < len(b) and a[i] < b[j]) or j == len(b):
            c += [a[i]]
            i = i + 1
        else:
            c += [b[j]]
            j = j + 1
    print(c)
    print("------- v3 ---------")
    '''
    NOTE : Don't use "counter"
    NOTE : only use .pop(index), append(element)
    
    '''
    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #HW0326    




def leetcode_shuffle_two_lists():
    """

    a = a+ [-1] #拆掉重蓋
    a += [-1] #加蓋

    len(a) <== length of list a
    len(a) == 0 <== a is an empty list

    """

    # Q: Given two lists, a and b, please shuffle a and b to c, following index order
    # NOTE: len(a) and len(b) are the same
    a = [3, 5, 1, 4]
    b = [9, 6, 1, 0]
    # => c=[3, 9, 5, 6, 1, 1, 4, 0]
    c = []
    for i in range(0, len(a), 1):  # [0, 1, 2....., len(a)-1]
        c += [a[i]]
        c += [b[i]]

    print(c)
    # HW0318

    print("------- v 0.1 ----- while--")
    a = [3, 5, 1, 4]
    b = [9, 6, 1, 0]
    # => c=[3, 9, 5, 6, 1, 1, 4, 0]
    c = []

    i = 0
    while i < len(a):
        c += [a[i]]
        c += [b[i]]
        i = i + 1
    print(c)

    print("------- v1 ---------")
    # Q: Given two lists, a and b, please shuffle a and b to c, following index order
    # NOTE: len(a) and len(b) may not be the same.
    a = [3, 5, 1, 4]
    b = [9, 6, 1, 0, 8, -1]
    c = []
    # => c=[3, 9, 5, 6, 1, 1, 4, 0, 8, -1]
    d = max(len(a), len(b))
    e = min(len(a), len(b))
    i = 0
    # deal with shared index(es)
    # time complexity: O(N)
    while i < e:
        c += [a[i]]
        c += [b[i]]
        i = i + 1

    # deal with the remaining numbers in longer one

    # while first -> if-else
    # while i<d:
    #     if len(a)>len(b):
    #         c+=[a[i]]
    #     else: # <= condition
    #         c+=[b[i]]
    #     i=i+1

    # if-else -> while <== better performance
    if len(a) > len(b):
        while i < len(a):
            c += [a[i]]
            i += 1
    else:
        while i < len(b):
            c += [b[i]]
            i += 1

    print(c)

    print("------- v1.1 ---------")
    """
    True or True => True
    True or False => True
    False or True => True
    False or False => False

    True and True => True
    True and False => False
    False and True => False
    False and False => False    
    """
    a = [3, 5, 1, 4]
    b = [9, 6, 1, 0, 8, -1]
    c = []

    i = 0  # for counting a
    j = 0  # for counting b
    # or , and
    # time complexity : O(N)
    while i < len(a) or j < len(b):
        if i < len(a):
            # take a
            c += [a[i]]
            i += 1

        if j < len(b):
            # take b
            c += [b[j]]
            j += 1

    print(c)

    print("------- v2 ---------")
    # .. list..

    print("------- v3 ---------")
    # .. list : complexity

    return


def basic_list_i():
    # ------ combine ------
    # Q: Give two lists a and b, combine a and b to c
    a = [3, 1]
    b = [5, 6, 7]
    c = a + b  # <== + combine
    print(c)

    # ------ append ------
    # Q: append x to a => [3, 1, -1]
    a = [3, 1]
    x = -1

    a = a + [x]
    a += [x]

    # ---- basic characteristics -----
    a = [7, 6]  # < a is the memory address
    #   ^  ^  <== two memory "blocks"

    a = [3, 5, 1, 4, 2]
    #    0  1  2  3   4
    #    -5 -4  -3 -2 -1
    #                 -6 <== (X)

    # Q: print out the length of a
    print(len(a))

    # Q: print out the last element in a
    print(a[-1])

    print("------- append meaning ----")
    # Q: append x to a => [3, 1, -1]
    a = [3, 1]  # a[0]= 0, a[1]= 1 <== mutable
    x = -1
    a = a + [x]  # 拆掉重蓋
    print(a)

    a = [3, 1]
    x = -1
    a += [x]  # 加蓋
    print(a)

    print("-------- immutable variable: int, floating, string--")
    a = 5
    a = a + 1

    a += 1

    return


def leetcode_find_max():
    # Q: find the maximum value in a given list "a"
    a = [3, 6, -1, 7, 5, 4]
    max_value = a[0]  # in-function global variable
    for x in a:
        if x > max_value:
            max_value = x
    print(max_value)

    print("------ in-place memory usage ------")
    """
    No additional global memory is required during the operation/execution
    """
    # time complexity : O(N)
    a = [3, 6, -1, 7, 5, 4]
    for x in a:
        if x > a[0]:
            a[0] = x
    print(a[0])
    print("result = %s" % str(a))  # <== rookie please use this expression
    # print("result = %s" % a ) #<== python assume the variable is string type

    print("------ bubble shifting ------")
    a = [3, 6, -1, 7, 5, 4]
    """
         0  1  2   3  4  5
    a = [3, 6, -1, 7, 5, 4]
         ^^^^^ index-0 vs index-1, compare, X
            ^^^^^^ index-1 vs index-2, compare, swap
         3  -1  6  7  5  4
                ^^^^ index-2 vs index-3, compare, X
                   ^^^^^ index-3 vs index-4, compare, swap
         3  -1  6  5  7  4
                      ^^^^^ index-4 vs index-5, compare, swap
         3  -1  6  5  4  7 <== max

    N = len(a)
    k = [0, ..., N-2] # k is the left index of each pair (comparison)    

    for k in range(0 , N-1, 1): #[0, ... N-2]
    
    """
    # time complexity : O(N)
    N = len(a)
    for k in range(0, N - 1, 1):
        if a[k] > a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]
            # swap
    print(a[-1])
    print(a)


def leetcode_bubble_sort():
    a = [3, 6, -1, 7, 5, 4]
    N = len(a)
    """
    3, 6, -1, 7, 5, 4
    ^^^^^^^^^^^^^^^^^ N
    3, -1, 6, 5, 4, 7
    ^^^^^^^^^^^^^^^ N-1
    -1  3  5  4  6  7
    ^^^^^^^^^^^ N-2
    ...

    ^^^^^ 2

    for n     [N, N-1, N-2.....2]:
       for k     [0, .....n-2]
          k...
    #HW0325    
    """
    # time complexity : O(N^2) => optimal sorting algorithm O(N logN) => .sort()
    for n in range(N, 1, -1):  # N
        for k in range(0, n - 1, 1):  # N
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                # swap
    print(a)

    return


def basic_list_ii():

    print("------ append ---------")
    # Q: Given a list "a", append -1
    a = [3, 5]
    # a => [3, 5, 1]
    a = a + [-1] #拆掉重蓋
    print(a)

    a = [3, 5]
    # a => [3, 5, 1]
    a += [-1] #加蓋
    print(a)

    print("------ .append(element) ----")
    a = [3, 5]
    a.append(-1) #加蓋
    print(a)

    print("------ .pop(index) , return the pop-out element ----")
    a = [3, 5, 1, 4, 2]
    #Q: erase index-2 element from a
    # => a = [3, 5, 4, 2]
    k = 2
    x = a.pop(k)
    print(x)
    print(a)

    print("------ .pop() : equivalent to pop out the last element ----")

    a = [3, 5, 1, 4, 2]
    #Q: erase last element from a
    a.pop(-1)
    x = a.pop()
    print(a)
    

    print("------ .insert(index, element) :  ----")
    #TBV HW0326

    
    return


def leetcode_numbers_histogram():
    # Q: Given a list "nums", find the histogram of the numbers.
    #   NOTE: the number value will range at 0<= value <= 9
    nums = [6, 1, 0, 1, 2, 7, 6]
    # print out the results in the following format in ascending order
    """
    0 : 1
    1 : 2
    2 : 1
    6 : 2
    7 : 1
    
    """
    # HW0326 : 2-step approach

    # Step 0 : gather statistics
    # Step 1 : analyze raw data | statistics

    return


def basic_swap():
    # swap- generic swap
    a = 5
    b = 3
    # Q: swap the values in a and b
    c = a
    a = b
    b = c

    print("unpack")
    # Q: Give a list [5, 3]. Assign the index-0 and index-1 to x and y, respectively
    a = [5, 3]
    x = a[0]
    y = a[1]

    x, y = a  # <== unpack

    # multi-variable assignment
    # Q: Give the value of a b c to x y z
    a = 5
    b = 3
    c = 6

    x = a
    y = b
    z = c

    x, y, z = a, b, c

    # swap- python specific
    a = 5
    b = 3
    # Q: swap the values in a and b
    a, b = b, a

    return


def basic_print_usage():
    # ---- integer %d-----
    # Q: print out the message "a is 3"
    #                               ^ a
    a = 2
    print("a is %d" % a)

    # Q: print out the messsage "x is 5, y is 3"
    #                                ^       ^
    #                                x       y
    x = 5
    y = 3

    print("x is %d, y is %d" % (x, y))

    # ---- string %s------
    # Q: print out the message , "my friend is John"
    #                                         ^^^^ name
    name = "John"  # <== string

    print("my friend is %s" % name)

    # Q: print out the message, "John's score is 90"
    #                           ^^^^            ^^
    #                          name             score
    score = 90
    print("%s's score is %d" % (name, score))

    # ---- floating point %f (default 6 floating points)------

    # Q: print out the message, "pi is 3.1415926"
    #                                 ^^^^^^^^^ pi
    pi = 3.1415926
    # 7 floating

    print("pi is %.7f " % pi)

    print("pi is %.3f " % pi)

    # ---- str() -------
    z = 12
    x = str(z)  # "12"
    print(x)

    a = [3, 1, 5, 4, 2]
    # Q: print out the message "my list is [3, 1, 5, 4, 2]"
    tmp = str(a)  # "[3, 1, 5, 4, 2]"
    print("my list is %s" % tmp)

    newStr = "my list is %s" % str(a)
    newStr = "my list is %s" % a
    print(newStr)

    print("pi is %s" % str(pi))

    return
