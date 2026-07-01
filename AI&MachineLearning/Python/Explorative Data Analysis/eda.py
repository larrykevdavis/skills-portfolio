
# Converted at: 2026-07-01T06:15:07.938Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Importing the Required Libraries


import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# # 1. Loading the Heart Disease Dataset


heart_disease_dataframe = pd.read_csv('heart_disease_uci.csv')

heart_disease_dataframe

# # 2. Preprocessing the Dataset


# ## 2.1 Filtering By Gender to exclude all women and retain the men


#filter by gender
heart_disease_dataframe_male = heart_disease_dataframe[heart_disease_dataframe['sex']=='Male']

heart_disease_dataframe_male 

# ## 2.2 Excluding the unimportant features dataset and sex


#Exclude the dataset and sex field
heart_disease_dataframe_male=heart_disease_dataframe_male.loc[:, ~heart_disease_dataframe_male.columns.isin(['dataset','sex'])]

# ## 2.3 Replacing the boolean categorical features with binary digits 0 or 1


heart_disease_dataframe_male['exang']=heart_disease_dataframe_male['exang'].apply(lambda x: 1 if x ==True else 0)
heart_disease_dataframe_male['fbs']=heart_disease_dataframe_male['fbs'].apply(lambda x: 1 if x ==True else 0)

# ## 2.4 Encoding the categorical feature values with numerical values


# A helper function for encoding columns of the dataset with numerical values using One Hot Encoder
def hot_encoder(dataframe,column):
    encoder = OneHotEncoder()
    one_hot_array = encoder.fit_transform(dataframe[[column]]).toarray()
    one_hot_df = pd.DataFrame(one_hot_array, columns=encoder.get_feature_names_out())
    return one_hot_df

#convert categorical features into numerical features through One Hot Encoding
cp_feature=hot_encoder(heart_disease_dataframe_male ,'cp')
restecg_feature=hot_encoder(heart_disease_dataframe_male ,'restecg')
slope=hot_encoder(heart_disease_dataframe_male ,'slope')
thal=hot_encoder(heart_disease_dataframe_male ,'thal')

heart_disease_dataframe_male_categorical=cp_feature.join(restecg_feature)
heart_disease_dataframe_male_categorical=heart_disease_dataframe_male_categorical.join(slope)
heart_disease_dataframe_male_categorical=heart_disease_dataframe_male_categorical.join(thal)

heart_disease_dataframe_male_categorical

# ## 2.5 For the categorical features, drop the rows with missing values and for the numerical features impute the rows with the missing values using the mean


# A helper function for imputing missing values with the mean
def impute_nan(dataframe,column):
    dataframe[column]=dataframe[column].fillna(dataframe[column].mean())
    return dataframe

#drop missing values categorical features
heart_disease_dataframe_male_categorical=heart_disease_dataframe_male_categorical.loc[:, ~heart_disease_dataframe_male_categorical.columns.isin(['cp_nan','restecg_nan','slope_nan','thal_nan'])]


#impute by mean numerical data of the categorical features
for i in range(len(heart_disease_dataframe_male_categorical.columns)):
    heart_disease_dataframe_male_categorical=impute_nan(heart_disease_dataframe_male_categorical,heart_disease_dataframe_male_categorical.columns[i])

target=heart_disease_dataframe_male.filter(['num'],axis=1)
heart_disease_dataframe_male_numerical=heart_disease_dataframe_male.loc[:, ~heart_disease_dataframe_male.columns.isin(['cp','restecg','slope','thal','num'])]

#impute by mean numerical data of the numerical features
for i in range(len(heart_disease_dataframe_male_numerical.columns)):
    heart_disease_dataframe_male_numerical=impute_nan(heart_disease_dataframe_male_numerical,heart_disease_dataframe_male_numerical.columns[i])
# heart_disease_dataframe_male['trestbps']=heart_disease_dataframe_male['trestbps'].fillna(heart_disease_dataframe_male['trestbps'].mean())
# heart_disease_dataframe_male['chol']=heart_disease_dataframe_male['chol'].fillna(heart_disease_dataframe_male['chol'].mean())
# heart_disease_dataframe_male['thalch']=heart_disease_dataframe_male['thalch'].fillna(heart_disease_dataframe_male['thalch'].mean())
# heart_disease_dataframe_male['oldpeak']=heart_disease_dataframe_male['oldpeak'].fillna(heart_disease_dataframe_male['oldpeak'].mean())
# heart_disease_dataframe_male['ca']=heart_disease_dataframe_male['ca'].fillna(heart_disease_dataframe_male['ca'].mean())

# ## 2.6 Create the preprocessed dataset by combining the imputed numerical features with the encoded categorical features and the target field


final_heart_disease_dataframe_male=heart_disease_dataframe_male_numerical.join(heart_disease_dataframe_male_categorical)
final_heart_disease_dataframe_male=final_heart_disease_dataframe_male.join(target)

#The target value 0 indicates the abscence of a heart disease and values 1,2,3,4 indicate the presence. The dataset can therefore be transformed to a binary classification
#dataset as below
final_heart_disease_dataframe_male['num']=final_heart_disease_dataframe_male['num'].apply(lambda x: 1 if x>0 else 0)
final_heart_disease_dataframe_male=final_heart_disease_dataframe_male.dropna()


#export to csv
final_heart_disease_dataframe_male.to_csv('final_heart_disease_dataframe_male.csv', index=False)  

# # 3. Data Preparation


# ## 3.1 Isolating the target field from the features


y=final_heart_disease_dataframe_male['num']
X=final_heart_disease_dataframe_male.drop(['num'], axis=1)

# ## 3.2 Creating the training and testing datasets


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# # 4. Model


# # 4.1 Creating the Model


classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# ## 4.2 Training the model


classifier.fit(X_train, y_train)

# ## 4.3 Prediction


y_pred = classifier.predict(X_test)

# ## 4.4 Model Evaluation


ac = accuracy_score(y_test,y_pred)*100
print("Model Accuracy Score: %.2f"%(ac))