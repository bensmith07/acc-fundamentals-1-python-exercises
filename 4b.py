#set the number of asterisks in the top row
TOP_SIZE = 10

for r in range(TOP_SIZE, 0, -1): #establish the outer loop that determines the number of rows
    for c in range(r):           #establish the inner loop that writes each row
        print('*', end='')                  
    print()                      #move to the next line at the end of the row