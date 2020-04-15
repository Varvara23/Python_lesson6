import lesson_5_module
import dirty_func

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

def test_f():
    assert dirty_func.f(['Мотоцикл', 'Семена'], 1) == ['Семена']

def test_f_two():
    assert dirty_func.f_two(3) == 3