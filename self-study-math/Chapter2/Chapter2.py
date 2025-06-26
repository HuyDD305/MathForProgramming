# Abstract algebra is a fundamental branch of mathematics, of which “normal”
#  arithmetic is but one instance. Abstract algebra uses sets, so you’ll put your newfound
#  set knowledge to work to understand one of the most widely used concepts in
#  abstract algebra: groups.
# A set is a collection of things. In math, sets are usually numbers or other sets. For
#  example
#  S ={1,2,5}
# The set
# ℕ
#  has a name: the natural numbers. Some ambiguity arises here as other
#  authors include 0 in the set of natural numbers. We’ll call the set that includes 0 the
#  whole numbers:
#  W={0,1,2,3,…}

from NumberSets import Quaternion

A = {1, 3, 4, 5, 7}
B = {0, 2, 4}
C = set()

x = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
y = list(set(x))
print(A | B)

c = 1 + 3j
print(c * c)
d = complex(-3.3, 0.4)

print(c * d)
c = Quaternion(1, 3, 0, 0)
d = Quaternion(-3.3, 0.4, 0, 0)
print(c)
print(d)
print(c * d)

print(c < d)
