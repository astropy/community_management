import pandas as pd 
import seaborn as sns

xlfile = 'data/2023-09-28-Facebook_Group_Insights_60 days.xlsx'

daily_numbers = pd.read_excel(xlfile,  index_col=0, sheet_name=0)
popular_days = pd.read_excel(xlfile, index_col=0, sheet_name=1)
popular_times = pd.read_excel(xlfile, index_col=0, sheet_name=2)
top_posts = pd.read_excel(xlfile, index_col=0, sheet_name=3)
member_age_gender = pd.read_excel(xlfile, index_col=0, sheet_name=4)
member_city = pd.read_excel(xlfile, index_col=0, sheet_name=5)
member_country = pd.read_excel(xlfile, index_col=0, sheet_name=6)
contributors = pd.read_excel(xlfile, index_col=0, sheet_name=7)


daily_numbers.to_csv('daily_numbers.csv')
popular_days.to_csv('popular_days.csv')
popular_times.to_csv('popular_times.csv')
top_posts.to_csv('top_posts')
member_age_gender.to_csv('member_age_gender.csv')
member_city.to_csv('member_city.csv')
member_country.to_csv('member_country.csv')
contributors.to_csv('contributors.csv')


times = popular_times.columns
graphic = sns.heatmap(popular_times, annot=True)
fig = graphic.get_figure()
fig.savefig('test.png')