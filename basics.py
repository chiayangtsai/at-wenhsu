"""

- head index : always moving
- tail index : conditionally moving triggered by new head data
"""


def leetcode_stock_trade_iii():
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

    Example 2:

    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
    Example 3:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

    Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
    """

    """
    f({a, b, c, d}) =max{  f({a})          +   f({b, c, d}),
                           f({a, b})       +   f({c, d}),
                           f({a, b, c})    +   f({d}),
                           f({a, b, c, d})     f({}) 
                         }
    ==> at least O(N^2)
    ==> optimal O(N)
    """

    def deriveProfit(prices):
        t =0
        maxP = 0
        for h in range(1, len(prices), 1):
            if prices[h] >= prices[t]:
                profit = prices[h] - prices[t]
                if profit > maxP:
                    maxP = profit
            else:
                t = h
        return maxP

    def maxProfit(prices):
        # time complexity : O(N^2) -> O(N) ?

        n = len(prices)
        maxP = 0
        for k in range(n + 1):
            profit = deriveProfit(prices[:k]) + deriveProfit(prices[k:])
            if profit > maxP:
                maxP = profit
        # HW0401
        return maxP  # TBD

    prices = [1, 3, 5, 4, 3, 7, 6, 9, 2, 4]
    print("max profit : %d (ans 10)\n\n" % maxProfit(prices))

    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print("max profit : %d (ans 13)\n\n" % maxProfit(prices))

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfit(prices))

    prices = [1, 2, 3, 4, 5]
    print("max profit : %d (ans 4)\n\n" % maxProfit(prices))

    prices = [7, 6, 4, 3, 1]
    print("max profit : %d (ans 0)\n\n" % maxProfit(prices))

    print("-------- v1 : O(N) ------------")
    '''
    f({a, b, c, d}) =max{  
                           f({})           + f({a,b, c, d})
                           f({a})          +   f({b, c, d}),
                           f({a, b})       +      f({c, d}),
                           f({a, b, c})    +         f({d}),
                           f({a, b, c, d})            f ({}) 
                         }

    # step 1: get f(a, b, c, d), f(a, b, c), f(a, b), f(a) (L->R)
    # save to tableLR

    # Step 2: get R->L
    # save to tableRL

    #Step 3: for loop to loop all combinations
    
    '''

    def maxProfitAlt(prices):
        #HW0406 : use two LUTs to save time complexity.
        return -1

    prices = [1, 3, 5, 4, 3, 7, 6, 9, 2, 4]
    print("max profit : %d (ans 10)\n\n" % maxProfitAlt(prices))

    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print("max profit : %d (ans 13)\n\n" % maxProfitAlt(prices))

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfitAlt(prices))

    prices = [1, 2, 3, 4, 5]
    print("max profit : %d (ans 4)\n\n" % maxProfitAlt(prices))

    prices = [7, 6, 4, 3, 1]
    print("max profit : %d (ans 0)\n\n" % maxProfitAlt(prices))


def leetcode_stock_trade_i():
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description


    You are given an array prices where prices[i] is the price of a given stock on
    the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and
    choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot
    achieve any profit, return 0.



    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
    6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because
    you must buy before you sell. Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.


    Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
    """
    # target : O(N), at least O(N^2)

    print("----- v0 --- O(N^2)---")

    # time complexity : O(N^2)
    # space complexity : O
    def maxProfit(prices):
        # HW0329
        # prices = [7, 1, 5, 3, 6, 4]
        N = len(prices)
        profits = []
        for k in range(0, N - 1, 1):
            for j in range(k + 1, N, 1):
                profits.append(prices[j] - prices[k])

        maxP = max(profits)

        return 0 if maxP < 0 else maxP

        # if maxP<0:
        #     return 0
        # else:
        #     return maxP

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfit(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfit(prices))

    prices = [4, 5, 4, 3, 7, 6, 9, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfit(prices))

    print("----- v1 --- O(N)---")

    # O(N)
    def maxProfitAlt(prices):
        # HW0329
        # prices = [7, 1, 5, 3, 6, 4]
        N = len(prices)

        min_price = prices[0]
        maxP = 0
        for i in range(1, N, 1):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > maxP:
                maxP = prices[i] - min_price
        return maxP

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitAlt(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitAlt(prices))

    prices = [4, 5, 4, 3, 7, 6, 9, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfitAlt(prices))

    print("----- v2 --- O(N)---")
    """   
             0  1  2  3  4  5  6  7  8
             4  5  4  3  7  6  9  1  4
                         h
                      t
     profit  0  1  0     4
     maxP    0  1  1  1  4
    
    """

    # O(N)
    def maxProfitLR(prices):
        maxP = 0
        t = 0
        for h in range(1, len(prices), 1):
            if prices[h] >= prices[t]:
                profit = prices[h] - prices[t]
                if profit > maxP:
                    maxP = profit
            else:
                t = h
        return maxP

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitLR(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitLR(prices))

    prices = [4, 5, 4, 3, 7, 6, 9, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfitLR(prices))

    print("----- v3 --- O(N)---")
    """   
             0  1  2  3  4  5  6  7  8  (index)
             4  5  4  3  7  6  9  1  4  
             h (買)                       
                               t
     profit  5  4  5  6  2  3     3  0
     maxP    6  6  6  6  3  3     3  0
    
    """

    # O(N)
    def maxProfitRL(prices):
        maxP = 0
        t = len(prices) - 1
        for h in range(len(prices) - 1, -1, -1):
            if prices[h] <= prices[t]:
                profit = prices[t] - prices[h]
                if profit > maxP:
                    maxP = profit
            else:
                t = h

        # HW0330

        return maxP

    prices = [7, 1, 5, 3, 6, 4]
    print("max profit : %d (ans 5)\n" % maxProfitRL(prices))

    prices = [7, 6, 4, 3, 0]
    print("max profit : %d (ans 0)\n" % maxProfitRL(prices))

    prices = [4, 5, 4, 3, 7, 6, 9, 1, 4]
    print("max profit : %d (ans 6)\n\n" % maxProfitRL(prices))


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
    """
    NOTE : Don't use "counter"
    NOTE : only use .pop(index), append(element)
    
    """
    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # HW0326

    while len(a) != 0 or len(b) != 0:
        if (len(a) != 0 and len(b) != 0 and a[0] < b[0]) or len(b) == 0:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    print(c)

    print("------- v4 -  ---------")

    """
    x = [3, 1, 5, 4, 2]
    #Q: if x is not empty, print "not empty"
    if x:
        print("not empty")

    y = [3, 1, 4]
    #Q: if y is empty, print "empty"
    if not y:
        print("empty")
    """

    a = [2, 3, 5, 6]
    b = [0, 1, 4, 7, 8]
    c = []
    # c=> [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while a or b:
        if (a and b and a[0] < b[0]) or not b:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    print(c)


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
    a = a + [-1]  # 拆掉重蓋
    print(a)

    a = [3, 5]
    # a => [3, 5, 1]
    a += [-1]  # 加蓋
    print(a)

    print("------ .append(element) ----")
    a = [3, 5]
    a.append(-1)  # 加蓋
    print(a)

    print("------ .pop(index) , return the pop-out element ----")
    a = [3, 5, 1, 4, 2]
    # Q: erase index-2 element from a
    # => a = [3, 5, 4, 2]
    k = 2
    x = a.pop(k)
    print(x)
    print(a)

    print("------ .pop() : equivalent to pop out the last element ----")

    a = [3, 5, 1, 4, 2]
    # Q: erase last element from a
    a.pop(-1)
    x = a.pop()
    print(a)

    print("---- del a[index] ----")
    a = [3, 5, 1, 4, 2]
    # Q: erase index-2 element from a
    del a[2]
    print(a)

    print("------ .insert(index, element) :  ----")
    a = [3, 5, 1, 4, 2]
    # Q : insert -1 to index-2 position [3, 5, -1, 1, 4, 2]
    a.insert(2, -1)
    print(a)

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

    """
    KES algorithm : use the data range index to establish look-up table (LUT)

    number <-> show times

    number <-> list index <-> show time
               ^^^^^^^^^^^^^^^^^^^^^^^^ list
        
    """

    # time complexity : O(N)

    # HW0326 : 2-step approach
    c = [0] * 10

    # Step 0 : gather statistics
    for x in nums:  # O(N)
        c[x] += 1

    # Step 1 : analyze raw data | statistics
    for i in range(0, 10, 1):  # O(1)
        if c[i] > 0:
            print(i, ":", c[i])
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


