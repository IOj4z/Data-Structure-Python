import pandas as pd
my_dict = {'Dave': '001', 'John': '002', 'Joe': '003'}
print(my_dict)
print(type(my_dict))

new_dict = dict()
print(new_dict)
print(type(new_dict))

new_dict = dict(Dave='001', Ava='002', Joe='003')
print(new_dict)
print(type(new_dict))

emp_details = {'Employ': {
    'Dave': {
        'ID': '001',
        'Salary': 2000,
        'Designation': 'Python Developer'
    },
    'Ava': {'ID': '002',
            'Salary': 2300,
            'Designation': 'Java Developer'
            },
    'Joe': {'ID': '003',
            'Salary': 1843,
            'Designation': 'Hadoop Developer'
            }}}
df = pd.DataFrame(emp_details['Employ'])
print(df)
print(emp_details.keys())
print(emp_details['Employ'].get('Dave'))
