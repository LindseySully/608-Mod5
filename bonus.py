"""Designed for data validation of phone numbers, zip code, and city names"""
#Written by Lindsey Sullivan

from multiprocessing.sharedctypes import Value
import pandas as pd

#Zip Codes
zips = pd.Series({'Boston':'02215','Miami':'3110','Kansas City':'64151'})
#checking if zipcode is valid(exactly 5 digits)
str_match = zips.str.match(r'\d{5}')

print('Zip Code Results:')
print(str_match)#results of zipcode

#City Names
cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101', 'Kansas City, MO 64151'])

#check if each entry includes letters and if it matches the defined pattern
#patterns is a space after the city name, followed by two upppercase letters for the state, followed by a space

cities_contain = cities.str.contains(r' [A-Z]{2} ')
cities_match = cities.str.match(r' [A-Z]{2} ')

print('Cities Results:')
print(cities_contain,cities_match)
#Written by Lindsey Sullivan

#Contacts
contacts = [['Mike Green', 'demo1@dietel.com', '5555555555'],['Sue Brown', 'demo2@deitel.com','5555551234'], ['Lindsey Sullivan','demo3@deitel.com','5555555890']]

#creating the data frame
contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone Number'])

print(contactsdf)


#reformat phone numbers to include hyphens

import re

contacts = [['Mike Green', 'demo1@dietel.com', '5555555555'],['Sue Brown', 'demo2@deitel.com','5555551234'], ['Lindsey Sullivan','demo3@deitel.com','5555557890']]
contactsdf = pd.DataFrame(contacts, columns = ['Name', 'Email', 'Phone Number'])

def get_formatted_phone(value) :
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Phone Number'].map(get_formatted_phone)
print(formatted_phone)

contactsdf['Phone Number'] = formatted_phone
print(contactsdf)
