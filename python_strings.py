# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
my_first_name = 'Devin'
#   - my_last_name
#       -set this equal to your last name
my_last_name = 'Weeks'
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
my_year_birth = 2001
#   - current_year
#       -set this equal to 2020
current_year = 2023




# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)




#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times





# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print(my_first_name, my_last_name, 'was born in', my_year_birth)


# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
print(my_first_name + '\'s' + " birth year is " + str(my_year_birth)) #
#       - tab last name current year
print("\t" , my_last_name, current_year)

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
print(my_first_name.casefold(),my_last_name.casefold()) #method
#       - length of last name
print(len(my_last_name)) #function
#       - first name and last name all in upper case
print(my_first_name.upper(), my_last_name.upper())