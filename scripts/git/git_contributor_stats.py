#!/usr/bin/env python 

import datetime
import os
import shutil
from astropy.time import Time
import astropy.units as u
from git import Repo
import pandas
import numpy as np
from scipy.ndimage import generic_filter
import tempfile 
from repos import repos


def repo_stats(repo_path):

    tempdir = tempfile.TemporaryDirectory().name

    print(f"Cloning repo...{repo_path}...")
    repo = Repo.clone_from('https://github.com/'+repo_path, os.path.join(tempdir, os.path.basename(repo_path)) )
    print("Cloned!")

    print("Analyzing...")
    first_commit_hash = repo.git.log('--pretty=format:%h', '--reverse').split('\n')[0]
    first_commit = list(repo.iter_commits(max_count=1, rev=first_commit_hash))[0]
    first_date = Time(first_commit.committed_date, format='unix')
    first_date.datetime

    stop_date = Time(datetime.datetime.now()) # Set stop date as today for now (add as argument later)
    total_days = int((stop_date - first_date).jd)
    total_days

    # ### Time ranges:

    month_bins = (
        first_date + np.arange(0, total_days, 30).astype(int) * u.day
    )

    commits_per_month = []
    for after_dt, before_dt in zip(month_bins[:-1].datetime,
                                month_bins[1:].datetime):
        count = repo.git.rev_list(['--count', '--all',
                                f'--after={after_dt:%Y-%m-%d}',
                                f'--before={before_dt:%Y-%m-%d}'])
        commits_per_month.append(int(count))


    committers_per_month = []
    for after_dt, before_dt in zip(month_bins[:-1],
                                month_bins[1:]):
        shortlog = repo.git.shortlog(
            'HEAD', s=True, n=True,
            after=f"{after_dt.datetime:%Y-%m-%d}",
            before=f"{(before_dt + 1*u.day).datetime:%Y-%m-%d}"
        )
        committers_per_month.append(len(shortlog.split('\n')))


    commits = pandas.DataFrame(zip([repo_path]*len(commits_per_month),commits_per_month,committers_per_month,month_bins[:-1].datetime), 
                            columns=['repo_name','commits','committers','month'])
    print("Done!")

    print("Writing output...")
    repo_name = repo_path.replace("/","_")
    commits.to_csv(f'out/{repo_name}_monthly_commits.csv')
    print("Done!")
    # Cleanup and remove repo directory
    print("Cleaning up...")
    shutil.rmtree(tempdir)
    print("Done!")
    

for repo in repos: 
    repo_stats(repo)
