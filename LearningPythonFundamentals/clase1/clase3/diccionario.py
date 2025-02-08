#Declarar un diccionario
student = {
    'name' : 'Pedrito Perez',
    'age' : 25,
    'language' : 'Python',
    'city' : 'Lerma'
}
#acceso a los valores del diccionario
print(f'Contenido total del estudiante: {student}')
print(f'Nombre: {student["name"]}')
print(f'Edad: {student.get("age")}')

print('--- Operaciones basicas sobre diccionarios ---')
#Modificar valores
student['language'] = 'C#'
print(f'\nContenido actual del estudiante una vez modificado el lenguaje: {student}')

#Eliminar elementos
student.pop('city')
print(f'\nContenido del estudiante una vez eliminado la ciudad: {student}')

#Agregar elementos
student['comida'] = 'Galletas'
print(f'\nContenido actual del estudiante una vez agregada la comida: {student}')

print('\n\n\n--- Iterar sobre un diccionario ---')
print('\nIteracion de los elementos de un diccionario, simple')

for element in student:
    print(f'{element}:{student[element]}')

print('\nIteracion de los elementos de un diccionario, destructuracion - unpacking')

for key, value in student.items():
    print(f'Llave: {key}, Valor: {value}')

print('\nIteracion de los elementos de un diccionario, llaves')

for key in student.keys():
    print(f'Llave: {key}')

print('\nIteracion de los elementos de un diccionario, valores')

for value in student.values():
    print(f'Valor: {value}')