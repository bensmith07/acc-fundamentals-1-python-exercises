import pickle

#global constants for menu choices
SHOW_GPA = '1'
CHANGE_GPA = '2'
CHANGE_GRADE = '3'
ADD_STUDENT = '4'
PRINT_DATA = '5'
QUIT = '6'
MENU_CHOICES = ['1', '2', '3', '4', '5', '6']

#global constants for filenames
FILENAME_1 = 'students_1.dat'
FILENAME_2 = 'students_2.dat'

def main():
  add_first_five()
  mystudents_dict = load_students()
  
  #initialize menu_choice variable
  menu_choice = 0

  while menu_choice != QUIT:
    #prompt user to enter a menu choice
    menu_choice = get_menu_choice()

    #process menu choice

    #SHOW STUDENT GPA
    if menu_choice == SHOW_GPA:
      print()
      print('Show student GPA')
      print('----------------')
      name = input('Enter student name: ')
      if name in mystudents_dict:        
        print()
        print(name, '\'s GPA is: ', mystudents_dict[name].get_gpa(), sep='')
      else:
        print()
        print('Student ', name, ' not found.', sep='')

    #CHANGE STUDENT GPA
    if menu_choice == CHANGE_GPA:
      print()
      print('Change student GPA')
      print('------------------')
      name = input('Enter student name: ')
      if name in mystudents_dict:        
        print()
        print(name, '\'s current GPA is: ', mystudents_dict[name].get_gpa(), sep='')
        print()
        old_gpa = mystudents_dict[name].get_gpa()
        new_gpa = input('Enter the new GPA: ')
        mystudents_dict[name].set_gpa(new_gpa)
        print()
        print(name, '\'s GPA has been changed from ', old_gpa, ' to ', new_gpa, '.', sep='')
      else:
        print()
        print('Student ', name, ' not found.', sep='')

    #CHANGE STUDENT EXPECTED GRADE
    if menu_choice == CHANGE_GRADE:
      print()
      print('Change student\'s expected grade')
      print('--------------------------------')
      name = input('Enter student name: ')
      if name in mystudents_dict:
        print()
        print(name, '\'s current expected grade is: ', mystudents_dict[name].get_grade(), sep='')
        print()
        old_grade = mystudents_dict[name].get_grade()
        new_grade = input('Enter the new expected grade: ')
        mystudents_dict[name].set_grade(new_grade)
        print()
        print(name, '\'s expected grade has been changed from ', old_grade, ' to ', new_grade, '.', sep='')

      else:
        print()
        print('Student ', name, ' not found.', sep='')

    #ADD A NEW STUDENT
    if menu_choice == ADD_STUDENT:
      print()
      print('Add a new student')
      print('-----------------')
      name = input('Enter student name: ')
      id_num = input('Enter student ID#: ')
      gpa = input('Enter student GPA: ')
      grade = input('Enter the student\'s expected grade: ')
      status = input('Enter the student\'s status: ')
      if name in mystudents_dict:
        print()
        print('An entry for that student already exists.')
      else:
        mystudents_dict[name] = Student(name, id_num, gpa, grade, status)
        print()
        print(name, ' has been added to the database.')

    #PRINT ALL STUDENT DATA
    if menu_choice == PRINT_DATA:
      print()
      print('Here is the current student data:')
      print('---------------------------------')
      print('NAME \t\tID# \tGPA \tGrade \tStatus')
      for student in mystudents_dict:
        name = mystudents_dict[student].get_name()
        id_num = mystudents_dict[student].get_id_num()
        gpa = mystudents_dict[student].get_gpa()
        grade = mystudents_dict[student].get_grade()
        status = mystudents_dict[student].get_status()
        print(name, id_num, gpa, grade, status, sep='\t')

  #QUIT PROGRAM AND SAVE
  output_file = open(FILENAME_2, 'wb')
  pickle.dump(mystudents_dict, output_file)
  output_file.close()
  print('Your data has been saved. Goodbye.')
  

def add_first_five():

  #create 5 student objects and pass data to them
  student1 = Student('Eric Foreman', '1234', '3.0', 'B', 'full-time')
  student2 = Student('Donna Pinciotti', '1235', '3.5', 'B', 'full-time')
  student3 = Student('Michael Kelso', '1236', '1.0', 'D', 'full-time')
  student4 = Student('Steven Hyde', '1237', '2.5', 'C', 'part-time')
  student5 = Student('Jackie Burkhart', '1238', '4.0', 'A', 'full-time')

  #create an empty dictionary
  mystudents_dict = {}

  #add students to dictionary (with name as key)
  mystudents_dict['Eric Foreman'] = student1
  mystudents_dict['Donna Pinciotti'] = student2
  mystudents_dict['Michael Kelso'] = student3
  mystudents_dict['Steven Hyde'] = student4
  mystudents_dict['Jackie Burkhart'] = student5

  output_file = open(FILENAME_1, 'wb')
  pickle.dump(mystudents_dict, output_file)
  output_file.close()

def load_students():
  try:
    #open the students.dat file
    input_file = open(FILENAME_1, 'rb')
    #unpickle the dictionary
    students_dict = pickle.load(input_file)
    #close the students.dat file
    input_file.close()
  except IOError:
    #could not open the file, so create an empy dictionary
    students_dict = {}

  #return the dictionary
  return students_dict

def get_menu_choice():
  print()
  print('--------------------------------')
  input('Press Enter to display the menu: ')
  display_menu()
  print()
  menu_choice = input('Choose an action from the menu above: ')
  while menu_choice not in MENU_CHOICES:
    display_menu()
    print()
    print('Invalid selection. Must enter a number 1-6.')
    menu_choice = input('Choose an action from the menu above: ')
  return menu_choice
  

def display_menu():

  print()
  print('[1] Show student GPA.')
  print('[2] Change student GPA.')
  print('[3] Change student expected grade.')
  print('[4] Add a new student')
  print('[5] Print all student data.')
  print('[6] Quit program and save.')
  print()

class Student():

  def __init__(self, name, id_num, gpa, grade, status):
    self.__name = name
    self.__id_num = id_num
    self.__gpa = gpa
    self.__grade = grade
    self.__status = status

  def get_name(self):
    return(self.__name)

  def get_id_num(self):
    return(self.__id_num)

  def get_gpa(self):
    return(self.__gpa)

  def get_grade(self):
    return(self.__grade)

  def get_status(self):
    return(self.__status)

  def set_gpa(self, gpa):
    self.__gpa = gpa

  def set_grade(self, grade):
    self.__grade = grade

  def __str__(self):
    return 'Name: '+self.__name+', ID#: '+self.__id_num+', GPA: '+self.__gpa+', Exp. Grade: '+self.__grade+', Status: '+self.__status

main()
