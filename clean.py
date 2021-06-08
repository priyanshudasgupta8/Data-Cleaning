from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time 
import csv
import requests
import pandas as pd

# OPEN THE URL
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(start_url)
soup = bs(page.text,'html.parser')
star_table = soup.find('table')

# FUNTION FOR ADDING AND SCRAPPING THE DATA

temp_list =[]

table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td ]
    temp_list.append(row)



print(temp_list)

star_names = []
star_distance = []
star_mass = []
star_radius = []
star_lum = []
star_solar_mass = []
star_solar_radius = []
star_apparent_magnitude = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    star_distance.append(temp_list[i][3])
    star_mass.append(temp_list[i][7])
    star_radius.append(temp_list[i][6])
    star_lum.append(temp_list[i][7])

    try:
        mass_val = float(temp_list[i][7])
        
    except Exception as err:
        mass_val = 0.0
    
    star_solar_mass.append(mass_val *0.000954588)

    try:
        radius_val = float(temp_list[i][6])
        print(radius_val)
    except Exception as err:
        radius_val = 0.0
    
    star_solar_radius.append(radius_val*0.102763)

    star_apparent_magnitude.append(temp_list[i][0])

df = pd.DataFrame(list(zip(star_names,star_distance,star_mass,star_radius,star_lum,star_solar_mass,star_solar_radius,star_apparent_magnitude)),columns = ['star_names','distance','mass','radius','luminosity','solar_mass','solar_radius','apparent_magintude'])

df.to_csv('stars.csv')
