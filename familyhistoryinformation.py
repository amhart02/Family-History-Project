#Alayna Hart
#3/30/24
#Provide 4 activites to do with a csv file of ancestors
#Sources used: https://www.datacamp.com/tutorial/lists-python https://realpython.com/python-csv/ 

import csv 

def main():
    #create lists using csv files
    ancestor_list = ah_read_compound_list('familyhistoryinformation.csv')
    fun_fact_list = ah_read_compound_list('funfacts.csv')

    #define the variables
    activity = 0
    BIRTH_YEAR_INDEX = 2

    #create a while loop for the user to choose an activity
    while activity != 5:
        #print activity list
        print('1. Calculate an ancestors age at an event')
        print('2. Sort the list of ancestors')
        print('3. Add an ancestor to the list')
        print('4. Find a fun fact about the year an ancestor was born')
        print('5. Quit')
        #user chooses and activity
        print()
        activity = (input('Please choose an activity (Enter a number 1-5): '))
        print()
        
        #activity to calculate age at event
        if activity == '1':
            print()
            #prompt user for an ancestor name and an event
            ancestor_name = input('Please enter the first name of an ancestor you want to calculate an age for: ')
            ancestor_event = input('Please enter an event you want to calculate an age for (death, marriage, or baptism): ')
            #ensure an event was chosen
            check_ancestor = ah_search_in_list(ancestor_name, ancestor_list)
            if check_ancestor != True:
                print()
                print('Please enter a first name in the ancestor list.')
                print()
            elif ancestor_event.lower() not in ('death', 'marriage', 'baptism'):
                print()
                print('Please enter death, marriage, or baptism as the event.')
                print()
            else:
                #find ancestor information
                ancestor_information = ah_find_ancestor(ancestor_name, ancestor_list)
                #find ancestor event year
                ancestor_event_year = ah_find_ancestor_event(ancestor_information, ancestor_event)
                #ensure ancestor had the specified event
                if ancestor_event_year == '':
                    print()
                    print(f'{ancestor_name.capitalize()} did not have a {ancestor_event}.')
                    print('Please choose a different event.')
                    print()
                else:
                    #calculate age at event
                    age_at_event = ah_calculate_age(ancestor_information[BIRTH_YEAR_INDEX] , ancestor_event_year)
                    #print the age
                    print()
                    print(f'{ancestor_name.capitalize()} was {age_at_event} years old at his/her {ancestor_event}')
                    print()

        #activity to sort the list of ancestors
        elif activity == '2':
            print()
            #ask which category to sort with
            sorting_method = input('Please enter a sorting method (first name, last name, birth year, or death year): ')
            #ensure category is in the list
            if sorting_method.lower() not in ('first name', 'last name', 'birth year', 'death year'):
                print()
                print('Please enter first name, last name, birth year, or death year as a sorting method.')
                print()
            #print sorted list
            else:
                sorted_file = ah_sort_file(sorting_method, ancestor_list)
                print()
                print(f'Ancestor list sorted by {sorting_method.upper()}:')
                ah_print_ancestor_list(sorted_file)
                print()

        #activity to add an ancestor to the list
        elif activity == '3':
            print()
            #prompt user for a new ancestor information
            first_name = input('Please enter a first name: ')
            last_name = input('Please enter a last name: ')
            birth_year = input('Please enter a birth year: ')
            death_year = input('Please enter a death year: ')
            marriage_year = input('Please enter a marriage year (press enter if there is no marriage year): ')
            baptism_year = input('Please enter a baptism year (press enter if there is no baptism year): ')
            #add new ancestor to list
            ah_add_ancestor(first_name, last_name, birth_year, death_year, marriage_year, baptism_year, ancestor_list)
            #print the ancestor list with new ancestor
            print()
            ah_print_ancestor_list(ancestor_list)
            print()

        #activity to find a fun fact
        elif activity == '4':
            print()
            #prompt user for the name of an ancestor 
            ancestor_name = input('Please enter the first name of an ancestor you want a fun fact about for the year they were born: ')
            check_ancestor = ah_search_in_list(ancestor_name, ancestor_list)
            if check_ancestor != True:
                print()
                print('Please enter a first name in the ancestor list.')
                print()
            else:
                #find ancestor's information
                ancestor_information = ah_find_ancestor(ancestor_name, ancestor_list)
                #find fun fact from the fun fact file
                fun_fact = ah_find_fun_fact(ancestor_information, fun_fact_list)
                #print fun fact
                print()
                print(f'A fun fact in {ancestor_information[BIRTH_YEAR_INDEX]} is {fun_fact}')
                print()

        elif activity == '5':
            #user wants to quit
            break 

        else:
            #user did not enter a number 1-5
            print('Please enter a number 1-5.')
            print()

