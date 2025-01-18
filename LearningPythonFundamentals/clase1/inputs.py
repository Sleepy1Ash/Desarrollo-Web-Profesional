# Entrada de datos mediante la consola INPUT

name = input(' ¿Cual es el nombre? ')
age = int(input( ' ¿Cual es tu edad? '))
salary = float(input('¿Cual es tu salario?'))
total_pets = eval(input(' ¿Cuantas mascotas tienes?'))
university = input( '¿Cual es el nombre de tu universidad? ')

print(f'Hola, me llamo {name}, mi edad es {age} y mi universidad {university}')
print(type(name))
print(type(age))
print(type(salary))
print(type(total_pets))
