print('Eejmplo con tuplas \n\n')

#Definición de una tupla
tupla_information = ('Ana Picapiedra', 22, 95.5)
print(f'Información de la tupla: {tupla_information}')

# Destructuración o unpacking
full_name, age, salary = tupla_information

print (f'Nombre: {full_name}, Age: {age}, Salary: {salary}')

print('\n\nImpresión de la tupla con un ciclo FOR')
#Impresión de los elementos de una tupla

for item in tupla_information:
    print(item)