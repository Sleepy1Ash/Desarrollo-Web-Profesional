import pandas as pd

nba_players = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', usecols=['DRtg']).squeeze()
some_values = nba_players.iloc[:5]

addition_1 = some_values + 10
addition_2 = some_values.add(10)

print(f'Realización de una suma')
print(some_values)
print(addition_1)
print(addition_2)

print(f'Realización de una resta')
subtract_1 = some_values - 10
subtract_2 = some_values.subtract(10)

print(subtract_1)
print(subtract_2)

#Realizar la operacion para la multiplicacion y la divicion
print(f'Realización de una multiplicación')
multiply_1 = some_values * 10
multiply_2 = some_values.multiply(10)

print(multiply_1)
print(multiply_2)

print(f'Realización de una division')
divide_1 = some_values / 10
divide_2 = some_values.divide(10)

print(divide_1)
print(divide_2)