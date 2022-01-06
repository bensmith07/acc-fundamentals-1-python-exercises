# This program converts imperial measurement inputs to metric and displays the metric values. 

MENU_CHOICES = list(range(1,6))
ITERATIONS = 12

def display_menu():
    print()
    print('Which conversion would you like to perform?')
    print('Enter a number 1-5 to choose.')
    print()
    print('[1] MILES TO KILOMETERS')
    print('[2] FAHRENHEIT TO CELSIUS')
    print('[3] GALLONS TO LITERS')
    print('[4] POUNDS TO KILOGRAMS')
    print('[5] INCHES TO CENTIMETERS')
    print()

def main():

    import conversion_functions as convert

    #open file for writing
    outfile = open('conversions.txt', 'w')

    #initiate loop
    for count in range(1, ITERATIONS+1):
    
        try:
            #ask the user which conversion they would like to perform
            display_menu()
            menu_selection = int(input('Make a selection: '))
            #Check for invalid menu selection, raise exception
            if menu_selection not in MENU_CHOICES:
                raise ValueError
            #Continue program if menu selection is valid
            else:

                #MILES TO KILOMETERS
                if menu_selection == 1:
                    miles = float(input('Enter the number of miles: '))
                    try:
                        if miles < 0:
                            raise ValueError
                        else:
                            #perform conversion and write to file
                            outfile.write(str(miles) + ' mile(s) is ' + str(format(convert.MilesToKm(miles), '.2f')) + ' kilometer(s).' + '\n')
                    except ValueError:
                        print()
                        print('Invalid input. Number of miles cannot be negative.')

                #FAHRENHEIT TO CELSIUS
                elif menu_selection == 2:
                    fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
                    try:
                        if fahrenheit >= 1000:
                            raise ValueError
                        else:
                            #perform conversion and write to file
                            outfile.write(str(fahrenheit) + ' degrees Fahrenheit is ' + str(format(convert.FahToCel(fahrenheit), '.2f')) + ' degrees Celsius.' + '\n')
                    except ValueError:
                        print()
                        print('Invalid input. Temperature cannot be more than 1000.')

                #GALLONS TO LITERS
                elif menu_selection == 3:
                    gallons = float(input('Enter the number of gallons: '))
                    try:
                        if gallons < 0:
                            raise ValueError
                        else:
                            #perform conversion and write to file
                            outfile.write(str(gallons) + ' gallons is ' + str(format(convert.GalToLit(gallons), '.2f')) + ' liters.' + '\n')
                    except ValueError:
                        print()
                        print('Invalid input. Number of gallons cannot be negative.')

                #POUNDS TO KILOGRAMS
                elif menu_selection == 4:
                    pounds = float(input('Enter the number of pounds: '))
                    try:
                        if pounds < 0:
                            raise ValueError
                        else:
                            #perform conversion and write to file
                            outfile.write(str(pounds) + ' pounds is ' + str(format(convert.PoundsToKg(pounds), '.2f')) + ' kilograms.' + '\n')
                    except ValueError:
                        print()
                        print('Invalid input. Number of pounds cannot be negative.')
                    
                #INCHES TO CENTIMETERS
                elif menu_selection == 5:
                    inches = float(input('Enter the number of inches: '))
                    try:
                        if inches < 0:
                            raise ValueError
                        else:
                            #perform conversion and write to file
                            outfile.write(str(inches) + ' inches is ' + str(format(convert.InchesToCm(inches), '.2f')) + ' centimeters.' + '\n')
                    except ValueError:
                        print()
                        print('Invalid input. Number of inches cannot be negative.')

        except ValueError:
            print()
            print('You must make a selection by entering a number 1-5.')
            print('Please try again.')

    #close file and end program
    outfile.close()
    print()
    print('Conversions complete.')
    print('Open the conversions.txt file to see your conversions.')

main()

    
