import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == {country_code}"
    df_price = df.query(queryString)

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    queryString = f"(iso_a3 == {country_code})"

    

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    min_df_idx = df_Year['dollar_price'].idxmin()
    min_item = df.loc[min_df_idx]
    results = (f"{min_item['name']}({min_item['iso_a3']}): ${round(min_item['dollar_price'],2)}")
    return results

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    max_df_idx = df_Year['dollar_price'].idxmax()
    max_item = df.loc[max_df_idx]
    results = (f"{max_item['name']}({max_item['iso_a3']}): ${round(max_item['dollar_price'],2)}")
    return results

if __name__ == "__main__":
    userCountry = int(input("Enter a year: "))
    userYear = input("Enter a country code: ")
    get_big_mac_price_by_country(userCountry)
    get_the_cheapest_big_mac_price_by_year(userYear)
    get_the_most_expensive_big_mac_price_by_year(userYear)