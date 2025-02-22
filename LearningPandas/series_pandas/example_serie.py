import pandas as pd

#Colección de datos
list_ice_cream = ['Lemon', 'Chocolate', 'Vanilla']
series = pd.Series(list_ice_cream)
print(f' Este es el contenido de la serie: \n {series}')

#Indice personalizado
index = ['a', 'b', 'c']
serie_2 = pd.Series(list_ice_cream, index)
print(f'\n\n Este es el contenido de la serie 2: \n {serie_2}')