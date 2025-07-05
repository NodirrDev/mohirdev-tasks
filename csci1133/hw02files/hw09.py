#Problem A: Total Time
def total_time(filename, employee):
    '''
    Purpose:
        Calculates the total number of hours an employee has worked
        during the week
    Parameter(s):
        filename: The name of the file that contains employee work hours (str)
        employee: The name of the employee to calculate total hours for (str)
    Return Value:
        Total hours worked by the employee. Returns 0.0 if employee is not found and/or -1.0 if the file doesn't exist (float)
    '''
    total_hours = 0.0
    try:
        with open(filename) as fp:
            for line in fp:
                parts = line.strip().split()
                name = parts[0]
                hours = parts[1]
                if name == employee:
                    total_hours += float(hours)
        return total_hours
    except FileNotFoundError:
        return -1.0

#Problem B: Hours to Minutes
def hours_to_minutes(filename):
    '''
    Purpose:
        Converts employee work hours into minutes, and writes the results into a new file with 'minutes_' name
    Parameter(s):
        filename: The name of the original file with hours(str)
    Return Value:
        None
    '''
    fp = open(filename)
    lines = fp.readlines()
    fp.close()

    write_file = open('minutes_' + filename, 'w')
    for line in lines:
        parts = line.strip().split()
        name = parts[0]
        hours = float(parts[1])
        minutes = hours * 60
        write_file.write(f"{name} {minutes}\n")
    write_file.close()

#Problem C: Most Populous City
def most_populous(year, region):
    '''
    Purpose:
        Returns a list of cities from a given region in a given year
    Parameter(s):
        year: The year to search for (int)
        region: The region name (str)
    Return Value:
        A list of city names that match the given year and region
    '''
    result = []
    year = str(year)

    fp = open('cities.csv')
    fp.readline()
    for line in fp:
        line = line.strip()
        parts = line.split(',')


        file_year = parts[0]
        city = parts[1]
        file_region = parts[4]

        if file_year == year and file_region == region:
                result.append(city)
    fp.close()
    return result

#Problem D: Temporal Stasis
def stasis(jump_year, jump_city):
    '''
    Purpose:
        Creates a modified copy of cities.csv where the population of a specific city is increased by 3000
    Parameter(s):
        jump_year: The year the mage jumped to (int)
        jump_city: The city the mage teleported to (str)
    Return Value:
        Number of lines in the file that were changed (int)
    '''
    counts = 0

    fp = open('cities.csv')
    fp.readline()
    lines = fp.readlines()



    write_file = open(f'{jump_year}_{jump_city}.csv', 'w')

    for line in lines:
        parts = line.strip().split(',')

        year = int(parts[0])
        city = parts[1]

        if city == jump_city and year >= jump_year:
            population = int(parts[3])
            population += 3
            parts[3] = str(population)
            counts += 1

        new_line = ','.join(parts)
        write_file.write(new_line + '\n')
    fp.close()

    write_file.close()
    return counts

if __name__ == '__main__':
    print()
    print(most_populous(1500, 'East Asia'))
    #['Beijing', 'Guangzhou', 'Hangzhou', 'Nanjing']

    print(most_populous(1673, 'Europe'))
    #['Istanbul', 'London', 'Naples', 'Paris']

    print(most_populous(1499, 'South Asia'))
    #[]

    print(most_populous(1500, 'USA'))
    #[]

















