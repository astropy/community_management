#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv('out/github_repodata.csv')

# Convert observation_date to datetime
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Sort by repo_name and observation_date
df = df.sort_values(['repo_name', 'observation_date'])

# Calculate the differences
df['diff_stars'] = df.groupby('repo_name')['stars'].diff()
df['diff_forks'] = df.groupby('repo_name')['forks'].diff()
df['diff_issues'] = df.groupby('repo_name')['open_issues'].diff()

# Get the most recent row for each repo
latest_data = df.groupby('repo_name').tail(1)


# Print the table headers
print("| Repo Name | Stars | Star Changes | Forks | Fork Changes | Issues | Issue Changes |")
print("| --- | --- | --- | --- | --- | --- | --- |")

# Iterate over the rows and print the summary
for _, row in latest_data.iterrows():
    diff_stars = f"+{row['diff_stars']}" if row['diff_stars'] > 0 else row['diff_stars']
    diff_forks = f"+{row['diff_forks']}" if row['diff_forks'] > 0 else row['diff_forks']
    diff_issues = f"+{row['diff_issues']}" if row['diff_issues'] > 0 else row['diff_issues']
    print(f"| `{row['repo_name']}` | {row['stars']} | {diff_stars} | {row['forks']} | {diff_forks} | {row['open_issues']} | {diff_issues} |")