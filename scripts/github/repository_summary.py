#!/usr/bin/env python
import requests
import pandas as pd
from datetime import datetime 
from pathlib import Path
import os
from dotenv import load_dotenv
# Your GitHub personal access token
load_dotenv()
access_token =  os.getenv('REPO_TOKEN')
#print(access_token)
#Organization name
org_name = 'astropy'

# Base API endpoint for GitHub
base_url = 'https://api.github.com'

# Headers for API request
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Fetch all repositories in the given organization
response = requests.get(f'{base_url}/orgs/{org_name}/repos', headers=headers)
repos = response.json()
#print(repos)

# Create an empty DataFrame to store the repository data
# df = pd.DataFrame(columns=['repo_name', 'observation_date', 'stars', 'forks', 'open_issues'])

# Empty list to hold output for each repo
output = []
# Iterate over each repository
for repo in repos:
    print(repo['name'])
    repo_name = repo['full_name']
    observation_date = datetime.now()
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    watchers_count = repo['watchers_count']
    open_issues = repo['open_issues_count']

    # Append repository data to DataFrame
    output.append({
        'repo_name': repo_name,
        'observation_date': observation_date,
        'stars': stars,
        'forks': forks,
        'open_issues': open_issues
    })

df = pd.DataFrame.from_records(output)

df = df.sort_values(by="stars", ascending=False)

outfile = 'out/github_repodata.csv'
# Check if outfile already exists, append if it does, create if it doesn't
if Path(outfile).is_file():
    df.to_csv(outfile, mode='a', header=False, index=False)
else: 
    df.to_csv(outfile, index=False)