
#  pep 661
from builtins import sentinel

NOT_SET = sentinel("NOT_SET")

def config(key, default=NOT_SET):
    settings = {
        "timeout": None,
    }

    value = settings.get(key, NOT_SET)

    if value is NOT_SET:
        if default is NOT_SET:
            raise KeyError(key)
        return default

    return value

print(config("timeout"))
print(config("missing", 30))
# print(config("missing"))  # raises KeyError
print(NOT_SET)

from typing import assert_type

MISSING = sentinel('MISSING')

def foo(value: int | MISSING) -> None:
    if value is MISSING:
        assert_type(value, MISSING)
    else:
        assert_type(value, int)

    