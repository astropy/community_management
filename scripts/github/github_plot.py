#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('out/github_repodata.csv')


# Sort the grouped data by the total number of stars in descending order
grouped_data = df.sort_values(by='stars', ascending=True)

# Set the style for the plot
plt.style.use('seaborn')

# Create a figure and axis
fig, ax = plt.subplots()

# Create arrays for the repo_name labels and the three bar groups
stars = grouped_data['stars']
forks = grouped_data['forks']
open_issues = grouped_data['open_issues']

# Compute the positions for the bars
bar_positions = range(len(grouped_data['repo_name']))

# Create the horizontal bar plots for each bar group
ax.barh(bar_positions, stars, color='r', height=0.3, label='Stars')
ax.barh(bar_positions, forks, color='g', height=0.3, label='Forks', left=stars)
ax.barh(bar_positions, open_issues, color='b', height=0.3, label='Open Issues', left=forks+stars)

# Set the y-axis ticks and labels
ax.set_yticks(bar_positions)
ax.set_yticklabels(grouped_data['repo_name'])

# Set the x-axis label
ax.set_xlabel('Count')

# Set the title
ax.set_title('Repository Statistics')

# Display the legend
ax.legend()

# Display the plot
plt.show()
