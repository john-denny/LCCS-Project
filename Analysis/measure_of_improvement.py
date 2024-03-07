import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Read the CSV file using pandas
df = pd.read_csv("data.csv")

# Choose a random user
random_user = random.choice(df['Name'].unique())

# Filter the DataFrame for the selected user
user_data = df[df['Name'] == random_user]

# Plot the user's shooting against the index
plt.plot(user_data.index, (user_data[' Shots Scored'] / user_data[' Shots Taken']) * 100, marker='o', label='Shooting Accuracy')

# Linear regression
x = np.array(user_data.index)
y = np.array((user_data[' Shots Scored'] / user_data[' Shots Taken']) * 100)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='blue', label='Line of Best Fit')

plt.title(f"Shooting Performance for User: {random_user}")
plt.xlabel("Index in CSV")
plt.ylabel("Shooting Accuracy")
plt.legend()
plt.show()
