import pandas as pd

cars = pd.read_csv('Cars_file.csv')

result = pd.concat([cars.head(5), cars.tail(5)])
print(result)