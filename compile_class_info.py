import os
import json

FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1
NET_ID_INDEX = 2
GITHUB_INDEX = 3
TEAM_INDEX = 4

def main():
    
    filenames = collect_csv_files()
    student_data, count = cat_data(filenames)
    write_csv(student_data)
    print('Number of CamelCase: %d' % count)

def collect_csv_files():
    currentDirectory = os.getcwd()
    csvFiles = [f for f in os.listdir(currentDirectory) if f.endswith('.csv')]
    return csvFiles

def cat_data(list_of_filenames):

    CamelCaseCount = 0
    allStudentData = []
    for current_file in list_of_filenames:
        if(current_file == 'mlp6.csv' or current_file == 'everyone.csv'):
            continue
        else:
            with open(current_file,'r') as rf:
                for line in rf:

                    # Check formatting:
                    if(line.startswith('#') or len(line)==1):
                       continue
                    if not line.endswith('\n'):
                        line += '\n'

                    allStudentData.append(line)
                    CamelCaseCount += write_json_check_case(line)        

    return allStudentData, CamelCaseCount

def write_csv(write_data):
    csv_filename = 'everyone.csv'
    with open(csv_filename,'w') as wf:
        for line in write_data:
            wf.write(line)

    print('Finished compiling information.')

def write_json_check_case(csv_data):
   
    # Write JSON:
    data = csv_data[:-1].split(', ')
    if(len(data)==1):
        data = csv_data[:-1].split(',')
    
    json_data = {'First name': data[FIRST_NAME_INDEX],
                 'Last name': data[LAST_NAME_INDEX],
                 'NetID': data[NET_ID_INDEX],
                 'GitHub username': data[GITHUB_INDEX],
                 'Team': data[TEAM_INDEX]}
    json_filename = json_data['NetID'] + '.json'
    with open(json_filename,'w') as wf:
        json.dump(json_data, wf)

    # Ensure CamelCase:
    if(json_data['Team'].find(' ') == -1):
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
