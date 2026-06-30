# Generated from: 4.text-fake_and_real_news(1).ipynb
# Converted at: 2026-06-30T19:12:25.645Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Environment Setup


# ## Loading Libraries


import kagglehub
import pandas as pd
import re
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,accuracy_score,precision_score,recall_score,f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from transformers import AutoTokenizer, AutoModelForSequenceClassification,Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
import shap
import numpy as np

# K-Means
from sklearn import cluster

# Visualization and Analysis
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from sklearn.metrics import silhouette_samples, silhouette_score
from wordcloud import WordCloud

# ## Downloading Dependencies


import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')

# # 0. Downloading the Dataset


path = kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset",)

print("Path to dataset files:", path)

#replace this with the printed path above
data_path=str(Path.home())+'/.cache/kagglehub/datasets/clmentbisaillon/fake-and-real-news-dataset/versions/1'

# # 1. Understanding the Data
# 
# The dataset is split into 2 datasets
# 1. Fake.csv - Containing fake news
# 2. True.csv - Containing the true news


# # 2. Loading the Data


# ## 2.1 Loading the Fake News Dataset


fakenews_data_path=data_path+'/Fake.csv'
fake_news= pd.read_csv(fakenews_data_path)

# ### 2.1.1 Data Overview


fake_news.head()

# ### 2.1.2 Assign a label (0) 


fake_news['labels']=0
fake_news.head()

# ## 2.2 Loading the True News Dataset


truenews_data_path=data_path+'/True.csv'
true_news= pd.read_csv(truenews_data_path)

# ### 2.2.1 Data Overview


true_news.head()

# ### 2.2.2 Assign a label (1) 


true_news['labels']=1
true_news.head()

# ## 2.3 Merge the Datasets into One Dataset


fake_true_df = pd.concat([fake_news, true_news], axis=0, ignore_index=True)
fake_true_df

# # 3. Data Preparation


# ## 3.1 Drop the unnecessary Fields


fake_true_df.drop(['title', 'subject','date'], axis=1, inplace=True)

fake_true_df

# ## 3.2 Isolated Target Variable from the Features


y= fake_true_df['labels']
X = fake_true_df.drop('labels', axis=1)

# ## 3.3 Data Preprocessing for Classical ML Models


# ### 3.3.1 Tokenization


def tokenize(text):
    text = text.lower() # Lowercase
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    tokens = word_tokenize(text)
    return tokens

X['tokens'] = X['text'].apply(tokenize)

# ### 3.3.2 Remove Stop words


def remove_stopwords(tokens):
    filtered_words = [word for word in tokens if word not in stop_words]
    return filtered_words
stop_words = set(stopwords.words('english'))

X['no_stop_words'] = X['tokens'].apply(remove_stopwords)

# ### 3.3.3 Perform Stemming


 def stem_tokens(tokens_no_stop_words):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens_no_stop_words]

X['tokenized_no_stop_words_stemmed'] = X['no_stop_words'].apply(stem_tokens)

# ### 3.3.4 Create the Preprocessed text string representation


X['preprocessed_text'] = X['tokenized_no_stop_words_stemmed'].apply(lambda x: ' '.join(x))

# ### 3.3.5 Perform Feature Extraction using TfidfVectorizer


vectorizer = TfidfVectorizer()
X_features = vectorizer.fit_transform(X['preprocessed_text'])

# ## 3.4 Data Preprocessing for DistilBERT Model


# ### 3.4.1 Preparing the dataset for use with DistilBert


fake_true_distilbert=fake_true_df
fake_true_distilbert

# ### 3.4.2 Truncate Column to 512 characters


fake_true_distilbert['text'] = fake_true_distilbert['text'].str[:512]

# ### 3.4.2 Split the data into a training and evaluation set


df_train, df_eval = train_test_split(
    fake_true_distilbert,
    train_size=0.8,
    stratify=fake_true_distilbert['labels'], # Stratify by label to maintain class balance
    random_state=42
)

# ### 3.4.3 Convert to Hugging Face Dataset


hf_dataset = DatasetDict({
    "train": Dataset.from_pandas(df_train, preserve_index=False),
    "eval": Dataset.from_pandas(df_eval, preserve_index=False)
})


print(hf_dataset)

# ### 3.3.3 Tokenize the text


def tokenize(df):
    return tokenizer(df['text'],truncation=True, padding=True,return_tensors='pt',max_length=512)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

hf_tokenized_datasets = hf_dataset.map(tokenize, batched=True)

# ## 3.3 Split the Data into a training and testing set


# ### 3.3.1 Classical ML Models


X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2)

# # 4. Modelling - Classical ML Models


# ## 4.1 Training and Evaluating a Logistic Regression Model


# ### 4.1.1 Training


LR_Model=LogisticRegression(solver='liblinear', random_state=42)

LR_Model.fit(X_train,y_train)

# ### 4.1.2 Evaluation


y_proba_LR=LR_Model.predict_proba(X_test)
y_pred_LR=LR_Model.predict(X_test)

