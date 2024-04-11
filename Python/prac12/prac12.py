import pandas as pd

# Create a DataFrame and save it to a CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Gender': ['Female', 'Male', 'Male', 'Male']
}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# Read the CSV file
df = pd.read_csv('data.csv')

# Filter data
filtered_df = df[df['Age'] > 30]

# Sort data
sorted_df = filtered_df.sort_values(by='Age')

# Add a column
sorted_df['Status'] = ['Young' if age <= 35 else 'Old' for age in sorted_df['Age']]

# Save the results
sorted_df.to_csv('filtered_sorted_data.csv', index=False)

# Display the final results
print("Final Results:")
print(sorted_df)
