# new immutable type
# it doesn't allow any changes to the object after it has been created
# hasable as long as its keys and values are hashable
from builtins import frozendict

a = frozendict(x=1, y=2)
print(a['x'])

try:
    a['z'] = 3
except TypeError as e:
    print(e)

b = frozendict(y=2, x=1)
print(hash(a) == hash(b))
print(a == b)