LR_scores={
    'Model':'Logistic Regression',
    'roc_auc_score': roc_auc_score(y_test,y_proba_LR[:,1]),
    'accuracy_score': accuracy_score(y_test,y_pred_LR),
    'precision_score': precision_score(y_test,y_pred_LR,average="binary", pos_label=1),
    'recall_score': recall_score(y_test,y_pred_LR,average="binary", pos_label=1),
    'f1_score': f1_score(y_test,y_pred_LR,average="binary", pos_label=1)
}
LR_scores

# ## 4.2 Training and Evaluating a Naive Bayes


# ### 4.2.1 Training


MNB_Model= MultinomialNB()

MNB_Model.fit(X_train,y_train)

# ### 4.2.2 Evaluation


y_proba_MNB=MNB_Model.predict_proba(X_test)
y_pred_MNB=MNB_Model.predict(X_test)

MNB_scores={
    'Model':'Multinomial Gaussian Naive Bayes',
    'roc_auc_score': roc_auc_score(y_test,y_proba_MNB[:,1]),
    'accuracy_score': accuracy_score(y_test,y_pred_MNB),
    'precision_score': precision_score(y_test,y_pred_MNB,average="binary", pos_label=1),
    'recall_score': recall_score(y_test,y_pred_MNB,average="binary", pos_label=1),
    'f1_score': f1_score(y_test,y_pred_MNB,average="binary", pos_label=1)
}
MNB_scores

# ## 4.3  Training and Evaluating a Support Vector Machine Model - SVM


# ### 4.3.1 Training


SVM_Model = LinearSVC()

SVM_Model.fit(X_train,y_train)

# ### 4.3.2 Evaluation


y_pred_SVM=SVM_Model.predict(X_test)

SVM_scores={
    'Model':'SVM',
    'accuracy_score': accuracy_score(y_test,y_pred_SVM),
    'precision_score': precision_score(y_test,y_pred_SVM,average="binary", pos_label=1),
    'recall_score': recall_score(y_test,y_pred_SVM,average="binary", pos_label=1),
    'f1_score': f1_score(y_test,y_pred_SVM,average="binary", pos_label=1)
}
SVM_scores

# ## 4.3  Best Performing Model


data=[LR_scores,MNB_scores,SVM_scores]

score_comparison=pd.DataFrame(data)

score_comparison

# # 5. Modelling - Using a Fine tuned Transformer - DistilBERT


# ## 5.1 Initialize the Model


model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# ## 5.2 Training the Model - Fine Tuning


 training_args = TrainingArguments(
     output_dir="./results",
     num_train_epochs=1,
     per_device_train_batch_size=100,
     per_device_eval_batch_size=100,
     weight_decay=0.01,
     logging_dir="./logs",
 )

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=hf_tokenized_datasets['train'],
    eval_dataset=hf_tokenized_datasets['eval'],
    tokenizer=tokenizer,
)

trainer.train()

# ## 5.3 Evaluating the Model


# Evaluate the model
validation_results = trainer.evaluate()


distilbert_scores={
    'Model':'Distilbert',
    'accuracy_score': validation_results['eval_accuracy'],
}
distilbert_scores

# ## 5.4 Comparing Classical ML and Deep Model Performances


data=[LR_scores,MNB_scores,SVM_scores,distilbert_scores]
score_comparison=pd.DataFrame(data)
score_comparison

# ## 5.5 Model Explainability


# ## 5.5.1 Visualizing Word Importance with SHAP


# Ensure initjs is called
shap.initjs()

# Create explainer
explainer = shap.LinearExplainer(SVM_Model, X_features)

# Generate SHAP values
text_to_explain = "Pope Francis used his annual Christmas Day"
x = vectorizer.transform([text_to_explain])

# Convert sparse matrix to dense array
x_dense = x.toarray()

# Generate SHAP values for the dense array
shap_values = explainer.shap_values(x_dense)

# Visualize
shap.force_plot(explainer.expected_value, shap_values, x_dense)

# ## 5.6 K-Means Clustering


# ### 5.6.1 Generating the Clusters


max_k=9
kmeans_results = dict()

for k in range(2 , max_k):
    kmeans = cluster.KMeans(n_clusters = k, init = 'k-means++', algorithm = 'elkan')
    kmeans_results.update( {k : kmeans.fit(X_features)} )
    

# ### 5.6.2 Perform Predictions of the top 5 best clusters


# Get the clusters for the top 5 best results
best_result = 5
kmeans = kmeans_results.get(best_result)

#perform predictions
prediction = kmeans.predict(X_features)
n_feats = 5

# This notebook applies classical and deep learning models to a text data. The text dataset contains batches of true and fake news
# 
# The following models have been used:
# 
# - Classical Supervised Models
#     - SVM
#     - Naive Bayes
#     - Logistic Regression
# 
# - Classical Unsupervised Models
#     -  K-Nearest Neighbors
# 
# - Deep Learning Models
#     - Hugging Face DistilBert Model
# 
# The best performing classical model was the SVM Model which achieved an accuracy level of 99% making it the most suitable classification algorithm for this problem
# 
# The Distilbert achieved an accuracy level of 60%
# 
# 
#