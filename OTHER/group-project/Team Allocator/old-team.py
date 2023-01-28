# Name: Aaliyah
# Surname: Jardien
# email: 7001758910@bootcamp.wethinkcode.co.za

#  creating a program that allocates specific users to the group project

# TOTAL STUDENTS IN LIST
def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


# FETCHING ALL DURBAN STUDENTS
def dbn_campus_students(student_list):

    # adding all durban students to the list
    dbn_students = []

    for idn in student_list:
        if ("Durban") in idn:
            dbn_students.append(idn)

    # printing outcome to check if correct
    print(dbn_students)
    return dbn_students


# FETCHING ALL CAPE TOWN STUDENTS
def cpt_campus_students(student_list):

    # adding all cape town students to list
    cpt_students = []

    for ict in student_list:
        if ("Cape Town") in ict:
            cpt_students.append(ict)

    print(cpt_students)
    return cpt_students


# FETCHING ALL JOBURG STUDENTS
def jhb_campus_students(student_list):

    jhb_students = []

    for ijb in student_list:
        if ("Johannesburg") is ijb:
            jhb_students.append(ijb)

    print(jhb_students)
    return jhb_students


# FETCHING ALL STUDENTS FROM NORTH WEST 
def nw_campus_students(student_list):
    
    # name of list
    nw_students = []

    for inw in student_list:
        if ("Phokeng") is inw:
            nw_students.append(inw)

    print(nw_students)
    return nw_students

    
def dbn_physical_students(dbn_students):


    return dbn_physical_students


def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''

    return dbn_physical_teams


def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''



def cpt_physical_students(cpt_physical_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    
    return cpt_physical_students


def cpt_physical_teams(cpt_physical_teams):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    
    return cpt_physical_teams


def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''


def jhb_physical_students(jhb_physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''

    return jhb_physical_students


def jhb_physical_teams(jhb_physical_teams):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''

    return jhb_physical_teams

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''


def nw_physical_students(nw_physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''

    return nw_physical_students


def nw_physical_teams(nw_physical_teams):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''

    return nw_physical_teams


def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []

    return virtual_campus


def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []

    return virtual_teams


def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''

# creating student list file
# using a with block to automatically close the file after using
#  "wr" - writing text mode

# create text files after all funcitions
# def student_list():
#     with open("student_list.txt", mode='wt') as file:
#         file.write('zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3\n'
#         'ddhaalJHB2022 - 2 May - Cape Town Virtual\n'
#         'thandohDBN2022 - 4 April - Phokeng Physical - seat 3\n'
#         'zaneleJHB2022 - 2 May - Durban Virtual\n'
#         'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2\n'
#         'BusiJHB2022 - 2 May - Durban Virtual\n'
#         'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1\n'
#         'CebiJHB2022 - 2 May - Durban Virtual\n'
#         'lukhona - 4 April - Phokeng Virtual\n'
#         'ddhaalJHB2022 - 2 May - Durban Physical - seat 4\n'
#         'gabiDBN2022 - 4 April - Phokeng Virtual\n'
#         'ngakithilJHB2022 - 2 May - Durban Physical - seat 5\n'
#         'zimthembilehDBN2022 - 4 April - Phokeng Virtual\n'
#         'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2\n'
#         'zimlindilehDBN2022 - 4 April - Phokeng Virtual\n'
#         'yenzileJHB2022 - 2 May - Durban Physical - seat 3\n'
#         'zimthandilehDBN2022 - 4 April - Johannesburg Virtual\n'
#         'kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1\n'
#         'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual\n'
#         'hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3\n'
#         'zizonkehDBN2022 - 4 April - Johannesburg Virtual\n'
#         'sibusisohDBN2022 - 4 April - Durban Physical - seat 2\n'
#         'kholekileDBN2022 - 4 April - Johannesburg Virtual\n'
#         'vusiDBN2022 - 4 April - Durban Physical - seat 9\n'
#         'kholelwahDBN2022 - 4 April - Johannesburg Virtual\n'
#         'zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10\n'
#         'thembelahDBN2022 - 4 April - Johannesburg Virtual\n'
#         'babazileDBN2022 - 4 April - Durban Physical - seat 11\n'
#         'thembisileDBN2022 - 4 April - Johannesburg Virtual\n'
#         'owenkosiDBN2022 - 4 April - Durban Physical - seat 8\n'
#         'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5\n'
#         'nobuhleJHB2022 - 2 May - Cape Town physical\n'
#         'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6\n'
#         'nonkonzoJHB2022 - 2 May - Cape Town Physical\n'
#         'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7\n'
#         'nombusoJHB2022 - 2 May - Cape Town Virtual\n'
#         'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4\n'
#         'nozizweJHB2022 - 2 May - Cape Town Virtual')

#     return []


if __name__ == '__main__':
    
    # # # creating & opening a file with student list names
    # text_file = open("student_list.txt", "a")

    # # #  reading content in the file
    # text_file = open("student_list.txt", "r")
    # # print(text_file.read())

    # # #  writing/adding content to the file
    # text_file = open("student_list.txt", "w")
    
    # declaring varirables of located students to add in the loop as an index
    students = student_list()

    # FETCHING ALL DURBAN STUDENTS 
    idn = dbn_campus_students(students)

    # FETCHING ALL CAPE TOWN STUDENTS
    ict = cpt_campus_students(students)

    # FETCHING ALL JOBURG STUDENTS
    ijb = jhb_campus_students(students)

    # FETCHING ALL NORTH WEST STUDENTS
    inw = nw_campus_students(students)

    #  DETCHING
    pass

    # dbn_students.write(str(i))
    # dbn_students.write('\n')