from decimal import Decimal
from math import modf

import statistics


def my_round(number, n_digits=0, string_convert=False):
    if isinstance(number, int) or isinstance(number, float) and isinstance(n_digits, int):
        n_digits = abs(n_digits)
        string_number_n_digits_add_1 = str(int(Decimal(number)*pow(10, n_digits + 1)))

        number_compare = int(string_number_n_digits_add_1[-1])
        int_number = int(string_number_n_digits_add_1[:len(string_number_n_digits_add_1) - 1]) + 1 if number_compare >= 5 else int(string_number_n_digits_add_1[:len(string_number_n_digits_add_1) - 1])
        result = float(int_number/pow(10, n_digits))
        print(string_number_n_digits_add_1, number_compare, int_number, result, modf(number))

        if string_convert:
            result = f"{result}{'0'* (n_digits - len(str(result)[str(result).find('.') + 1: len(str(result))]))}" if n_digits > 0 else f"{result:.1f}"
        return result
    else:
        if isinstance(number, int) is False or isinstance(number, float):
            raise ValueError(f"This is {number} Much Be Integer Or Float, Please Check Your Input !!!")
        if isinstance(n_digits, int) is False:
            raise ValueError(f"This is {n_digits} Much Be Integer, Please Check Your Input !!!")


a = my_round(1738.25, 2)
print(a)
