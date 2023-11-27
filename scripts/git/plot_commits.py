#!/usr/bin/env python

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import glob

input_files = glob.glob("out/*monthly_commits.csv")

def make_plots(input_file, timestamp=True):

    # Load the CSV file into a DataFrame
    print(f"Reading csv...{input_file}")
    df = pd.read_csv(input_file)
    repo_name = df['repo_name'][0]
    # Convert 'month' column to datetime
    df['month'] = pd.to_datetime(df['month'])

    # Extract year from 'month' column
    df['year'] = df['month'].dt.year

    # Group the data by 'year' and calculate the sum of 'commits' and 'commiters' for each year
    yearly_stats = df.groupby('year').agg({'commits': 'sum', 'committers': 'sum'}).reset_index()
    # Get the current year's statistics
    #current_year = yearly_stats.loc[yearly_stats['year'] == pd.Timestamp.now().year]
    yearly_stats.to_csv('test.csv')    
    print("Plotting...")
    # Plotting
    fig = plt.figure()
    
    # Big subplot for common labels on graphs
    ax = fig.add_subplot(111)
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)


    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    fig.suptitle(f'Annual contributor stats {repo_name}')
    ax1.plot(yearly_stats['year'], yearly_stats['commits'], label='Total Commits')
    ax2.plot(yearly_stats['year'], yearly_stats['committers'], label='Total Commiters')
    ax1.legend()
    ax2.legend()
    #plt.scatter(current_year['year'], current_year['commits'], color='blue', label='Current Year Commits')
    #plt.scatter(current_year['year'], current_year['committers'], color='red', label='Current Year Commiters')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    if timestamp:
        plot_time =  datetime.now().strftime("%Y-%m-%d")
        ax.annotate(f'Plotted on {plot_time}', xy=(10, 10), 
                xycoords='figure pixels', size=7)
    
    out_pdf = input_file.replace(".csv",".pdf")
    print(f'Saving pdf...{out_pdf}')
    fig.savefig(out_pdf, format="pdf")
    out_svg = input_file.replace(".csv",".svg")
    print(f'Saving pdf...{out_svg}')
    fig.savefig(out_svg, format="svg")

for commit_file in input_files:
    make_plots(commit_file)
