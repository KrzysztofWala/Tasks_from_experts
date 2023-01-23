'''Functions gives possibility to store and load data from text files'''
from datetime import datetime

def create_files(path):
    '''Function create empty user_DB and log files

    :Parameters
        - path - path on drive to place where files will be created
    '''
    file_users="".join([path,'users_DB'])
    file_log="".join([path,'log'])
    open(file_users,"w", encoding="utf-8")
    open(file_log,"w", encoding="utf-8")

def store_users_file(users_data, path):
    '''Function store received data in users_DB file.
       Formating adjusted to the user table.

    :Parameters:
        - users_data - list which will be stored in log
        - path - path to users_DB file
    '''
    file_name="".join([path,'users_DB'])
    with open(file_name,"w", encoding="utf-8") as file:
        for line in users_data:
            pause = "".join([" "*(8-len(str(line[0])))])
            file.writelines(f'{line[0]}{pause}')
            pause = "".join([" "*(15-len(line[1]))])
            file.writelines(f'{line[1]}{pause}')
            pause = "".join([" "*(15-len(line[2]))])
            file.writelines(f'{line[2]}{pause}')
            file.writelines("\n")

def store_log_file(log_list, path):
    '''Function store received data in log file.
       Formating adjusted to the needed data in log file.

    :Parameters:
        - log_list - list which will be stored in log file
        - path - path to log file
    '''
    file_name="".join([path,'log'])
    with open(file_name,"a", encoding="utf-8") as file:
        for line in log_list:
            if len(line) == 5:
                file.writelines(f'{line[0]}     ')
                pause = "".join([" "*(8-len(line[1]))])
                file.writelines(f'{line[1]}{pause}')
                pause = "".join([" "*(15-len(line[2]))])
                file.writelines(f'{line[2]}{pause}')
                pause = "".join([" "*(15-len(line[3]))])
                file.writelines(f'{line[3]}{pause}')
                file.writelines(f'{line[4]}{pause}')
                file.writelines("\n")
            else:
                for word in line:
                    file.writelines(f'{word}     ')
                file.writelines("\n")

def data_validation(list):
    '''Function validate data

    :Parameters:
        - list - data for validation, should be 3 element list
                 correct data should should be: [int, string, string]

    :Return:
        - validation - True when data is correct
                     - False when data is incorrect
    '''
    validation = True
    try:
        int(list[0])
    except:
        validation = False
    try:
        if list[1].isalpha() is False or list[2].isalpha() is False:
            validation=False
    except:
        validation=False
    return validation

def add_records(file_name, path):
    '''Function check if records inside the file can be stored in DB.

    :Parameters:
        - file_name - name of file on drive to check
        - path - path on drive to file to check

    :Return:
        - records_to_add - list of approved records ready to store in DB
                           example: [[1, name1, lastname1,],[2, name2, lastname2,]]
        - log_list - sumarized information after file check, contain:
                        - checking date
                        - checked data
                        - feedback (Record added succesfully/Wrong input data)
                     example: [2023-01-23 17:49:40.634644     11      Piotr
                              Baginski       Record added succesfully ]
    '''
    log_list = []
    records_to_add = []
    file_name="".join([path,file_name])
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            line_list = line.split()
            if data_validation(line_list) is True:
                records_to_add.append(line.split())
                line_list.insert(0, str(datetime.now()))
                line_list.append("Record added succesfully")
                log_list.append(line_list)
            else:
                line_list.insert(0, str(datetime.now()))
                line_list.append("Wrong input data")
                log_list.append(line_list)
    return records_to_add, log_list
