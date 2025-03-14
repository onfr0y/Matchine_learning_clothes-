import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#import data
reviews = pd.read_csv('reviews.csv')
 
#print column names
print(reviews.columns)
 
#print .info
print(reviews.info())

#look at the counts of recommended
print(reviews['recommended'].value_counts())
 
#create binary dictionary
binary_dict = {True:1 , False:0 }
#create rating dicitionary
rating_dict = {
    'Loved it': 5,
    'Liked it': 4,
    'Was okay': 3,
    'Not great': 2,
    'Hated it': 1
}
#creating one-hot encoding
one_hot = pd.get_dummies(reviews['department_name'])
#transform column
reviews['recommended'] = reviews['recommended'].map(binary_dict)

#transform rating 
reviews['rating'] = reviews['rating'].map(rating_dict)
 
#print your transformed column
print(reviews['recommended'].value_counts())

#print rating column
print(reviews['rating'].value_counts())

#transform department_name
print(reviews['department_name'])

#join the column back onto the original
reviews = reviews.join(one_hot)

#print column name 
print(reviews.columns)

# Replace 'actual_column_name' with the correct column name
reviews['review_date'] = pd.to_datetime(reviews['review_date'])


print(reviews['review_date'].dtype)


#get numerical columns
#get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()

#reset index
reviews = reviews.set_index('clothing_id')

scaler = StandardScaler()
scaler.fit_transform(reviews)
