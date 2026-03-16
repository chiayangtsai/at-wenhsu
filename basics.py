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
    a = [3, 1]
    x = -1
    a = a + [x] # 拆掉重蓋
    print(a)

    a = [3, 1]
    x = -1
    a += [x] #加蓋
    print(a)


    
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
