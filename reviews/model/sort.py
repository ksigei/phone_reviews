import pandas as pd

# Load the dataset
data = pd.read_csv("./fake reviews dataset.csv")


# Filter data by category Electronics_5
electronics_data = data[data['category'] == 'Electronics_5']

# Drop the 'category' column
electronics_data = electronics_data.drop(columns=['category'])

# Save the filtered data to a new CSV file
electronics_data.to_csv("electronics_data.csv", index=False)