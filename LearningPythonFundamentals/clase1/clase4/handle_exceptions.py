result = None
numero_x = 10
numero_y = 0

try:
    numero_x = int(input('Ingresa un numero para X: '))
    numero_y = int(input('Ingresa un numero para Y: '))
    result = numero_x / numero_y
    print(f'\nEl resultado de la divición es {result}')
except ZeroDivisionError as e:
    print(f'La excepcion es la siguiente: {e}')
except ValueError as e:
    print(f'La excepcion de ValueError genero el sisguiente mensaje: {e}')
except Exception as e:
    print(f'La excepcion de Exception genero el sisguiente mensaje: {e}')
finally:
    print('Nuestro programa a finalizado')