# DATA WRANGLING

## Description

Real-world data rarely comes clean. Using Python and its libraries, you will gather data from a 
variety of sources and in a variety of formats, assess its quality and tidiness,
then clean it. This is called data wrangling. You will document your wrangling efforts in a J
upyter Notebook, plus showcase them through analyses and visualizations using Python (and its libraries) and/or SQL.

The dataset that you will be wrangling (and analyzing and visualizing) is the tweet archive of Twitter 
user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with
a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators, 
though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. Why? Because "they're good dogs Brent."
WeRateDogs has over 4 million followers and has received international media coverage.

The twitter-archive-enhanced.csv file contains info of abt 5000 tweets, which primarily needs to be cleaned.
The predictions.tsv file contains dog breed predictions for some tweets.
The tweet_data needs to be downloaded seperately from Twitter using Tweepy API in python.

The master_dataframe contains the final result.
