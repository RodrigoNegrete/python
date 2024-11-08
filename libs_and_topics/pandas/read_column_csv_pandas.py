import pandas


col_list = ["Name", "Department"]
df = pandas.read_csv("sample_file.csv", usecols=col_list)

col_name = df["Name"]
col_department = df["Department"]

print(col_name)
print(col_department)

combined = col_name + ',' + col_department
print(combined)
