import interface as i
import view as v
import math_fun as m
from logger import logging


def button_click():
    while True:
        type_num = i.menu()
        op = i.menu_calc(type_num)
        if op == -1:
            break

        if type_num == 1:
            if op == 7:
                print('Enter number: ', end="")
                num1 = v.get_value(op)
                result = m.square_root(num1)
                v.view_result(result)
                logging.info(f'sqrt of {num1} = {result}')
            elif op == 0:
                button_click()
            else:
                print('Enter 1 number: ', end="")
                num1 = v.get_value(op)
                print('Enter 2 number: ', end="")
                num2 = v.get_value(op)
                if op == 1:
                    result = m.summ(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} + {num2} = {result}')
                elif op == 2:
                    result = m.diff(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} - {num2} = {result}')
                elif op == 3:
                    result = m.multi(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} * {num2} = {result}')
                elif op == 4:
                    result = m.int_div(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} / {num2} = {result}')
                elif op == 5:
                    result = m.remain_div(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} % {num2} = {result}')
                elif op == 6:
                    result = m.exponent(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} ^ {num2} = {result}')

        elif type_num == 2:
            if op == 6:
                print('Enter real part: ', end="")
                num1_real = v.get_value()
                print('Enter imaginary number: ', end="")
                num1_imag = v.get_value()
                num1 = complex(num1_real, num1_imag)
                result = m.square_root(num1)
                v.view_result(result)
                logging.info(f'sqrt of {num1} = {result}')
            elif op == 0:
                button_click()
            else:
                print('Enter 1 real part: ', end="")
                num1_real = v.get_value()
                print('Enter 1 imaginary number: ', end="")
                num1_imag = v.get_value()
                num1 = complex(num1_real, num1_imag)
                print('Enter 2 real part: ', end="")
                num2_real = v.get_value()
                print('Enter 2 imaginary number: ', end="")
                num2_imag = v.get_value()
                num2 = complex(num2_real, num2_imag)
                if op == 1:
                    result = m.summ(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} + {num2} = {result}')
                elif op == 2:
                    result = m.diff(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} - {num2} = {result}')
                elif op == 3:
                    result = m.multi(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} * {num2} = {result}')
                elif op == 4:
                    result = m.int_div(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} / {num2} = {result}')
                elif op == 5:
                    result = m.exponent(num1, num2)
                    v.view_result(result)
                    logging.info(f'{num1} ^ {num2} = {result}')

