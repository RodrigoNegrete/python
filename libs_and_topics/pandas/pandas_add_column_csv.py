from csv import writer, reader
import pandas
from collections import deque

# read file
col_list = ["Name", "Department"]
df = pandas.read_csv("sample_file.csv", usecols=col_list)

# split columns
col_name = df["Name"]
print(col_name)

col_department = df["Department"]
print(col_department)

# add header
col_department = deque(col_department)
col_department.appendleft("Header")
col_department = list(col_department)
print(col_department)

# append new column


def add_column_in_csv(sample_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(sample_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


add_column_in_csv('sample_file.csv', 'output_file.csv', lambda row,
                  line_num: row.append(col_department[line_num - 1]))
