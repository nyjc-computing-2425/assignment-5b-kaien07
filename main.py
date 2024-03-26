# Part 1
def read_csv(filename):
    """
Takes a string filename, reads CSV data stored in filename, and returns header, a list containing column labels, and data, a nested list containing data
    """
    data = []
    with open(filename, "r") as file:
        header = file.readline().split(',')
        for line in file:
            line = line.split(',')
            line[0], line[3] = int(line[0]), int(line[3])
            data.append(line)
    return header, data


# Part 2
def filter_gender(enrolment_by_age, sex):
    """
Takes a list of records enrolment_by_age and a string sex, returns a list of records where the value in the "sex" column matches string sex, and excludes sex column from returned records
    """
    search_list = []
    for elem in enrolment_by_age:
        if elem[2] == sex:
            elem.pop(2)
            search_list.append(elem)
    return search_list


# Part 3
def sum_by_year(enrolment):
    """
Takes a list of records enrolment, adds up total enrolment for each year, returns result as a list of lists, each inner list comprising of two integers, year and total_enrolment
    """
    year_list = []
    my_sum = 0
    enrolment_list = []
    for elem in enrolment:
        if elem[0] not in year_list:
            year_list.append(elem[0])
    for year in year_list:
        for elem in enrolment:
           if elem[0] == year:
               my_sum += elem[-1]
        enrolment_list.append([year, my_sum])
        my_sum = 0
    return enrolment_list

# Part 4
def write_csv(filename, header, data):
    """
Takes a string filename and two lists header and data, writes header and data to filename, and returns number of lines written   
    """
    with open(filename, 'x') as file:
        file.write(','.join(header))
        lines = 1
        file.write("\n")
        for elem in data:
            file.write(f"{','.join(str(elem1).strip() for elem1 in elem)}\n")
            lines += 1
    return lines