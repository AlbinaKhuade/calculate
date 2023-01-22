from logger import logging
from math_fun import summ, diff, multi, int_div, remain_div, exponent, square_root
from fractions import Fraction
import view


def menu():
    while True:
        type_num = int(input('Working with:\n'
                             '1 - rational\n'
                             '2 - complex\n'
                             '3 - exit\n'))
        if type_num == 1 or type_num == 2:
            return type_num
        elif type_num == 3:
            logging.info('Stop program')
            break
        else:
            logging.error('Error: wrong menu selection')
            menu()


def menu_calc(type_num):
    while True:
        if type_num == 1:
            op = int(input('Operations:\n'
                           '1 - sum +\n'
                           '2 - sub -\n'
                           '3 - mult *\n'
                           '4 - div /\n'
                           '5 - pow **\n'
                           '6 - sqrt\n'
                           '7 - %\n'
                           '0 - previous menu\n'))
                    
        elif type_num == 2:
            op = int(input('Operations:\n'
                           '1 - sum +\n'
                           '2 - sub -\n'
                           '3 - mult *\n'
                           '4 - div /\n'
                           '5 - pow **\n'
                           '6 - sqrt\n'
                           '0 - previous menu\n'))
        return op





# def menu_calc_rat(type_num):
#     while True:
#         type_num = int(input('Operations:\n'
#                              '1 - sum +\n'
#                              '2 - sub -\n'
#                              '3 - mult *\n'
#                              '4 - div /\n'
#                              '5 - %\n'
#                              '6 - pow **\n'
#                              '7 - sqrt\n'
#                              '0 - previous menu\n'))
#         if type_num == 1:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = summ(num1, num2)
#             print(result)
#             logging.info(f'{num1} + {num2} = {result}')
#         if type_num == 2:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = diff(num1, num2)
#             print(result)
#             logging.info(f'{num1} - {num2} = {result}')
#         if type_num == 3:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = multi(num1, num2)
#             print(result)
#             logging.info(f'{num1} * {num2} = {result}')
#         if type_num == 4:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = int_div(num1, num2)
#             print(result)
#             logging.info(f'{num1} / {num2} = {result}')
#         if type_num == 5:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = remain_div(num1, num2)
#             print(result)
#             logging.info(f'{num1} % {num2} = {result}')
#         if type_num == 6:
#             num1, num2 = Fraction(input("enter the first number: ")), Fraction(
#                 input('enter the second number: '))
#             result = exponent(num1, num2)
#             print(result)
#             logging.info(f'{num1} ** {num2} = {result}')
#         if type_num == 7:
#             num1 = Fraction(input("enter the number: "))
#             result = square_root(num1)
#             print(result)
#             logging.info(f'sqrt of {num1} = {result}')
#         if type_num == 0:
#             # нужно ли тут логгирование?
#             menu()
#         else:
#             logging.error('Error: wrong menu selection')
#             break


# def menu_calc_compl(type_num):
#     while True:
#         type_num = int(input('Operations:\n'
#                              '1 - sum +\n'
#                              '2 - sub -\n'
#                              '3 - mult *\n'
#                              '4 - div /\n'
#                              '5 - pow **\n'
#                              '6 - sqrt\n'
#                              '0 - previous menu\n'))
#         if type_num == 1:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             num2 = complex(float(input("enter 2 real part: ")),
#                            float(input('enter 2 imaginary number: ')))
#             result = summ(num1, num2)
#             print(result)
#             logging.info(f'{num1} + {num2} = {result}')
#         if type_num == 2:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             num2 = complex(float(input("enter 2 real part: ")),
#                            float(input('enter 2 imaginary number: ')))
#             result = diff(num1, num2)
#             print(result)
#             logging.info(f'{num1} - {num2} = {result}')
#         if type_num == 3:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             num2 = complex(float(input("enter 2 real part: ")),
#                            float(input('enter 2 imaginary number: ')))
#             result = multi(num1, num2)
#             print(result)
#             logging.info(f'{num1} * {num2} = {result}')
#         if type_num == 4:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             num2 = complex(float(input("enter 2 real part: ")),
#                            float(input('enter 2 imaginary number: ')))
#             result = int_div(num1, num2)
#             print(result)
#             logging.info(f'{num1} / {num2} = {result}')
#         if type_num == 5:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             num2 = complex(float(input("enter 2 real part: ")),
#                            float(input('enter 2 imaginary number: ')))
#             result = exponent(num1, num2)
#             print(result)
#             logging.info(f'{num1} ** {num2} = {result}')
#         if type_num == 6:
#             num1 = complex(float(input("enter 1 real part: ")),
#                            float(input('enter 1 imaginary number: ')))
#             result = square_root(num1)
#             logging.info(f'sqrt of {num1} = {result}')
#             print(result)
#         if type_num == 0:
#             menu()
#         else:
#             logging.error('Error: wrong menu selection')
#             break
