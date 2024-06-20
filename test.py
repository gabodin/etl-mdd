import pandas as pd

df = pd.read_csv('/opt/trabalhos/etl-mdd/resultado/pbf-2014-2024.csv/part-00000-c0534232-3d57-4dec-bbfe-7deef949e67b-c000.csv')

# Get the number of rows in the DataFrame, which is equal to the number of lines in the CSV file
num_lines = df.shape[0]

# Print the number of lines in the CSV file
print("Number of lines in the CSV file: ", num_lines)