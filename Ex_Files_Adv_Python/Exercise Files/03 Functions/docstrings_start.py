# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """my function(arg1, arg2=None) --> do nothing

    parameters:
    arg1: the first argument
    arg2: secound argument
    """

    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
