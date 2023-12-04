import pandas as pd

ad_clicks = pd.read_csv("ad_clicks.csv")
#How many views (i.e., rows of the table) came from each utm_source?
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.
clicks_by_source= ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)
#pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id
clicks_by_source_pivot = clicks_by_source\
    .pivot(index ='utm_source',
       columns='is_click',
       values ='user_id').reset_index()  

#Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
clicks_by_source_pivot['percent_clicked ']= (clicks_by_source_pivot[True]/(clicks_by_source_pivot[True] + clicks_by_source_pivot[False]))
print(clicks_by_source_pivot)
# group by experimental_group and count the number of users
# check to see if a greater percentage of users clicked on Ad A or Ad B.
experimental_group_numbers = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
experimental_group_numbers_pivot = experimental_group_numbers.pivot\
(index= 'experimental_group',
 columns ='is_click',
 values='user_id').reset_index()
print(experimental_group_numbers_pivot)
#creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#calculate the percent of users who clicked on the ad by day
is_click_by_days= ad_clicks.groupby(['is_click','day']).user_id.count().reset_index()
is_click_by_days_pivot = is_click_by_days.pivot\
(index ='day',
 columns ='is_click',
 values= 'user_id').reset_index()
is_click_by_days_pivot['percentage'] = is_click_by_days_pivot[True]/(is_click_by_days_pivot[True] + is_click_by_days_pivot[False] )
print(is_click_by_days_pivot)