import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('Lots_of_flight_data.csv')

# 2. Display the first 7 rows of the DataFrame
print(df.head(7))

# 3. Display the last 7 rows of the DataFrame
print(df.tail(7))

# 4. Check the number of rows and columns in the DataFrame
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

# 5. List the column names of the DataFrame
print("Column names:", df.columns)

# 6. Display the summary statistics for numerical columns
print(df.describe())

# 7. Select only the 'AIR_TIME' and 'DISTANCE' columns
selected_columns = df[['AIR_TIME', 'DISTANCE']]

# 8. Find the average of the 'DISTANCE' in the DataFrame
average_distance = df['DISTANCE'].mean()
print("Average Distance:", average_distance)

# 9. Filter the DataFrame to show only rows where the 'Age' is greater than 30
filtered_df = df[df['Age'] > 30]

# 10. Sort the DataFrame in descending order based on the 'FL_DATE' column
sorted_df = df.sort_values(by='FL_DATE', ascending=False)

# 11. Find the maximum 'ARR_TIME' in the DataFrame
max_arr_time = df['ARR_TIME'].max()
print("Maximum ARR_TIME:", max_arr_time)

# 12. Calculate the total sum of the 'DISTANCE' column
total_distance = df['DISTANCE'].sum()
print("Total DISTANCE:", total_distance)

# 13. Find unique values in the 'ORIGIN' and 'DEST' columns
unique_origin = df['ORIGIN'].unique()
unique_dest = df['DEST'].unique()
print("Unique ORIGIN values:", unique_origin)
print("Unique DEST values:", unique_dest)

# 14. Count the number of occurrences of each unique value in the 'ORIGIN' column
origin_counts = df['ORIGIN'].value_counts()
print("Origin Counts:\n", origin_counts)

# 15. Create a new DataFrame with rows where 'DISTANCE' is greater than 1000
distance_greater_than_1000 = df[df['DISTANCE'] > 1000]

# 16. Save the filtered DataFrame to a new CSV file
distance_greater_than_1000.to_csv('distance_1000.csv', index=False)

# 17. Create a line plot to visualize 'AIR_TIME' and 'DISTANCE'
df[['AIR_TIME', 'DISTANCE']].plot()
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Plot')
plt.show()

# 18. Create a scatter plot to visualize the relationship between 'AIR_TIME' and 'DISTANCE'
plt.scatter(df['AIR_TIME'], df['DISTANCE'])
plt.xlabel('AIR_TIME')
plt.ylabel('DISTANCE')
plt.title('Scatter Plot')
plt.show()
