# . Integers are all the positive and negative
#  numbers on the number line, including zero, that have no fractional or decimal
#  part. Real numbers are all the numbers on the number line, including those
#  between the integers.
#  I need not belabor the point; we know how to write and manipulate decimal
#  numbers. Now, let’s take a step back and write what we mean by numbers in an
#  arbitrary base, B
#  …d3d2d1d0 = …+d3B3+d2B2+d1B1+d0B0
#  where d
# ∊
#  [0, B – 1]. The symbol
# ∊
#  means that d is an element from the following
#  set. If B = 8, then d is a number in [0,7] = {0,1,2,3,4,5,6,7}
from django.utils.termcolors import foreground


def dec2base(d, b):
    def digit(r):
        return chr(48 + r if (r < 10) else 55 + r)

    r = d % b
    d = d // b
    m = digit(r)
    while d != 0:
        r = d % b
        d = d // b
        m += digit(r)
    return m[::-1]


#
# print(dec2base(6563, 16))


def add_100_time():
    sum = 0.1
    for i in range(100):
        sum += 0.1
    return sum


print(add_100_time())
