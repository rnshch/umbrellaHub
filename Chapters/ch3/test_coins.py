import pytest
from Chapters.ch3 import coins


def test_sum_pennies():
    total = coins.sum_pennies(user_input='50')
    assert total == 50


def test_sum_nickles():
    total = coins.sum_nickels(user_input='5')
    assert total == 25


def test_sum_dimes():
    total = coins.sum_dimes(user_input='3')
    assert total == 30


def test_sum_quarters():
    total = coins.sum_quarters(user_input='4')
    assert total == 100


def test_sum_all_coins():
    total = coins.sum_all_coins(pennies='1', quarters='1', dimes='1', nickels='1')
    assert total == 41


def test_win_the_exact_dollar():
    pytest.fail()


def test_loss_under():
    pytest.fail()


def test_loss_above():
    pytest.fail()
