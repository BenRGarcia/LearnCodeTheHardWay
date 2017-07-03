"""Python Symbol Review"""

# Declare arbitrary variables to show use of various Python symbols
arbitrary_list = ['dog', 'cat', 'snake', 'zebra', 'hippo', 'giraffe', 'catfish']
number_list = [2, 4, 6]
car = "Honda Civic"
single_number_list = [31415.92653000]

def math_hard():
    for number in number_list:
        if number >= 6:
            print ("This number is greater than or = 6: ", number)
        elif number >= 4:
            print ("This number is greater than or = 4: ", number)
        else:
            print ("This number is less than 4: ", number)
    for i in single_number_list:
        print ("Original number: ", single_number_list)
        print ("Decimal integer '%%d': %d" % i)
        print ("Unsigned decimal '%%u': %u" % i)
        print ("Exponential notation, lowercase 'e' '%%e': %e" % i)
        print ("Exponential notation, uppercase 'E' '%%E': %E" % i)
        print ("Floating point real number '%%f': %f" % i)
        print ("Either %%f or %%e, whichever is shorter ''%%g': %g" % i)
        print ("Same as %%g, but uppercase '%%G': %G" % i)
        print ("Repr format (debugging format) '%%r': %r" % i)
        print ("String format '%%s': %s" % i)
        print ("Percent sign '<escape character>%%': %g%%" % i)
    for i in single_number_list:
        integer_number = int(single_number_list[0] // 1)
        print ("Octal number '%%o': %o" % integer_number)
        print ("Hexadecimal lowercase '%%x': %x" % integer_number)
        print ("Hexadecimal uppercase '%%X': %X" % integer_number)
        print ("Character format '%%c': %c" % integer_number)

math_hard()


def true_or_false():
    print ("Is this true or false? 'True and False'", True and False)
    print ("Is this true or false? '40 is 'the new 30''", 40 is 'the new 30')
    print ("Is this true or false? 'not True == True or False'", not True == True or False)

true_or_false()


def unknown_unused():
    print ("""
    Here is a list of symbols I haven't yet used:
    assert
    break
    class
    continue
    del
    except
    exec
    finally
    global
    from/import
    lambda
    pass
    raise
    return
    try
    while
    with
    yield
    """)
