import json
from tabulate import tabulate
import pandas as pd

# Wczytanie danych z pliku JSON
with open('sluzba.json') as file:
    data = json.load(file)

# Konwersja danych do obiektu pandas DataFrame
df = pd.DataFrame(data)

# Funkcja wyświetlania danych w postaci tabeli
def display_table(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

# Funkcja filtrowania danych
def filter_data(df, column, value):
    filtered_df = df[df[column] == value]
    return filtered_df

# Funkcja sortowania danych
def sort_data(df, column):
    sorted_df = df.sort_values(by=column)
    return sorted_df

# Funkcja paginacji danych
def paginate_data(df, page_size, page_number):
    start = (page_number - 1) * page_size
    end = start + page_size
    paginated_df = df.iloc[start:end]
    return paginated_df

# Wyświetlanie danych w postaci tabeli
display_table(df)

# Filtrowanie po atrybucie 'name'
filtered_data = filter_data(df, 'name', 'Dobromir')
display_table(filtered_data)

# Sortowanie po atrybucie 'dateOfBirth'
sorted_data = sort_data(df, 'dateOfBirth')
display_table(sorted_data)

# Paginacja (strona 2, 5 wyników na stronę)
paginated_data = paginate_data(df, 5, 2)
display_table(paginated_data)
