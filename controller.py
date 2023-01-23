import view as v
import math_fun as m
from logger import logging

def button_click():
    logging.info('Start programm')
    while True:
        try:
            type_num = int(input('Working with:\n'
                            '1 - rational\n'
                            '2 - complex\n'
                            '3 - exit\n'))
            if type_num == 1:
                rational_evaluation()
            elif type_num == 2:
                complex_evaluation()
            elif type_num == 3:
                logging.info('Programm close')
                break
            else:
                logging.error('Invalid input for number type')
                raise Exception('Invalid input for number type')
        except Exception as err:
            logging.error(err)
            print("ERROR. Try again")
            

def rational_evaluation():
    op = int(input('Operations:\n'
                    '1 - sum +\n'
                    '2 - sub -\n'
                    '3 - mult *\n'
                    '4 - div /\n'
                    '5 - pow **\n'
                    '6 - sqrt\n'
                    '7 - %\n'
                    '0 - previous menu\n'))
    if 0 <= op < 8:
        result = None
        title = ''
        if op == 0:
            logging.info('Open previous menu')
            return
        elif op == 6:
            print('Enter number: ', end="")
            num1 = v.get_value()
            result = m.square_root(num1)
            title = f'sqrt of {num1}'
            logging.info(f'sqrt of {num1} = {result}')
        else:
            print('Enter 1 number: ', end="")
            num1 = v.get_value()
            print('Enter 2 number: ', end="")
            num2 = v.get_value()
            if op == 1:
                result = m.summ(num1, num2)
                title = f'{num1} + {num2}'
                logging.info(f'{num1} + {num2} = {result}')
            elif op == 2:
                result = m.diff(num1, num2)
                title = f'{num1} - ({num2})'
                logging.info(f'{num1} - {num2} = {result}')
            elif op == 3:
                result = m.multi(num1, num2)
                title = f'{num1} * {num2}'
                logging.info(f'{num1} * {num2} = {result}')
            elif op == 4:
                result = m.int_div(num1, num2)
                title = f'{num1} / {num2}'
                logging.info(f'{num1} / {num2} = {result}')
            elif op == 5:
                result = m.exponent(num1, num2)
                title = f'{num1} ^ {num2}'
                logging.info(f'{num1} ^ {num2} = {result}')
            else:
                result = m.remain_div(num1, num2)
                title = f'{num1} % {num2}'
                logging.info(f'{num1} % {num2} = {result}')
    else:
        raise Exception('invalid operation type')
    v.view_result(result, title)    


def complex_evaluation():
    op = int(input('Operations:\n'
                '1 - sum +\n'
                '2 - sub -\n'
                '3 - mult *\n'
                '4 - div /\n'
                '5 - pow **\n'
                '6 - sqrt\n'
                '0 - previous menu\n'))
    if 0 <= op < 7:           
        result = None
        title = ''
        if op == 0:
            logging.info('Open previous menu')
            return
        elif op == 6:
            print('Enter real part: ', end="")
            num1_real = v.get_value()
            print('Enter imaginary number: ', end="")
            num1_imag = v.get_value()
            num1 = complex(num1_real, num1_imag)
            result = m.square_root(num1)
            title = f'sqrt of {num1}'
            logging.info(f'sqrt of {num1} = {result}')
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
                title = f'{num1} + {num2}'
                logging.info(f'{num1} + {num2} = {result}')
            elif op == 2:
                result = m.diff(num1, num2)
                title = f'{num1} - ({num2})'
                logging.info(f'{num1} - {num2} = {result}')
            elif op == 3:
                result = m.multi(num1, num2)
                title = f'{num1} * {num2}'
                logging.info(f'{num1} * {num2} = {result}')
            elif op == 4:
                result = m.int_div(num1, num2)
                title = f'{num1} / {num2}'
                logging.info(f'{num1} / {num2} = {result}')
            else:
                result = m.exponent(num1, num2)
                title = f'{num1} ^ {num2}'
                logging.info(f'{num1} ^ {num2} = {result}') 
    else:
        raise Exception('invalid operation type')
    v.view_result(result,title)