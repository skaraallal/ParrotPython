
print("***************************************")
print("** ")
print("** Premier Programme de Sofène")
print("** ")
print("***************************************")


def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("")
    print("Example:")
    print("-------")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    print("----------------------------")
    print("Tests unitaires: BEGIN ")
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    assert mult_two(4, 2) == 8
    assert mult_two(10, 2) == 18
    assert mult_two(10, 2) == 20
    print("Tests unitaires: END ")
    print("----------------------------")
