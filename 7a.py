import conversion_functions as cv

def main():
  create_FahToCel_table()
  create_GalToLit_table()
  create_PoundsToKg_table()
  create_InchesToCm_table()

#FAHRENHEIT TO CELSIUS
def create_FahToCel_table():

  #create a list of values to be converted
  f_list = list(range(-10, 101, 10))

  #create an empty list to store converted values
  c_list = []

  #create a loop to convert each element in the first list
  #using the previously written function and then append
  #the converted values to the second list
  for fahrenheit in f_list:
    c_list.append(cv.FahToCel(fahrenheit))

  #create a two dimensional list/table using the two lists
  temp_table = [f_list, c_list]

  #display the lists
  print()
  print('Fahrenheit to Celsius Table:')
  print(temp_table)

#GALLONS TO LITERS
def create_GalToLit_table():
  
  #repeat the process
  g_list = list(range(10, 101, 10))
  l_list = []
  for gallons in g_list:
        l_list.append(cv.GalToLit(gallons))
  volume_table = [g_list, l_list]
  print()
  print('Gallons to Liters Table:')
  print(volume_table)

#POUNDS TO KILOGRAMS
def create_PoundsToKg_table():

  #repeat the process
  p_list = list(range(0, 101, 10))
  k_list = []
  for pounds in p_list:
        k_list.append(cv.PoundsToKg(pounds))
  weight_table = [p_list, k_list]
  print()
  print('Pounds to Kilograms Table:')
  print(weight_table)

#INCHES TO CENTIMETERS
def create_InchesToCm_table():
  
  #repeat the process
  in_list = list(range(0, 101, 10))
  cm_list = []
  for inches in in_list:
      cm_list.append(cv.InchesToCm(inches))
  distance_table = [in_list, cm_list]
  print()
  print('Inches to Centimeters')
  print(distance_table)

main()
