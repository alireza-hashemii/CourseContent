# Subclassing built-ins Is Tricky

class DoppleDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppleDict(one=1)
print(dd)
dd['two'] = 2
print(dd)

dd.update(three=3)
print(dd)

# This built-in behavior is a violation of a basic rule of object-oriented programming:
# the search for methods should always start from the class of the receiver (self), even
# when the call happens inside a method implemented in a superclass. This is what is
# called “late binding,

# Subclassing built-in types like dict or list or str directly is error-
# prone because the built-in methods mostly ignore user-defined
# overrides. Instead of subclassing the built-ins, derive your classes
# from the collections module using UserDict, UserList, and
# UserString, which are designed to be easily extended.