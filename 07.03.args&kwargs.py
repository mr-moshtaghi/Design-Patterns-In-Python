"""
    *args  **kwargs
"""


def show(name, *args, **kwargs):
    print(args)
    print(kwargs)
    return f'Hello {name}'


print(show('amir', 'ali', 'hassan', age=23, height=157))


def show1(name, *amir, **big):
    print(amir)
    print(big)
    return f'Hello {name}'


print(show1('amir', 'ali', 'hassan', age=23, height=157))
