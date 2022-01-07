#Define conversion rates
milesToKilometers = 1.6
fahrenheitToCelsius1 = 32
fahrenheitToCelsius2 = (5/9)
gallonsToLiters = 3.9
poundsToKilograms = .45
inchesToCentimeters = 2.54

#Define maximum number of invalid inputs that will be allowed
max_tries = 4

#Get the values to be converted
counter = 0
miles = float(input('Enter the number of miles: '))
while miles < 0 and counter < (max_tries - 1):
    print('Invalid input. Number of miles cannot be negative. Try again.')
    miles = float(input('Enter the number of miles: '))
    counter += 1
if miles >= 0:
    counter = 0
    fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
    while fahrenheit > 1000 and counter < (max_tries - 1):
        print('Invalid input. Temperature must be less than 1000. Try again.')
        fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
        counter += 1
    if fahrenheit <= 1000:
        counter = 0
        gallons = float(input('Enter the number of gallons: '))
        while gallons < 0 and counter < (max_tries - 1):
            print('Invalid input. Number of gallons cannot be negative. Try again.')
            gallons = float(input('Enter the number of gallons: '))
            counter += 1
        if gallons >= 0:
            counter = 0
            pounds = float(input('Enter the number of pounds: '))
            while pounds < 0 and counter < (max_tries - 1):
                print('Invalid input. Number of pounds cannot be negative. Try again.')
                pounds = float(input('Enter the number of pounds: '))
                counter += 1
            if pounds >= 0:
                counter = 0
                inches = float(input('Enter the number of inches: '))
                while inches < 0 and counter < (max_tries - 1):
                    print('Invalid input. Number of inches cannot be negative. Try again.')
                    inches = float(input('Enter the number of inches: '))
                    counter += 1
                if inches >= 0: 
                        
                    #Convert the values to metric
                    kilometers = miles * milesToKilometers
                    celsius = (fahrenheit - fahrenheitToCelsius1) * fahrenheitToCelsius2
                    liters = gallons * gallonsToLiters
                    kilograms = pounds * poundsToKilograms
                    centimeters = inches * inchesToCentimeters
                        
                    #Display the new values, rounded to two decimal places
                    print('Here are the converted values:')
                    print(miles, 'miles is', format(kilometers, '.2f'), 'kilometers.')
                    print(fahrenheit, 'degrees Fahrenheit is', format(celsius, '.2f'), 'degrees Celsius.' )
                    print(gallons, 'gallons is', format(liters, '.2f'), 'liters.')
                    print(pounds, 'pounds is', format(kilograms, '.2f'), 'kilograms.')
                    print(inches, 'inches is', format(centimeters, '.2f'), 'centimeters.')
                    
                else:
                    print('Invalid input. Number of inches cannot be negative. Goodbye.')
            else:
                print('Invalid input. Number of pounds cannot be negative. Goodbye.')
        else:
            print('Invalid input. Number of gallons cannot be negative. Goodbye.')
    else:
        print('Invalid input. Temperature must be less than 1000. Goodbye.')
else:
    print('Invalid input. Number of miles cannot be negative.Goodbye.')