def basic_copy_concept():
    print("------- deep copy ------")
    a = 5  # immutable variable
    b = a
    print("a= %d, b= %d" % (a, b))
    b = -1
    print("a= %d, b= %d" % (a, b))

    print("------- shallow copy ------")
    a = [7, 5]  # mutable variable
    b = a
    print("a= %s, b= %s" % (a, b))
    b[0] = -1
    print("a= %s, b= %s" % (a, b))

    """
    immutable: integer, floating point, string, tuple (TBV)
        copy : deep copy

    mutable: list, dict (TBV)
        copy : shallow copy
    
    """
    name = "John"
    print(name[0])
    print(name[1])
    # name.append("y") <==X "string" is immutable
    name = name + "y"

    print("------- list: deep copy ------")
    a = [7, 5]  # mutable variable

    # -method 0 --
    b = []
    for x in a:
        b.append(x)
        # b += [x]
        # b = b+ [x]
    # -method 0.1 --
    b = [x for x in a]
    # -method 1 --
    b = list(a)  # <== RECOMMENDED

    # --method 2 ---
    b = a[:]  # <== RECOMMENDED

    print("a= %s, b= %s" % (a, b))
    b[0] = -1
    print("a= %s, b= %s" % (a, b))

    print("---- simplifed unpack -----")
    # Q: Given a list "nums", pick up all the negative numbers and assign a new list "nums"
    nums = [3, -1, -2, 0, 7, -3]
    # => nums = [-1, -2, -3]
    nums = [x for x in nums if x < 0]
    print(nums)

    return


