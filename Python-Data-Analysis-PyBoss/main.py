import os
import csv

input_file = 'employee_data.csv'
output_file = 'employee_data_finished.csv'
print(os.getcwd())

# state abbreviation library
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# input path and output paths
employee_data_path = os.path.join('.', input_file)
finished_employee_data_path = os.path.join('.', output_file)


# pull data from original employee_data file and read file
with open(employee_data_path, mode='r', newline='') as employee_data:
    reader = csv.reader(employee_data)

# skip headers before loading lists
    next(reader)

# create empty list for each row
    emp_id = []
    full_name = []
    dob = []
    ssn = []
    state = []
    first_name = []
    last_name = []
    dob_modified = []
    ssn_modified = []
    state_modified = []


# load data to original list for each row
    for i in reader:
        emp_id.append(i[0])
        full_name.append(i[1])
        dob.append(i[2])
        ssn.append(i[3])
        state.append(i[4])

# modify lists to new format

for i in range(len(dob)):
    # The Name column should be split into separate First Name and Last Name columns.
    first_name.append(full_name[i].split()[0])
    last_name.append(full_name[i].split()[1])

    from datetime import datetime
    # The DOB data should be re-written into MM/DD/YYYY format.
    str = (dob[i])
    date = datetime.strptime(str, '%Y-%m-%d').strftime('%d/%m/%Y')
    dob_modified.append(date)

    # The SSN data should be re-written such that the first five numbers are hidden from view.
    ssn_modified.append("***-**-" + ssn[i][-4:])

    # The State data should be re-written as simple two-letter abbreviations.
    state_modified.append(us_state_abbrev[state[i]])


# wrap up

# store value to new csv file
finisheddata_header = [('Employee_ID', 'First_Name', 'Last_Name', 'DOB', 'SSN', 'State')]
finisheddata_values = zip(emp_id, first_name, last_name, dob_modified, ssn_modified, state_modified)


with open(finished_employee_data_path, mode='w', newline='') as employee_data1:
    writer = csv.writer(employee_data1)

    writer.writerows(finisheddata_header)
    writer.writerows(finisheddata_values)