import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file
file_path = 'data.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Extracting data for the plot
happiness_before = df[' Happiness Before'].tolist()
happiness_after = df[' Happiness After'].tolist()

# Counting occurrences of each combination
combinations = list(zip(happiness_before, happiness_after))
unique_combinations = list(set(combinations))
counts = [combinations.count(comb) for comb in unique_combinations]

# Sorting unique combinations by the number of occurrences
sorted_combinations = sorted(zip(unique_combinations, counts), key=lambda x: x[1], reverse=True)

# Extracting labels and data for the plot
labels = [f'{comb[0][0]} to {comb[0][1]}' for comb in sorted_combinations]
counts = np.array([comb[1] for comb in sorted_combinations])

labels = labels[0:-4]
counts = counts[0:-4]

# Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.bar(labels, counts, color='#2596be')

# Adding labels and title
plt.title('Happiness Before vs Happiness After Playing (Sorted by Frequency)', fontsize=15, fontweight="bold")
plt.xlabel('Change in Mood Before Playing VS After')
plt.ylabel('Number of Players')

# Display the plot
plt.show()
