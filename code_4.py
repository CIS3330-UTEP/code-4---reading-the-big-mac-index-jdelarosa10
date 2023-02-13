import csv
#import pandas as pd
big_mac_file = open('./big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    pass
    '''
    for i in big_mac_file:
        if i is year and i is country_code:
            avgPrice = 
    '''
def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    min = 0
    for i in big_mac_file:
        if i == 'dollar price':
            min = int(i)
    return min

def get_the_most_expensive_big_mac_price_by_year(year):
    max = 0
    getIndex = 0
    for i in big_mac_file:
        if i == 'dollar price':
            getIndex = getIndex + 1
    return getIndex

if __name__ == "__main__":
    userYear = int(input("Enter the year you want to search for: "))
    userCountry = (input("Enter the country you want to search for: "))
    #need to convert userCountry to code 
    get_big_mac_price_by_year(userYear, userCountry)
    print(get_the_cheapest_big_mac_price_by_year(userYear))
    print(get_the_most_expensive_big_mac_price_by_year(userYear))