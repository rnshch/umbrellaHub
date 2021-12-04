from Chapters.ch2.add_numbers import add, is_even, is_positive, convert_to_number


def test_convert_string_to_number():
    number = convert_to_number('5')
    assert number == 5

def test_4_is_even():
    assert is_even(4)


def test_5_is_odd():
    assert is_even(5) is False


def test_adding_even_numbers_return_even_number():
    number = add(2, 2)
    assert number == 4


def test_adding_zero_to_a_number():
    number = add(0, 2)
    assert number == 2


def test_1_is_positive():
    assert is_positive(1)


def test__1__is_negative():
    assert is_positive(-1) is False


def test_add_string_to_number():
    output = add('carlos', 2)
    assert output == 'Error: invalid input number'
