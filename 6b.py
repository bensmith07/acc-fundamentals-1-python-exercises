NUM_OF_GRADES = 12
MIN_GRADE = 0
MAX_GRADE = 100

def main():
    input_grades()
    output_grades()

def input_grades():

    #open the file for writing
    grades_file = open('grades.txt', 'w')
    #keep track of the number of students entered
    student_num = 0

    #prompt user to enter the student's name and grade
    while student_num < NUM_OF_GRADES:
        student_num += 1
        print()
        print('Student #', student_num)
        name = input('Enter name: ')
        grade = float(input('Enter grade: '))

        #provide error message if the grade is outside the acceptable range 0-100
        try:
            if grade >= MIN_GRADE and grade <= MAX_GRADE:
                grades_file.write(name + '\n')
                grades_file.write(str(grade) + '\n')
            else:
                raise ValueError
        except ValueError:
            student_num -= 1
            print('Error: Grade must be between 0-100. Please enter a valid grade.')

    #close the file
    grades_file.close()

    #provide feedback to user
    print('Grade entry complete.')

def output_grades():

    #open the file
    try:
        grades_file = open('grades.txt', 'r')
    #if file not found, prompt user to enter the correct file name
    except FileNotFoundError:
        filename = 0
        while filename != 'grades.txt':
            print('Error: File not found.')
            filename = input('Please input the correct file name: ')
            infile = open(filename, 'r')

    print()
    print('Here are the grades you entered:')
    #read names and grades from the file and display to the user
    name = grades_file.readline()
    while name != '':
        grade = grades_file.readline()
        name = name.rstrip('\n')
        grade = grade.rstrip('\n')
        print()
        print(name)
        print(grade)
        name = grades_file.readline()

    grades_file.close
    
main()

    
        
            
            
        
    
