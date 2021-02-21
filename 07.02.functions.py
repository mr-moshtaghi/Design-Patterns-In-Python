"""
    1. functions are objects
    2. functions can be stored in data structure
    3. functions can be passed to other functions (higher-order function)
    4. functions can be nested (inner and outer functions)
    5. functions can capture local state (lexical closure)
    6. objects can behave like functions
"""


################# 1. functions are objects ###############
def show1(name):
    return f'hello {name}'


print("1. functions are objects")
print(show1('sajjad'))

x = show1
del show1
print(x('amir'))


# print(show1('hossien'))


##########################################################

##### 2. functions can be stored in data structure #######

def show2(name):
    return f'Hello {name.upper()}'


x = [show2, str.capitalize, str.lower]

print("2. functions can be stored in data structure")

print(x)
for i in x:
    print(i('SaJJAd mOsHTAghi'))


###########################################################

###### 3. functions can be passed to other functions ######

def show3(name):
    return f'Hello {name.upper()}'


def shoot(func):
    return func("AmIr")


print("3. functions can be passed to other functions")
print(shoot(show3))

for i in map(show3, ["sajjad", 'aMir', 'MoshTaghi']):
    print(i)


##########################################################

##4. functions can be nested (inner and outer functions)##

def show4():
    def shoot4():
        return 'Hello'

    return shoot4()


print("4. functions can be nested (inner and outer functions)")
print(show4())


# -----------------------


def Show4(name):
    def Shoot4(n):
        return f'Hello {n}....'

    return Shoot4(name)


print(Show4("amir"))


# -----------------------


def person(age):
    def adult(name):
        return f'{name} is Adult.'

    def kid(name):
        return f'{name} is Kid.'

    if age > 18:
        return adult
    else:
        return kid


x = person(10)
print(x)
print(x('sajjad'))


############################################################

## 5. functions can capture local state (lexical closure) ##


def person5(age, name):
    def adult5():
        return f'{name} is Adult.'

    def kid5():
        return f'{name} is Kid.'

    if age > 18:
        return adult5
    else:
        return kid5


print("5. functions can capture local state (lexical closure)")
print(person5(24, 'amir'))
print(person5(24, 'amir')())


###############################################################

######### 6. objects can behave like functions ##########

class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(f'{self.name} is {self.age} years old.')


print("6. objects can behave like functions")
p = Person(24, 'sajjad')
print(p)
p()
