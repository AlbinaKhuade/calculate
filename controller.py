import view as v
import math_fun as m
from logger import logging

def button_click():
    logging.info('Start programm')
    print('Hello!\U0001F44B You have started using our calculator '+chr(128522))
    while True:
        try:
            type_num = int(input('Working with numbers \U0001F522:\n'+
                            chr(65297)+'- rational\n'+
                            chr(65298)+'- complex\n'+
                            chr(65299)+'- exit\n'))
            if 0 < type_num < 4:              
                if type_num == 1:
                    rational_evaluation()
                elif type_num == 2:
                    complex_evaluation()
                else:
                    logging.info('Programm close')
                    print('Bye! '+chr(128521)+' We hope you enjoyed our calculator!')
                    break
            else:
                raise Exception()
        except Exception as err:
            logging.error(err)
            print("ERROR "+chr(10060)+" Try again")
                
def rational_evaluation():
    op = int(input('Operations:\n'+
                    chr(65297)+'- sum +\n'+ 
                    chr(65298)+'- sub -\n'+
                    chr(65299)+'- mult *\n'+
                    chr(65300)+'- div /\n'+
                    chr(65301)+'- pow **\n'+
                    chr(65302)+'- root '+chr(8730)+'\n' +
                    chr(65303)+'- div %\n'+
                    chr(65296)+'- previous menu\n'))
    if 0 <= op < 8:
        result = None
        title = ''
        if op == 0:
            logging.info('Open previous menu')
            return
        elif op == 6:
            print('Enter the root indicator: ', end="")
            indic = v.get_value()
            print('Enter number: ', end="")
            num = v.get_value()
            if indic % 2 == 0 and num > 0:
                result = m.any_root(num, indic)
                title = f'{indic} root from {num}'
                logging.info(f'{title} = {result}')
            elif indic % 2 != 0:
                result = m.any_root(num, indic)
                title = f'{indic} root from {num}'
                logging.info(f'{title} = {result}')
            else:
                raise Exception()          
        else:
            print('Enter 1 number: ', end="")
            num1 = v.get_value()
            print('Enter 2 number: ', end="")
            num2 = v.get_value()
            if op == 1:
                result = m.summ(num1, num2)
                title = f'{num1} + {num2}'
                logging.info(f'{title} = {result}')
            elif op == 2:
                result = m.diff(num1, num2)
                title = f'{num1} - ({num2})'
                logging.info(f'{title} = {result}')
            elif op == 3:
                result = m.multi(num1, num2)
                title = f'{num1} * {num2}'
                logging.info(f'{title} = {result}')
            elif op == 4:
                result = m.int_div(num1, num2)
                title = f'{num1} / {num2}'
                logging.info(f'{title} = {result}')
            elif op == 5:
                result = m.exponent(num1, num2)
                title = f'{num1} ^ {num2}'
                logging.info(f'{title} = {result}')
            else:
                result = m.remain_div(num1, num2)
                title = f'{num1} % {num2}'
                logging.info(f'{title} = {result}')
    else:
        raise Exception()
    v.view_result(result, title)    


def complex_evaluation():
    op = int(input('Operations:\n'+
                chr(65297)+'- sum +\n'+ 
                chr(65298)+'- sub -\n'+
                chr(65299)+'- mult *\n'+
                chr(65300)+'- div /\n'+
                chr(65301)+'- pow **\n'+
                chr(65302)+'- root\n'+
                chr(65296)+'- previous menu\n'))
    if 0 <= op < 7:           
        result = None
        title = ''
        if op == 0:
            logging.info('Open previous menu')
            return
        elif op == 6:
            print('Enter the root indicator: ', end="")
            indic = v.get_value()
            print('Enter real part: ', end="")
            num_real = v.get_value()
            print('Enter imaginary number: ', end="")
            num_imag = v.get_value()
            num = complex(num_real, num_imag)
            if indic % 2 == 0 and num > 0:
                result = m.any_root(num, indic)
                title = f'{indic} root from {num}'
                logging.info(f'{title} = {result}')
            elif indic % 2 != 0:
                result = m.any_root(num, indic)
                title = f'{indic} root from {num}'
                logging.info(f'{title} = {result}')
            else:
                raise Exception()  
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
                logging.info(f'{title} = {result}')
            elif op == 2:
                result = m.diff(num1, num2)
                title = f'{num1} - ({num2})'
                logging.info(f'{title} = {result}')
            elif op == 3:
                result = m.multi(num1, num2)
                title = f'{num1} * {num2}'
                logging.info(f'{title} = {result}')
            elif op == 4:
                result = m.int_div(num1, num2)
                title = f'{num1} / {num2}'
                logging.info(f'{title} = {result}')
            else:
                result = m.exponent(num1, num2)
                title = f'{num1} ^ {num2}'
                logging.info(f'{title} = {result}') 
    else:
        raise Exception()
    v.view_result(result,title)