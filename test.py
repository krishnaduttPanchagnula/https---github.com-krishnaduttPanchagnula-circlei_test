import calc

def test():
    assert calc.add(10, 5) == 15
    print ( 'Add ran perfectly')

    assert calc.divide(10, -1) == -10
    print ("divide ran sucessfully")

    assert calc.subtract(10, -1) == 11
    print ("subtract ran sucessfully")

    assert calc.multiply(5, -1) == -5
    print ("multiply ran sucessfully")


if __name__ == '__main__':
    test()