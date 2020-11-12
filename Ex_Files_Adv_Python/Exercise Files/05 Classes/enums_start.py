# define enumerations using the Enum base class

from enum import Enum, auto
class Fruit(Enum):
    APPLE = 2
    BANANA = 4
    ORANGE = 8
    TOMATO = 10
    PEAR = auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    # print(Fruit.APPLE)
    # print(type(Fruit.APPLE))
    # print(repr(Fruit.APPLE))

    # TODO: enums have name and value properties
    # print(Fruit.APPLE.name, Fruit.APPLE.value)

    # TODO: print the auto-generated value
    print(Fruit.PEAR.value)

    # TODO: enums are hashable - can be used as keys
    myFruit = {}
    myFruit[Fruit.BANANA] = "Come mr tally man"
    print(myFruit[Fruit.BANANA])


if __name__ == "__main__":
    main()
