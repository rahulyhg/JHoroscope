# JHoroscope
JHoroscope is a basic module to fetch the Horoscope of different Zodiac signs.
It is very simple to use and return the dictionary or json according to user demand

#How to use

from JHoroscope import Horoscope
myhoroscope = Horoscope()
"""
All the horoscopes are returned in a dictionary with key the zodiac sign name and the value is in the result.
The first Letter of all the signs should be capital.
"""

#To get all daily horoscope
myhoroscope.daily_horoscope()

#to get particular daily horoscope
cancer = myhoroscope.daily_horoscope(['Cancer'])

#to print use print(cancer['Carcer'])
print(cancer['Carcer'])

#get all the monthy horoscope
myhoroscope.get_by_month()

#For particular horoscope of a month you can pass a list of zodiac signs like this
myhoroscope.get_by_month(['Cancer','Virgo','Libra'])

#Same for yearly and weekly horoscopes


"""
Methods inside Horoscope class
myhoroscope.get_by_month()
myhoroscope.daily_horoscope()
myhoroscope.get_by_week()
myhoroscope.get_by_year()
All of these methods get the list of Zodiac signs or you can leave them empty if you want to fetch all the zodiac details
"""


#To get the Json format of the hotoscope pass True as second argument
cancer = myhoroscope.daily_horoscope(['Cancer'],True)

#or like this
cancer = myhoroscope.daily_horoscope(zname=['Cancer'],json=True)
