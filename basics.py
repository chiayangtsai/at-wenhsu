def basic_for_loop():

    a =  [3, 1, 5, 4, 2]
    #     0  1  2  3  4 <== len(a)-1

    #Q: print out the elements one by one in a
    for x in a:
        print(x)

    #Q: print out the elements one by one in a
    for i in [0, 1, 2, 3, 4]:
        print(a[i])
    print("------------")
    a= [3, 1, 5, 4, 2]
    #   0  1  2  3  4 
    #Q: Reset all elements to -1
    # a = [-1, -1, -1, -1, -1]
    for i in [0,1,2,3,4]:
        a[i]=-1
    print(a)


    #Q: Give a list a, find the maximum value.
    a= [5, 1, 4, 2, 7, 5]
    #NOTE : size of a is fixed number 6
    max_value=a[0]
    for x in a:
        if max_value<x:
            max_value=x
    print(max_value)

    #Q: sum up all eleemnts in a, and print out the sum value
    a = [-1, 3, 0, 2, 5]
    sum=0
    for x in a:
        sum=sum+x
    print(sum)
        
    sum = 0
    for i in [0, 1, 2, 3, 4]:
        sum=sum+a[i]
    print(sum)

    #Q: Give a list a, find the minimum value.
    a = [-1, 3, 0, 2, 5]
    min_value=a[0]
    for x in a:
        if x< min_value:
            min_value=x  
    print(min_value)
    
    #Q: Give a list a, find the minimum value., use index to access the list
    a = [-1, 3, 0, 2, 5]
    
    min_value=a[0]
    for i in [0,1,2,3,4]:
        if a[i] < min_value:
            min_value=a[i]  
    print(min_value)
    
def basic_range_usage():
    '''
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


    
    '''
    tmp = [3, 1]
    a = list(tmp) # [] <=== deep copy
    print(a)
    
    #!Q: [3, 4, 5, 6, 7]
    res = range(3, 8, 1)
    print(res)
    res = list(res)
    print(res)

    #Q: [6, 7, 8]
    res = range(6,9,1)
    res = range(6,9)
    print(list(res))
    
    #Q: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = range(0,10,1)
    print(list(res))
    

    #Q: [2, 4, 6, 8, 10]
    res = range(2,11,2)
    print(list(res))


    #Q: [7, 6, 5, 4, 3]
    res = range( 7 , 2, -1 )
    print(list(res))



    #Q: [5, 4, 3, 2, 1, 0]
    res = range( 5 , -1, -1 )
    print(list(res))


    #Q: Give a, print out the "list of indexes"
    a = [3, 1, 5, 4, 2, 9, 8]
    #    0  1  2  3  4  5  6  
    # => [0, ..........., len(a)-1]
    res = range(  0 ,  len(a)  , 1  ) # range(len(a))
    print(list(res))


    
    return 


def leetcode_shuffle_two_lists():
    #Q: Given two lists, a and b, please shuffle a and b to c, following index order
    # NOTE: len(a) and len(b) are the same
    a= [3, 5, 1, 4]
    b= [9, 6, 1, 0]
    c= []
    # => c=[3, 9, 5, 6, 1, 1, 4, 0]

    #HW0318

    print("------- v1 ---------")
    #Q: Given two lists, a and b, please shuffle a and b to c, following index order
    a= [3, 5, 1, 4]
    b= [9, 6, 1, 0, 8, -1]
    c= []
    # => c=[3, 9, 5, 6, 1, 1, 4, 0, 8, -1]

    #HW0318 (bonus)
    
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
    a= [7, 6] #< a is the memory address
    #   ^  ^  <== two memory "blocks"

    a = [3, 5, 1, 4, 2]
    #    0  1  2  3   4
    #    -5 -4  -3 -2 -1
    #                 -6 <== (X)
    
    #Q: print out the length of a
    print( len(a) )

    #Q: print out the last element in a
    print(a[-1])



    print("------- append meaning ----")
    # Q: append x to a => [3, 1, -1]
    a = [3, 1] #a[0]= 0, a[1]= 1 <== mutable
    x = -1
    a = a + [x] # 拆掉重蓋
    print(a)

    a = [3, 1]
    x = -1
    a += [x] #加蓋
    print(a)


    print("-------- immutable variable: int, floating, string--")
    a = 5
    a = a +1

    a += 1
    
    return


def leetcode_find_max():
    # Q: find the maximum value in a given list "a"
    a = [3, 6, -1, 7, 5, 4]

    max_value = a[0]
    for x in a:
        if x > max_value:
            max_value = x
    print(max_value)

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
