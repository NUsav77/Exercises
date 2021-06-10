import unit_test

def test_add():
    assert unit_test.add(7, 3) == 10
    assert unit_test.add(7) == 9

def test_product():
    assert unit_test.product(5, 5) == 25
    assert unit_test.product(5) == 10