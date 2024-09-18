import pandas as pd

cars = pd.read_csv('Cars_file.csv')

oddCol_only = cars.iloc[:, ::2]
problem_a = oddCol_only.head(5)

problem_b = cars.loc[cars['Model'] == 'Mazda RX4']

problem_c = cars.loc[cars['Model']== 'Camaro Z28', ['cyl']]
problem_d = cars.loc[(cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic'), ['cyl', 'gear']]

print("For a,\n\n", problem_a, "\n")
print("For b,\n\n", problem_b, "\n")
print("For c,\n\n", problem_c, "\n")
print("For d,\n\n", problem_d)