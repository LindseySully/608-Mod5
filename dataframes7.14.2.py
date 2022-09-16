import pandas as pd

grade_dictionary= {'Wally':[87,96,70], 'Eva':[100,87,90],'Sam':[94,77,90],'Katie':[100,81,82],'Bob':[83,65,85]}

grades = pd.DataFrame(grade_dictionary)

print(f'The DataFrame is: {grade_dictionary}\n')

#Customizing a DataFrames's Indices with the index Attribute

grades.index = ['Test1','Test2','Test3']
print(f'{grades}\n')

print(f"{grades['Eva']}\n")
print(f'{grades.Sam}\n')

#using loc and iloc attributes
print(f"Grades for Test 1:\n {grades.loc['Test1']}\n")
print(f'Grades for Test 2:\n {grades.iloc[1]}\n') #personally I prefer using the iloc attribute - it's easier than having to worry about the (' ') and ensuring the use of double quotes.

print(f"The result of Eva's grade on her second exam: {grades.at['Test2','Eva']}\n")
print(f"The results for Wally's third exam: {grades.iat[2, 0]}\n")

#descriptive statistics
print(f"Descriptive Statistics about the Exams:\n\n {grades.describe()}")

pd.set_option('display.precision', 2)
print(f'Descriptive Statistics with precision: \n {grades.describe()}')

#mean of each student

print(f'\n The mean of each student\'s grades:\n {grades.mean()}')

#sorting the grade book
print(f'{grades.sort_index(ascending=False)}\n')

print(f'{grades.sort_index(axis=1)}')

#Code Written by **Lindsey Sullivan** 