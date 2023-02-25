import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    pass

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass 

def get_the_most_expensive_big_mac_price_by_year(year):
    queryString = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_Year = df.query(queryString)
    min_df_idx = df['dollar_price'].idxmin()
    min_item = df.loc[min_df_idx]
    print(f"{min_item['name']}({min_item['iso_a3']}):")
    #: {round(min_item['dollarprice'],2)}")
    
if __name__ == "__main__":
    df = pd.read_csv(big_mac_file)
    userYear = 2000
    get_the_most_expensive_big_mac_price_by_year(userYear)