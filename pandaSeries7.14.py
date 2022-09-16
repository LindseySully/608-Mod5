import pandas as pd

grades = pd.Series([95,78,86])

print(f'Grade in the first index is: {grades[0]}')
print(f'The count: {grades.count()}, the mean: {grades.mean():.2f}, the minimum: {grades.min()}, the maximum: {grades.max()} and standard deviation: {grades.std():.2f}\n')
print(f'Describe is a method that produces all the stats above and more: {grades.describe()}')

#creating a series with custom indices
grades = pd.Series({'Wally': 87, 'Eva':100,'Sam':94})

#dictionary initalizers
print(f"Reviewing grades: \n Eva\'s grade: {grades['Eva']} \n Wally's grade: {grades.Wally} \n")

#the underlying array
print(f'The underlying array is: {grades.values}')

#Coded by Lindsey Sullivan