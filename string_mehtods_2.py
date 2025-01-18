# Otros metodos

message = 'Los cuervos de la UTVT'

#len
size = len(message)

#replace
new_message = message.replace('','')

#find
indexof = message.find('u')

#split
message_slice = message.split()

print(f'Longitud de la cadena: {size}')
print(f'Nueva cadena: {new_message}')
print(f'Posicion del elemento buscado: {indexof}')
print(f'Cadena particionada: {message_slice}')