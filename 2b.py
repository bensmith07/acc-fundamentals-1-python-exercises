#Define conversion rates
milesToKilometers = 1.6
fahrenheitToCelsius1 = 32
fahrenheitToCelsius2 = (5/9)
gallonsToLiters = 3.9
poundsToKilograms = .45
inchesToCentimeters = 2.54

#Get the values to be converted
miles = float(input('Enter the number of miles: '))
fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
gallons = float(input('Enter the number of gallons: '))
pounds = float(input('Enter the number of pounds: '))
inches = float(input('Enter the number of inches: '))

#Convert the values to metric
kilometers = miles * milesToKilometers
celsius = (fahrenheit - fahrenheitToCelsius1) * fahrenheitToCelsius2
liters = gallons * gallonsToLiters
kilograms = pounds * poundsToKilograms
centimeters = inches * inchesToCentimeters

#Display the new values, rounded to two decimal places
print(miles, 'miles is', format(kilometers, '.2f'), 'kilometers.')
print(fahrenheit, 'degrees Fahrenheit is', format(celsius, '.2f'), 'degrees Celsius.' )
print(gallons, 'gallons is', format(liters, '.2f'), 'liters.')
print(pounds, 'pounds is', format(kilograms, '.2f'), 'kilograms.')
print(inches, 'inches is', format(centimeters, '.2f'), 'centimeters.')