import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}'"
    df_price = df.query(queryString)
    avg = round(df_price["dollar_price"].mean(),2)
    return avg

def get_big_mac_price_by_country(country_code):
    queryString = f"iso_a3 == '{country_code.upper()}'"
    df_country = df.query(queryString)
    countryAvg = round(df_country['dollar_price'].mean(),2)
    return countryAvg

def get_the_cheapest_big_mac_price_by_year(year):
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    min_df_idx = df_Year['dollar_price'].idxmin()
    min_item = df.loc[min_df_idx]
    results = (f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'],2)}")
    return results

def get_the_most_expensive_big_mac_price_by_year(year):
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    max_df_idx = df_Year['dollar_price'].idxmax()
    max_item = df.loc[max_df_idx]
    results = (f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'],2)}")
    return results

if __name__ == "__main__":
    userCountry = input("Enter a country code: ")
    userYear = int(input("Enter a year: "))
    get_big_mac_price_by_year(userYear, userCountry)
    get_big_mac_price_by_country(userCountry)
    get_the_cheapest_big_mac_price_by_year(userYear)
    get_the_most_expensive_big_mac_price_by_year(userYear)