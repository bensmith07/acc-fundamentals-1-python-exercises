# This module includes functions that convert
# imperial measurements to metric values.

# The MilesToKm() function converts miles to
# kilometers and displays the number of kilometers. 
def MilesToKm(miles):
    MILES_TO_KILOMETERS = 1.6
    kilometers = miles * MILES_TO_KILOMETERS
    return(kilometers)
    
# The FahToCel() function converts degrees fahrenheit
# to degrees celsius and displays the degrees celsius. 
def FahToCel(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_1 = 32
    FAHRENHEIT_TO_CELSIUS_2 = (5/9)
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_1) * FAHRENHEIT_TO_CELSIUS_2
    return(celsius)

# The GalToLit function converts gallons to liters
# and displays the number of liters. 
def GalToLit(gallons):
    GALLONS_TO_LITERS = 3.9
    liters = gallons * GALLONS_TO_LITERS
    return(liters)
    
# The PoundsToKg() function converts pounds to
# kilograms and displays the number of kilograms. 
def PoundsToKg(pounds):
    POUNDS_TO_KILOGRAMS = .45
    kilograms = pounds * POUNDS_TO_KILOGRAMS
    return(kilograms)
    
# The InchesToCm() function converts inches to
# centimeters and displays the number of centimeters.  
def InchesToCm(inches):
    INCHES_TO_CENTIMETERS = 2.54
    centimeters = inches * INCHES_TO_CENTIMETERS
    return(centimeters)

    
