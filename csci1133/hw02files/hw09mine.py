# Problem A

def total_time(filename, employee):
    '''
    Purpose:
        To calculate the total hours a given employee worked in a week, knowing that
        an employee might have input his data more than once and ensuring exception handling
    Parameter(s):
        filename: (str) value that represents the name of the shared file
        that includes employees' names and hours they worked in a week
        employee: (str) name of an employee whose hours of work we need to find
    Return Value:
        (float) total number of hours an employee worked
    '''

    try:
        total_hours = 0.0
        fp = open(filename)
        for line in fp:
            list_data = line.split()
            if list_data[0] == employee:
                total_hours += float(list_data[1])
        fp.close()
        return total_hours
    except FileNotFoundError:
        return -1.0



# Problem B

def hours_to_minutes(filename):
    '''
    Purpose:
        To create a file that is the copy of given file, except the fact that
        hours are converted to minutes by multiplying by 60.
    Parameter(s):
        filename: (str) value representing name of the file
    Return Value:
        None
    '''

    fp = open(filename)
    fp_minutes = open('minutes_'+filename, 'w')
    for line in fp:
        list_data = line.split()
        list_data[1] = str(float(list_data[1]) * 60)+'\n'
        new_line = ' '.join(list_data)
        fp_minutes.write(new_line)
    fp.close()
    fp_minutes.close()



# Problem C

def most_populous(year, region):
    '''
    Purpose:
        To create a list of the most populous cities in the given year and region.
    Parameter(s):
        year: (int) value representing number of the year
        region: (str) value representing region
    Return Value:
        list of strings, list that represents cities with the criteria described
        in purpose
    '''
    cities = []
    fp = open('cities.csv')
    first_out = fp.readline()
    for line in fp:
        line = line.strip()
        data_line  = line.split(',')
        if int(data_line[0]) == year and data_line[4] == region:
            cities.append(data_line[1])
    fp.close()
    return cities


def stasis(jump_year, jump_city):
    '''
    Purpose:
    To update the population of the given jump_city after and in given jump_year
    by adding 3000 more people, in function only 3 is added because population
    is in thousands. New csv file is created with given updates. Number of lines
    altered calculated.
    Parameter(s):
        jump_year: (int) value representing a year of jumping
        jump_city: (str) value representing a city that was jumped to
    Return Value:
        (int) value representing number of lines altered
    '''

    fp = open('cities.csv')
    fp_new = open(f'{jump_year}_{jump_city}.csv', 'w')
    counter = 0
    first_line = fp.readline()
    fp_new.write(first_line)
    for line in fp:
        data_line = line.split(',')
        if data_line[1] == jump_city and int(data_line[0]) >= jump_year:
            data_line[3] = str(int(data_line[3]) + 3)
            new_line = ','.join(data_line)
            fp_new.write(new_line)
            counter += 1
        else:
            fp_new.write(line)
    fp.close()
    fp_new.close()
    return counter


























