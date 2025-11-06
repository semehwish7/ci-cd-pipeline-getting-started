from src.main import add,subtract

def test_add_function():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(1, 9) == 10

def test_subtract_function():
    assert subtract(6, 2) == 4
    assert subtract(0, 0) == 0
    assert subtract(10, 9) == 1