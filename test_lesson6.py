import lesson_5_module

def test_one():
    assert lesson_5_module.one(17)

def test_two():
    assert lesson_5_module.two(21) == [1,3,7,21]

def test_three():
    assert lesson_5_module.three(15) == 5

def test_four():
    assert lesson_5_module.four(28) == [2,2,7]

def test_five():
    assert lesson_5_module.five(28) == 14