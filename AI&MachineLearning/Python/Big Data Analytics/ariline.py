# Generated from: ariline.ipynb
# Converted at: 2026-07-01T06:23:32.010Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Importing the Libraries


import pandas as pd
from numpy import asarray
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats
from textblob import TextBlob
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

# # 1. Loading the Data


airline_data=pd.read_csv('Airline_Review.csv')

# # 2. Exploratory Data Analysis


airline_data

airline_data.isnull().sum()

airline_data.nunique()

# # 3. Data Cleaning


# ## 3.1 Drop Rows With Missing Values


airline_data=airline_data.dropna()

# ## 3.2 Fix the Flying Month Field


#Helper Method to drop the Columns that do not contain a valid date
def validate_flying_month(flying_month_string):
    test = True
    format = "%b-%d"
    try:
        test = bool(datetime.strptime(flying_month_string, format))
    except ValueError:
        test = False
    return test

airline_data=airline_data.loc[airline_data['Flying_month'].apply(validate_flying_month) == True]

# ## 3.3 Fix the traveller_type Field


airline_data=airline_data[airline_data['Traveller_type'].str.contains("Leisure") | airline_data['Traveller_type'].str.contains("Business")]

airline_data

# ## 3.3 Fix the Class Field


airline_data=airline_data[airline_data['Class'].str.contains("Economy") | airline_data['Class'].str.contains("Business") | airline_data['Class'].str.contains("First")]

airline_data

# ## 3.4 Fix the Month Field


def extract_month(row):
    flying_month_string=row['Flying_month']
    monthlist=flying_month_string.split('-')
    return monthlist[0]

airline_data['Flying_month']=airline_data.apply(extract_month,axis=1)

airline_data

# # 4. Data Preparation


sentiment_data=airline_data[['Review_title', 'Review_content']]
airline_data.drop(['Review_title', 'Review_content','Passanger_Name'], axis=1, inplace=True)

airline_data

# # Data Analysis


# # Prediction Using Sentiment Analysis


def get_booking(row):
    booking=""
    polarity_score=row['Polarity_score']
    if polarity_score >= 0.05:
        booking=1
    elif polarity_score <= -0.05:
        booking=2
    else:
        booking=3
    return booking

sentiment_data['Polarity_score']=sentiment_data['Review_content'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

airline_data['Booking']=sentiment_data.apply(get_booking,axis=1)

airline_data

enc = OrdinalEncoder()
encoder = OneHotEncoder()
airline_data[["Traveller_type","Class", "Flying_month",'Verified']] = enc.fit_transform(airline_data[["Traveller_type","Class", "Flying_month",'Verified']])


one_hot_encoded = encoder.fit_transform(pd.DataFrame(airline_data["Route"]))

one_hot_encoded = pd.DataFrame(data = one_hot_encoded.toarray(), columns = encoder.categories_)
one_hot_encoded=one_hot_encoded.dropna()
one_hot_encoded.columns = list(map(str, one_hot_encoded.columns))

final_airline_data= pd.merge(airline_data, one_hot_encoded, left_index=True, right_index=True)
final_airline_data.columns = final_airline_data.columns.str.replace('[(,)]','') 

final_airline_data

y=final_airline_data['Booking']
X=final_airline_data.drop('Booking',axis=1)

X

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(multi_class='ovr')



def assign_month_number(row):
    month_number=-1
    flying_month_string=row['Flying_month']
    monthlist=flying_month_string.split('-')
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(months)):
        if months[i]==monthlist[0]:
            month_number=i+1
            break
    return month_number

def assign_traveller_value(row,uniquelist):
    traveller_value=0
    print(uniquelist)
    
    
   
    return traveller_value

traveller_list=list(airline_data.Traveller_type.unique())
#print(traveller_list)
airline_data['Traveller_Number']=airline_data.apply(assign_traveller_value,args=(traveller_list),axis=1)

def assign_class_value(row,dataframe):
    class_value=0
    class_type=row['Class']
    class_list=list(dataframe.Class.unique())
    
    for i in range(len(class_list)):
        if class_list[i]==class_type:
            class_value=i+1
            break
    return class_value

#valid flying_month


airline_data

airline_data['Flying_Month_Name']=airline_data.apply(extract_month,axis=1)

airline_data

airline_data['Flying_Month_Number']=airline_data.apply(assign_month_number,axis=1)

#airline_data['Traveller_Number']=airline_data.apply(assign_traveller_value,args=(airline_data),axis=1)
# airline_data['Class_Number']=airline_data.apply(assign_class_value,args=(airline_data),axis=1)

avg_rating_by_month=airline_data.groupby('Flying_Month_Name')['Rating'].mean().reset_index()

plt.figure(figsize=(10,6))
plt.plot(avg_rating_by_month['Flying_Month_Name'],avg_rating_by_month['Rating'],marker='o',linestyle='-')
plt.title('Popularity of Flight Schedule')
plt.xlabel('Flying Month')
plt.ylabel('Average Rating')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

popular_routes=airline_data[airline_data['Flying_month'].str.contains("Oct")]

avg_rating_by_route=popular_routes.groupby('Route')['Rating'].mean().reset_index()

plt.figure(figsize=(14,10))
plt.plot(avg_rating_by_route['Route'],avg_rating_by_route['Rating'],marker='o',linestyle='-')
plt.title('Popularity of Routes')
plt.xlabel('Route')
plt.ylabel('Average Rating')
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

airline_data['Flying_Month_Number']=airline_data.apply(extract_month_number,axis=1)

airline_data