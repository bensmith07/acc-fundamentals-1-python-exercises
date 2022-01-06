
def main():
    write_data()
    read_data()
    append_data()
    read_data()
    remove_data()
    read_data
    replace_data()
    read_data

def write_data():
    #open file for writing
    c_file = open('coffeeInventory.txt', 'w')
    #write initial data to file
    c_file.write('Blonde Roast' + '\n')
    c_file.write('15' + '\n')
    c_file.write('Medium Roast' + '\n')
    c_file.write('21' + '\n')
    c_file.write('Flavored Roast' + '\n')
    c_file.write('10' + '\n')
    c_file.write('Dark Roast' + '\n')
    c_file.write('12' + '\n')
    c_file.write('Costa Rica Tarrazu' + '\n')
    c_file.write('18' + '\n')
    #close the file
    c_file.close()


def read_data():

    print()
    input('Press Enter to display the current coffee inventory:')
    print()
    print('Here is the current coffee inventory:')
    
    #open the file for reading
    c_file = open('coffeeInventory.txt', 'r')

    #keep track of sum of pounds
    total_pounds = 0

    #read and display data
    description = c_file.readline()
    while description != '':
        pounds = c_file.readline()
        description = description.rstrip('\n')
        pounds = pounds.rstrip('\n')
        total_pounds += float(pounds)
        print()
        print('Description: ', description)
        print('Pounds: ', pounds)
        description = c_file.readline()

    #display sum
    print()
    print('Total Pounds = ', total_pounds)

    #close the file
    c_file.close()


def append_data():

    print()
    input('Press enter to append additional data to the file:')
    
    #open the file for appending
    c_file = open('coffeeInventory.txt', 'a')

    #append records to file
    c_file.write('Guatemala Antigua' + '\n')
    c_file.write('22' + '\n')
    c_file.write('House Blend' + '\n')
    c_file.write('25' + '\n')
    c_file.write('Decaf House Blend' + '\n')
    c_file.write('16' + '\n')

    #close file
    c_file.close()

    print()
    print('Additional data has been appended to the file.')

def remove_data():

    import os

    #create flag variable to determine
    #whether the search term is found in the file
    found = False
    
    #prompt user for a description to delete
    print()
    search = input('Which coffee would you like to delete?: ')

    #open files
    c_file = open('coffeeInventory.txt', 'r')
    temp_file = open('temp.txt', 'w')

    #search the file
    description = c_file.readline()
    while description != '':
        pounds = (c_file.readline())
        description = description.rstrip('\n')
        pounds = pounds.rstrip('\n')

        #if search term is found, change flag variable to True
        #and do not write the record to the new file
        if description == search:
            found = True
        #write all other records to the new file    
        else:
            temp_file.write(description + '\n')
            temp_file.write(pounds + '\n')

        description = c_file.readline()
            

    #close both files
    c_file.close()
    temp_file.close()

    #remove original file
    os.remove('coffeeInventory.txt')
    os.rename('temp.txt', 'coffeeInventory.txt')

    if found:
        print()
        print('Your selection has been removed.')
    else:
        print()
        print('Your selection was not found in the file.')

def replace_data():

    import os

    #create flag variable to determine
    #whether the search term is found in the file
    found = False
    
    #prompt user for a description to delete
    print()
    search = input('Which coffee would you like to replace?: ')
   

    #open files
    c_file = open('coffeeInventory.txt', 'r')
    temp_file = open('temp.txt', 'w')

    #search the file
    description = c_file.readline()
    while description != '':
        pounds = (c_file.readline())
        description = description.rstrip('\n')
        pounds = pounds.rstrip('\n')

        #if search term is found, change flag variable to True
        #and write the new values to the file
        if description == search:
            found = True
            print()
            new_description = input('Which new coffee would you like to replace it with?: ')
            print()
            new_pounds = input('Enter the quantity (in pounds) of the new coffee: ')
            temp_file.write(new_description + '\n')
            temp_file.write(new_pounds + '\n')
        #write all other records to the new file    
        else:
            temp_file.write(description + '\n')
            temp_file.write(pounds + '\n')

        description = c_file.readline()

    #close both files
    c_file.close()
    temp_file.close()

    #remove original file
    os.remove('coffeeInventory.txt')
    os.rename('temp.txt', 'coffeeInventory.txt')

    if found:
        print()
        print('Your selection has been replaced with the new info you provided.')
        print()
        print('Open the coffeeInventory.txt file to view the final inventory.')
    else:
        print()
        print('Your selection was not found in the file.')
            
main()
