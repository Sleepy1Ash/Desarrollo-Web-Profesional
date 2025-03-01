import pandas as pd

nba_players_name = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
nba_players_age = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['AGE']).squeeze()

print(f'Nombre de los jugadores: \n {nba_players_name}')
print(f'\nEdad de los jugadores: \n {nba_players_age}')

print(f'Funcion LEN: {len(nba_players_name)}')
print(f'Funcion TYPE: {type(nba_players_name)}')
print(f'Funcion SORTED: {sorted(nba_players_age)}')
print(f'Funcion MAX: {max(nba_players_age)}')
print(f'Funcion MIN: {min(nba_players_age)}')
