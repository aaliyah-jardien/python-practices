# Full name: Aaliyah Jardien
# Email: farcanlekker@gmail.com / 7001758910@bootcamp.wethinkcode.co.za
# Feature: Team Allocator

'''
    This is the team allocator project solution example project
'''

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


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''

    dbn_students = []
    
    # finding durban students
    for i in student_list:
        if "Durban" in i:
            dbn_students.append(i)
    
    return dbn_students
    


def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []

    #  finding cape town students
    for i in student_list:
        if "Cape Town" in i:
            cpt_students.append(i)

    # print(cpt_students)... returns 5 cape town
    return cpt_students



def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []

    for i in student_list:
        if "Johannesburg" in i:
            jhb_students.append(i)

    # print(jhb_students)
    return jhb_students



def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []

    for i in student_list:
        if "Phokeng" in i:
            nw_students.append(i)

    # print(nw_students)
    return nw_students

    
# finding physical durban students
def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical = []

    for i in dbn_students:  # fetching from durban student list only
        if "Physical" in i:
            dbn_physical.append(i)

    print(dbn_physical)

    return dbn_physical


# def dbn_physical_teams(dbn_physical_students):
#     '''
#     from the list of dbn_physical_students create list of 4 students per team, and add them to 
#     one big list
#     '''

#     return dbn_physical_teams


# def dbn_teams_file(durban_physical_teams):
#     '''
#     write and save the information in the dbn_physical_teams into a textfile
#     '''



def cpt_physical_students(cpt_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical = []

    for i in cpt_students:  # fetching from durban student list only
        if "Physical" in i:
            cpt_physical.append(i)

    print(cpt_physical)

    return cpt_physical



# def cpt_physical_teams(cpt_physical_teams):
#     '''
#     from the list of cpt_physical_students create list of 4 students per team, and add them to 
#     one big list
#     '''
    
#     return cpt_physical_teams


# def cpt_teams_file(capetown_final_teams):
#     '''
#     write and save the information in the cpt_physical_teams into a textfile
#     '''


# def jhb_physical_students(jhb_physical_students):
#     '''
#     from the list of jhb_campus_students, fill in this function to return a list of all
#     students who will be attending physically on campus
#     '''

#     return jhb_physical_students


# def jhb_physical_teams(jhb_physical_teams):
#     '''
#     from the list of jhb_physical_students create list of 4 students per team, and add them to 
#     one big list
#     '''

#     return jhb_physical_teams

# def jhb_teams_file(jhb_final_teams):
#     '''
#     write and save the information in the jhb_physical_teams into a textfile
#     '''


# def nw_physical_students(nw_physical_students):
#     '''
#     from the list of nw_campus_students, fill in this function to return a list of all
#     students who will be attending physically on campus
#     '''

#     return nw_physical_students


# def nw_physical_teams(nw_physical_teams):
#     '''
#     from the list of nw_physical_students, create list of 4 students per team, and add them to 
#     one big list
#     '''

#     return nw_physical_teams


# def nw_teams_file(nw_final_teams):
#     '''
#     write and save the information in the nw_physical_teams into a textfile
#     '''


# def get_virtual_students(student_list):
#     '''
#     from the list of students above, fill in this function to return a list of all
#     students attending virtually.
#     '''
#     virtual_campus = []

#     return virtual_campus


# def virtual_teams(virtual_students_list):
#     '''
#     from the list of virtual_students above,  create list of 4 students per team, and add them to 
#         one big list
#     '''
#     virtual_teams = []

#     return virtual_teams


# def virtual_teams_file(virtual_teams):
#     '''
#     write and save the information in the virtual_teams into a textfile
#     '''


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    # students variable stores all from student_list
    students = student_list()

    # function fetching all durban students
    dbn_students = dbn_campus_students(students)

    # function fetching all cape town students
    cpt_students = cpt_campus_students(students)

    # function fetching all joburg students
    jhb_students = jhb_campus_students(students)

    # function fetching all phokeng students
    nw_students = nw_campus_students(students)

    # function fetching all physical durban students
    dbn_physical = dbn_physical_students(dbn_students)

    # function fetching all physical cape town students
    cpt_physical = cpt_physical_students(cpt_students)


# defining function to create student list as a text file
# def student_list():
#     # creating student list file
#     f = open("student_list.txt", "w")   # writes to file

#     # writing to file
#     f.write('zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3\n' +
#         'ddhaalJHB2022 - 2 May - Cape Town Virtual\n' +
#         'thandohDBN2022 - 4 April - Phokeng Physical - seat 3\n' +
#         'zaneleJHB2022 - 2 May - Durban Virtual\n' +
#         'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2\n' +
#         'BusiJHB2022 - 2 May - Durban Virtual\n' +
#         'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1\n' +
#         'CebiJHB2022 - 2 May - Durban Virtual\n' +
#         'lukhona - 4 April - Phokeng Virtual\n' +
#         'ddhaalJHB2022 - 2 May - Durban Physical - seat 4\n' +
#         'gabiDBN2022 - 4 April - Phokeng Virtual\n' +
#         'ngakithilJHB2022 - 2 May - Durban Physical - seat 5\n' +
#         'zimthembilehDBN2022 - 4 April - Phokeng Virtual\n' +
#         'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2\n' +
#         'zimlindilehDBN2022 - 4 April - Phokeng Virtual\n' +
#         'yenzileJHB2022 - 2 May - Durban Physical - seat 3\n' +
#         'zimthandilehDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1\n' +
#         'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3\n' +
#         'zizonkehDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'sibusisohDBN2022 - 4 April - Durban Physical - seat 2\n' +
#         'kholekileDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'vusiDBN2022 - 4 April - Durban Physical - seat 9\n' +
#         'kholelwahDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10\n' +
#         'thembelahDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'babazileDBN2022 - 4 April - Durban Physical - seat 11\n' +
#         'thembisileDBN2022 - 4 April - Johannesburg Virtual\n' +
#         'owenkosiDBN2022 - 4 April - Durban Physical - seat 8\n' +
#         'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5\n' +
#         'nobuhleJHB2022 - 2 May - Cape Town physical\n' +
#         'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6\n' +
#         'nonkonzoJHB2022 - 2 May - Cape Town Physical\n' +
#         'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7\n' +
#         'nombusoJHB2022 - 2 May - Cape Town Virtual\n' +
#         'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4\n' +
#         'nozizweJHB2022 - 2 May - Cape Town Virtual')

#     f.close()

#     #open and read the file after the appending:
#     f = open("student_list.txt", "r")
#     print(f.read())

#     return []