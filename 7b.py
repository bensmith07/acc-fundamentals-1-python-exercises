
QTY = 12

def main():

  student_list = get_list()
  display_list(student_list)

  student_list = sort_list(student_list)
  display_list(student_list)

  student_list = rev_sort(student_list)
  display_list(student_list)

  student_list = add_name_end(student_list)
  display_list(student_list)

  student_list = add_name_beg(student_list)
  display_list(student_list)

  write_to_file(student_list)
  display_file()

  make_tuple(student_list)

def get_list():

  student_list = []
  number = 1

  while number <= QTY:
    print()
    print('Input Name #', number, ':', sep='')
    name = input('Name: ')
    student_list.append(name)
    number += 1

  return student_list

def display_list(list1):
  
  print()
  print('The names in your list are:')

  number = 1

  for name in list1:
    print()
    print(number, ': ', name, sep='')
    number += 1

def sort_list(list1):

  print()
  input('Press Enter to sort the list alphabetically:')
  list1.sort()
  return list1

def rev_sort(list1):

  print()
  input('Press Enter to reverse the order of the names in the list:')
  list1.reverse()
  return list1

def add_name_end(list1):

  print()
  input('Press enter to add the instructor\'s name to the end of the list.')
  list1.append('Rene Polanco')
  return(list1)
  
def add_name_beg(list1):

  print()
  input('Press enter to add my name to the beginning of the list.')
  list1.insert(0, 'Ben Smith')
  return list1

def write_to_file(list1):

  print()
  input('Press Enter to write the list to a file.')

  name_file = open('names.txt', 'w')

  for item in list1:
    name_file.write(item + '\n')

  name_file.close()
    
  print()
  print('Your list has been written to the file \'names.txt\'')

def display_file():

  print()
  input('Press Enter to display the contents of the file.')

  name_file = open('names.txt', 'r')

  list1 = name_file.readlines()

  name_file.close()

  index = 0
  while index < len(list1):
    list1[index] = list1[index].rstrip('\n')
    index +=1
  print()
  print('File Contents:')
  print()
  for name in list1:
    print(name)

def make_tuple(list1):

  print()
  input('Press Enter to convert your list to a tuple.')
  your_tuple = tuple(list1)
  print()
  print('Here is your tuple:')
  print(your_tuple)

main()

  
  
