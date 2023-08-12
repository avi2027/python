import pandas as pd

student_data = {
    'StudentID' : [1552, 1553, 1554, 1555,1556,1557,1558],
    'Name' : ['John', 'Jane', 'Mary', 'Peter', 'David', 'Joseph', 'Martha'],
    'Age' : [18, 17, 18, 19, 18, 17, 18],
    'Grade' : ['A', 'B', 'D', 'A', 'A', 'C', 'B']
}

student_df = pd.DataFrame(student_data)
print(student_df)