def basic_list_iii():
    a = [3, 1, 5, 4, 2, 0, -2]
    #    0  1  2  3  4  5  6
    # Q: print out the index-2 element.
    print(a[2])

    # Q: print out the elements from index-2 to index-4, [5, 4, 2]
    print(a[2:5:1])

    # Q: print out the elements from index-1 to index-3
    print(a[1:4:1])

    """
        a [ starting index boundary :  ending index boundary  : step   ]
            ^^^^^^^^^^^^^^^^^^^^^^^     ^^^^^^^^^^^^^^^^^^^^
               inclusive                 exclusive

        1) if reached boundary, leave it empty.
        2) if step is 1, ":1" can be ignored.

        index-2 to index-4
        a[2 : 5 :  1]
    
    
    """

    nums = [5, -1, 0, 2, 6, 3, 7, 9]
    #       0   1  2  3  4  5  6  7

    # Q: print out elements from index-2 to index-5
    print(nums[2:6:1])

    # Q: print out elements from index-4 to the end
    print(nums[4:])  # python compiler fixes the problem

    # Q: print out elements from index-0 to index-3
    print(nums[0:4])
    print(nums[:4])

    # Q: print out elements from index-5 to index-2 [3, 6, 2, 0]
    print(nums[5:1:-1])

    # Q: print out elements from index-5 to index-0 [3, 6, 2, 0, -1, 5]
    print(nums[5::-1])

    # Q: print out elements in reversed order [9, 7, 3, 6, 2, 0, -1, 5]
    print(nums[::-1])

    # Q: print out a deep-copy of nums [5, -1, 0, 2, 6, 3, 7, 9]
    print(nums[:])


def basic_call_by_reference():
    print("------ call by value --------")

    def my_sum(x, y):  # x = a, y = b
        c = x + y
        return c

    # Q: give a and b , calcualte the sum using function.
    a = 5  # immutable
    b = 3  # immutable
    c = my_sum(a, b)
    print(c)

    print("------ call by reference --------")

    def my_append_minus_one(x):  # x = a <== shallow copy
        x = x + [-1]  # 拆掉重蓋  (X) 
        #x += [-1]    #加蓋     (O)
        #x.append(-1) #加蓋     (O)
        print("x = %s" % x)

    # Q : give list "a", append -1 to a using function
    a = [3, 0] #<== mutable <== copy: shallow copy
    print("before : %s" % a)
    my_append_minus_one(a)
    print("after : %s" % a)  # [3, 0, -1]

    print("------ function call - full permission --------")
    print("------ function call - deep copy + full permission --------")
    print("------ function call - read only --------")
