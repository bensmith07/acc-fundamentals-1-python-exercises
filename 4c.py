#initialize the accumulating variables
#to calculate the average at the end of the program
total = 0
count = 0

#receive input from the user
#provide instructions to input sentinel value to end the program
score = float((input('Insert the next score 0-100 (or enter -1 to end): ')))

#establish sentinel value and initiate loop
while score != -1:
    
    #establish acceptable input parameters
    #prompt user to try again if they have entered an invalid value
    while (score < 0 or score > 100):
        print('***Invalid score!*** The score must be between 0-100.')
        print()
        score = float(input('Insert the next score 0-100: '))
    
    #convert score to percentage to match syllabus
    score /= 100
    
    #calculate letter grades and
    #display message to user based on their grade
    if score >= .9:
        letter_grade = 'A'
        print('With a score of,', format((score * 100), '.2f'), 'you earned a', letter_grade, 'Good work.')
        print()
    elif score >= .8 and score < .9:
        letter_grade = 'B'
        print('With a score of,', format((score * 100), '.2f'), 'you earned a', letter_grade, 'Work harder next time.')
        print()
    elif score >= .7 and score < .8:
        letter_grade = 'C'
        print('With a score of,', format((score * 100), '.2f'), 'you earned a', letter_grade, 'Work harder next time.')
        print()
    elif score >= .6 and score < .7:
        letter_grade = 'D'
        print('With a score of,', format((score * 100), '.2f'), 'you earned a', letter_grade, 'Work harder next time.')
        print()
    elif score < .6:
        letter_grade = 'F'
        print('With a score of,', format((score * 100), '.2f'), 'you earned a', letter_grade, 'Work harder next time.')
        print()
    
    #add to the accumulator variables
    #keep track of total score and number of scores entered
    #in order to calculate the average at the end of the program
    count += 1
    total += score
    
    #receive the next input value from the user
    score = float((input('Insert your score 0-100 (or enter -1 to end): ')))

if count > 0:
    #display total number of grades entered
    #calculate and display the class average
    print('Number of grades entered:', count)    
    print('Class average:', format(((total / count)*100), '.2f'))
else:
    print('You did not enter any valid scores. Please restart the program and try again.')