def ah_print_ancestor_list(list):
    """Prints the list of ancestors in a more readable way

    Parameter
        list: the list of ancestors 
    Return: the readable list of ancestors 
    """
    for line in list:
        print(', '.join(line))

def ah_find_fun_fact(ancestor_information, list):
    """Uses the birth year of the user-chosen person
    and finds the related fun fact in the funfacts.csv file

    Parameters
        ancestor_information: the chosen line of information about an ancestor
        ex. "Judy,Smith,1909,1980,1930,1909"
        list: the list of fun facts from funfacts.py
    Return: the line from the fun facts list that corresponds 
    with the birth year of chosen ancestor
    """
    birth_year = ancestor_information[2]
    for line in list:
        if line[0] == birth_year:
            return line[1]

def ah_calculate_age(birth_event, second_event):
    """Calculates the difference between two events in an ancestor's
    life and returns their age at the event

    Parameters
        birth_event: birth year from chosen ancestor
        second_event: year of chosen ancestor event
    Return: the age of the ancestor at the event 
    """
    age = int(second_event) - int(birth_event)
    return age

def ah_sort_file(sorting_type, list):
    """Based on user input, will decifer which way to sort
    the list of ancestors

    Parameters
        sorting_type: the sorting type the user chooses
        list: the list of ancestors 
    Return: a sorted list of ancestors 
    """
    if sorting_type.lower() == 'first name':
        return sorted(list, key = lambda number: number[0])
    elif sorting_type.lower() == 'last name':
        return sorted(list, key = lambda number: number [1])
    elif sorting_type.lower() == 'birth year':
        return sorted(list, key = lambda number: number[2])
    elif sorting_type.lower() == 'death year':
        return sorted(list, key = lambda number: number[3])            

def ah_add_ancestor(first, last, birth, death, marriage, baptism, list):
    """Uses each of the user's entered information about a new ancestor
    and creates a new line to append to the ancestor list

    Parameters
        first, last, birth, death, marriage, and baptism: the user-entered
        values of the new ancestor
        list: the list of ancestors 
    Return: appends the new line to the ancestor list
    """
    ancestor_information = first.capitalize() + ',' + last.capitalize() + ',' + birth + ',' + death + ',' + marriage + ',' + baptism
    split_ancestor_information = ancestor_information.split(',')
    list.append(split_ancestor_information)

def ah_find_ancestor(user_input, list):
    """Uses the first name the user gave and compares it to the list
    of ancestors to find the line containing the first name

    Parameters
        user_input: the first name of the ancestor the user entered
        list: the list of ancestors
    Return: the line from the ancestor list that corresponds 
    with the chosen ancestor 
    """
    for line in list:
        name = line[0]
        if user_input.capitalize() == name:
            return line

def ah_find_ancestor_event(line, event):
    """Finds the year of the event that the user chose 

    Parameters
        line: the line in the ancestor list which contains
        the information about the user-chosen ancestor 
        event: the event the user chose 
    Return: the year of the event of the chosen ancestor
    """
    if event.lower() == 'death':
        year = line[3]
        return year
    elif event.lower() == 'marriage':
        year = line[4]
        return year
    elif event.lower() == 'baptism':
        year = line[5]
        return year

def ah_read_compound_list(filename):
    """Reads through the csv file and makes a compound list

    Parameter
        filename: name of the csv file to be read
    Return: a compund list of the lines in the file
    """
    compound_list = []
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            compound_list.append(line)
    return compound_list

def ah_search_in_list(user_input, list):
    """Searches through the list and finds if the user input can be found in the list

    Parameters
        user_input: the first name of the chosen ancestor
        list: the list of ancestors 
    Return: true if the name was found in the list, and false if not 
    """
    user_input_found = False
    for line in list:
        if user_input.capitalize() in line:
            user_input_found = True
    return user_input_found

if __name__ == '__main__':
    main()