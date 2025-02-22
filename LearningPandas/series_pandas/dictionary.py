import pandas as pd

kid_gifts = {
    'videogames': 'Play 5',
    'boardgames': 'Monopoly',
}
serie = pd.Series(kid_gifts)
print(f'\n{serie}')