# This program converts imperial measurement inputs to metric and displays the metric values. 

def display_menu():
    print('Which conversion would you like to perform?')
    print('[1] MILES TO KILOMETERS')
    print('[2] FAHRENHEIT TO CELSIUS')
    print('[3] GALLONS TO LITERS')
    print('[4] POUNDS TO KILOGRAMS')
    print('[5] INCHES TO CENTIMETERS')
    print('[0] EXIT PROGRAM')
    print()

def main():

    import conversion
    
    #Define maximum number of invalid inputs that will be allowed
    max_invalid_inputs = 4

    #Get the values to be converted
    invalid_inputs = 0
    miles = float(input('Enter the number of miles: '))
    while miles < 0 and invalid_inputs < (max_invalid_inputs - 1):
        print('Invalid input. Number of miles cannot be negative. Try again.')
        miles = float(input('Enter the number of miles: '))
        invalid_inputs += 1
    if miles >= 0:
        invalid_inputs = 0
        fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
        while fahrenheit > 1000 and invalid_inputs < (max_invalid_inputs - 1):
            print('Invalid input. Temperature must be less than 1000. Try again.')
            fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
            invalid_inputs += 1
        if fahrenheit <= 1000:
            invalid_inputs = 0
            gallons = float(input('Enter the number of gallons: '))
            while gallons < 0 and invalid_inputs < (max_invalid_inputs - 1):
                print('Invalid input. Number of gallons cannot be negative. Try again.')
                gallons = float(input('Enter the number of gallons: '))
                invalid_inputs += 1
            if gallons >= 0:
                invalid_inputs = 0
                pounds = float(input('Enter the number of pounds: '))
                while pounds < 0 and invalid_inputs < (max_invalid_inputs - 1):
                    print('Invalid input. Number of pounds cannot be negative. Try again.')
                    pounds = float(input('Enter the number of pounds: '))
                    invalid_inputs += 1
                if pounds >= 0:
                    invalid_inputs = 0
                    inches = float(input('Enter the number of inches: '))
                    while inches < 0 and invalid_inputs < (max_invalid_inputs - 1):
                        print('Invalid input. Number of inches cannot be negative. Try again.')
                        inches = float(input('Enter the number of inches: '))
                        invalid_inputs += 1
                    if inches >= 0:

                        # Convert the values to metric
                        # and display the new values values, rounded to two decimal places
                        print()
                        print('Here are the converted values:')
                        print()
                        print(miles, 'miles is', format(conversion.MilesToKm(miles), '.2f'), 'kilometers.')
                        print(fahrenheit, 'degrees Fahrenheit is', format(conversion.FahToCel(fahrenheit), '.2f'), 'degrees Celsius.' )
                        print(gallons, 'gallons is', format(conversion.GalToLit(gallons), '.2f'), 'liters.')
                        print(pounds, 'pounds is', format(conversion.PoundsToKg(pounds), '.2f'), 'kilograms.')
                        print(inches, 'inches is', format(conversion.InchesToCm(inches), '.2f'), 'centimeters.')

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

main()  
    
