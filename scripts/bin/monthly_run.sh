#!/bin/bash

# This script is to be run on the 1st of every month to run summary stats on 

# Git statistics 
cd git
# Clone and analyze monthly affiliated package data set
python3 git_contributor_stats.py
# Update annual plots
python3 plot_commits.py
cd ..
cd github
# Get stats from GitHub
python3 repository_summary.py
# Update summary table with change since last run
python3 github_summary_table.py > out/summary.md
cd ..
