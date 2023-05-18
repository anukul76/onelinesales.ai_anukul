import pandas as pd
import numpy as np

# Import departments.csv into a pandas DataFrame
departments_df= pd.read_csv('ASDE Assignment - Departments (1).csv')

# Import employees.csv into a pandas DataFrame
employees_df = pd.read_csv('ASDE Assignment - Employees (1).csv')

# Import salaries.csv into a pandas DataFrame
salaries_df = pd.read_csv('ASDE Assignment - Salaries (1).csv')
join_df = departments_df.merge(employees_df, left_on='ID', right_on='DEPT ID', suffixes=('_dept', '_emp'))
joined_df = join_df.merge(salaries_df, left_on='ID_emp', right_on='EMP_ID', suffixes=('_emp', '_sal'))
grouped_df = joined_df.groupby(['NAME_dept']).agg({'AMT (USD)': 'mean'})
sorted_df = grouped_df.sort_values('AMT (USD)', ascending=False)
top_3_departments = sorted_df.head(3)


#rename the column
top_3_departments = top_3_departments.rename(columns={'name': 'DEPT_NAME', 'amt_usd': 'AVG_MONTH_SALARY'})

#Display the result
print(top_3_departments)