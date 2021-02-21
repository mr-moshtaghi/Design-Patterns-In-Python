"""
    python decorators:
        1. creating decorators
        2. applying multiple decorators to a single functions
        3. accepting arguments in decorator functions
        4. defining general purpose decorators
        5. passing arguments to the decorators
        6. debugging decorators
"""


########### 1. creating decorators #############

def outer_upper(func):
    def inner_upper():
        f = func()
        text = f.upper()
        return text

    return inner_upper


@outer_upper
def show():
    return 'hello world...'


print("1. creating decorators")
print(show())


#################################################

# 2. applying multiple decorators to a single functions #

def outer_upper1(func):
    def inner_upper1():
        f = func()
        text = f.upper()
        return text

    return inner_upper1


def outer_split(func):
    def inner_split():
        f = func()
        text = f.split(' ')
        return text

    return inner_split


@outer_split
@outer_upper1
def show1():
    return 'hello world...'


print("2. applying multiple decorators to a single functions")
print(str.split("hello world", ' '))
print(show1())


########################################################

##### 3. accepting arguments in decorator functions ####

def outer_upper3(func):
    def inner_upper3(t):
        f = func(t)
        text = f.upper()
        return text

    return inner_upper3


@outer_upper3
def show3(text):
    return text


print("3. accepting arguments in decorator functions")
print(show3('how are you...'))


######################################################

##### 4. defining general purpose decorators #####

def outer_upper4(func):
    def inner_upper4(t, *args, **kwargs):
        f = func(t)
        print(args)
        print(kwargs)
        text = f.upper()
        return text

    return inner_upper4


@outer_upper4
def show4(text):
    return text


print("4. defining general purpose decorators")
print(show4('how are you...', 'amir', age=20))


########################################################

##### 5. passing arguments to the decorators #######

def outer_deco(v1, v2):
    def outer_upper5(func):
        def inner_upper5(t):
            f = func(t)
            print(v1, v2)
            text = f.upper()
            return text

        return inner_upper5

    return outer_upper5


@outer_deco('amir', 20)
def show5(text):
    return text


print("5. passing arguments to the decorators")
print(show5('how are you...'))


####################################################

########## 6. debugging decorators ##########

import functools

def outer_deco6(v1, v2):
    def outer_upper6(func):
        @functools.wraps(func)
        def inner_upper6(t):
            'inner_upper6 function'
            f = func(t)
            print(v1, v2)
            text = f.upper()
            return text

        return inner_upper6

    return outer_upper6


@outer_deco6('amir', 20)
def show6(text):
    'show6 functions'
    return text


print("6. debugging decorators")
print(show6('how are you...'))
print(show6.__doc__)
print(show6.__name__)

def outer_deco7(v1, v2):
    def outer_upper7(func):
        def inner_upper7(t):
            'inner_upper6 function'
            f = func(t)
            print(v1, v2)
            text = f.upper()
            return text

        return inner_upper7

    return outer_upper7


@outer_deco7('amir', 20)
def show7(text):
    'show6 functions'
    return text


print(show7('...'))
print(show7.__doc__)
print(show7.__name__)
