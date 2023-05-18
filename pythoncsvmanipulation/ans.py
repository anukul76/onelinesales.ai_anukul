import pandas as pd
import numpy as np
# Import departments.csv into a pandas DataFrame
departments_df = pd.read_csv('ASDE Assignment - Departments (1).csv')


employees_df = pd.read_csv('ASDE Assignment - Employees (1).csv')


salaries_df = pd.read_csv('ASDE Assignment - Salaries (1).csv')

#don't know the join and group by part in pandas


orted_df = grouped_df.sort_values('amt_usd', ascending=False)



# Select the top 3 rows
top_3_departments = sorted_df.head(3)

#rename the column
top_3_departments = top_3_departments.rename(columns={'name': 'DEPT_NAME', 'amt_usd': 'AVG_MONTH_SALARY'})

#Display the result
print(top_3_departments)