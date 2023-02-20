import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    pass

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    '''
    queryString = f"(iso_a3 == {year})"
    leastExp = round(df['dollar_price'].min(),2)
    idx = df["dollar_price"].idxmin()
    leastExpCountry = df.loc[idx]
    print(f"{leastExpCountry['name']}({leastExpCountry['iso_a3']}): {leastExp}")
    '''

def get_the_most_expensive_big_mac_price_by_year(year):
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    print(df_Year)
    mostExp = round(df['dollar_price'].max(),2)
    idx = df["dollar_price"].idxmax()
    mostExpCountry = df.loc[idx]
    print(f"{mostExpCountry['name']}({mostExpCountry['iso_a3']}): {mostExp}")

if __name__ == "__main__":
    df = pd.read_csv(big_mac_file)
    userYear = 2005
    get_the_most_expensive_big_mac_price_by_year(userYear)