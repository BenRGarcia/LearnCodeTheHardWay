i = 0
numbers = []
while_loop_limit = 6
x_incrementor = 2

def while_loop(x):
    while x < while_loop_limit:
        print ("At the top i is %d" % x)
        numbers.append(x)

        x += x_incrementor
        print ("Numbers now: ", numbers)
        print ("at the botton i is %d" % x)


        print ("The numbers: ", numbers)


while_loop(i)

for num in numbers:
    print (num)
