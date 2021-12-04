def convert_to_number(string):
    return int(string)


def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return 'Error: invalid input number'
    else:
        return x + y


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


def challeng_1():
    input_1 = input("Entrer premier numero")
    input_2 = input("Entrer deuxième numero")
    num_1 = convert_to_number(input_1)
    num_2 = convert_to_number(input_2)
    total = add(num_1, num_2)
    print(total)


if __name__ == '__main__':
    challeng_1()
