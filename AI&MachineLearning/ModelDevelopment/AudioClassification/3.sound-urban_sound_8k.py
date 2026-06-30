# Generated from: 3.sound-urban_sound_8k.ipynb
# Converted at: 2026-06-30T19:11:42.698Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Environment Setup


import kagglehub
from pathlib import Path
import pandas as pd
import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,accuracy_score,precision_score,recall_score,f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import tensorflow as tf
import tensorflow_io as tfio
import shap
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# # 0. Downloading the Data


# Download latest version
path = kagglehub.dataset_download("chrisfilo/urbansound8k")

print("Path to dataset files:", path)

data_path=str(Path.home())+'/.cache/kagglehub/datasets/chrisfilo/urbansound8k/versions/1'

# # 1. Data Overview


audio_dataset_path=data_path+'/UrbanSound8K.csv'
audio_dataset= pd.read_csv(audio_dataset_path)

audio_dataset

# # 2. Feature Extraction


# ## 2.1 Extracting Target Labels


y=audio_dataset['classID']

# ## 2.2 Extracting MFCCs Features


def extract_mfccs(dataset):
    data_path=str(Path.home())+'/.cache/kagglehub/datasets/chrisfilo/urbansound8k/versions/1'
    
    fold=dataset['fold']
    label=dataset['class']

    audio_path=data_path+'/fold'+str(fold)+"/"+dataset['slice_file_name']
    #extract mfccs
    y, sr = librosa.load(audio_path, sr=22050, duration=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc = (mfcc - np.mean(mfcc, axis=1, keepdims=True)) / (np.std(mfcc, axis=1, keepdims=True) + 1e-6)
    max_pad_len=100
    if max_pad_len is not None:
        if mfcc.shape[1] < max_pad_len:
            # Pad the MFCCs matrix with zeros
            pad_width = max_pad_len - mfcc.shape[1]
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            # Trim if longer than max_pad_len
            mfcc = mfcc[:, :max_pad_len]
            
    return mfcc.flatten()

# Apply extraction row-by-row
audio_dataset["mfcc_features"] = audio_dataset.apply(
    lambda row: extract_mfccs(row), axis=1
)

# ## 2.3 Extracting Spectograms


def extract_spectograms(dataset):
    data_path=str(Path.home())+'/.cache/kagglehub/datasets/chrisfilo/urbansound8k/versions/1'
    
    fold=dataset['fold']
    label=dataset['class']

    audio_path=data_path+'/fold'+str(fold)+"/"+dataset['slice_file_name']
    y, sr = librosa.load(audio_path, sr=22050, duration=None)
    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    
    max_pad_len=100
    if mel_spectrogram.shape[1] < max_pad_len:
            padding = np.zeros((mel_spectrogram.shape[0], max_pad_len - mel_spectrogram.shape[1]))
            mel_spectrogram = np.concatenate((mel_spectrogram, padding), axis=1)
    else:
        mel_spectrogram = mel_spectrogram[:, :max_pad_len] 

    log_mel_spectrogram = librosa.power_to_db(mel_spectrogram+ 1e-6, ref=np.max)
    tensorflow_spectogram = tf.convert_to_tensor(log_mel_spectrogram, dtype=tf.float32)
    tensorflow_spectogram = tf.where(tf.math.is_finite(tensorflow_spectogram), tensorflow_spectogram, tf.zeros_like(tensorflow_spectogram))
    tensorflow_spectogram=tf.expand_dims(tensorflow_spectogram, axis=-1)
    
    return tensorflow_spectogram

# Apply extraction row-by-row
X_cnn =[]

for i, row in audio_dataset.iterrows():
    spec=extract_spectograms(row)
    X_cnn.append(spec)

# # 3. Data Preparation


# ## 3.1 Classical ML Models


# ### 3.1.1 Prepare the features and Target Classes


# Convert list of arrays into clean numpy array
X = np.vstack(audio_dataset["mfcc_features"].values)

# Labels
y = audio_dataset["classID"].values

# ### 3.1.2 Split the data into training and testing set


X_train,X_test,y_train,y_test=train_test_split(X,y_encoded,train_size=0.7,random_state=0)

# ### 3.1.3 Scale the Data


# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data and transform both training and testing data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ## 3.2 Deep Learning Model


# ### 3.2.1 Prepare the features and Target Classes


X_cnn=np.array(X_cnn)
y_cnn = audio_dataset["classID"].values
dataset = tf.data.Dataset.from_tensor_slices((X_cnn, y_cnn))
dataset = dataset.batch(32)

print(X_cnn.shape)

# ### 3.2.2 Split the data into training and testing set


# 2. Define split parameters (e.g., 80% train, 20% test)
DATASET_SIZE = len(X_cnn)
TRAIN_SIZE = int(0.8 * DATASET_SIZE)
SEED = 42 # for reproducible shuffling

# 3. Shuffle the entire dataset once
# Setting reshuffle_each_iteration=False ensures the split remains consistent across epochs
shuffled_dataset = dataset.shuffle(DATASET_SIZE, seed=SEED, reshuffle_each_iteration=False)

# 4. Split into training and test sets
train_dataset = shuffled_dataset.take(TRAIN_SIZE)
test_dataset = shuffled_dataset.skip(TRAIN_SIZE)

# # 4. Model Creating and Evaluation


# ## 4.1 Classical ML Models


# ## 4.1.1 Support Vector Machine Classifier


# ## 4.1.1.1 Training


SVM_Model = svm.SVC(kernel='rbf', C=1, gamma='scale')

SVM_Model.fit(X_train,y_train)

# ## 4.1.1.2 Evaluation


y_pred_SVM=SVM_Model.predict(X_test)

SVM_scores={
    'Model': 'SVM',
    'accuracy_score': accuracy_score(y_test,y_pred_SVM),
    'f1_score': f1_score(y_test,y_pred_SVM,average="macro")
}
SVM_scores

# ## 4.1.2 Random Forest Classifier


# ## 4.1.2.1 Training


RF_Model = RandomForestClassifier(n_estimators=100, random_state=42)

RF_Model.fit(X_train,y_train)

# ## 4.1.2.2 Evaluation


y_pred_RF=RF_Model.predict(X_test)

RF_scores={
    'Model': 'Random Forest',
    'accuracy_score': accuracy_score(y_test,y_pred_RF),
    'f1_score': f1_score(y_test,y_pred_RF,average="macro")
}
RF_scores

# ## 4.1.2 XGBoost


# ## 4.1.3.1 Training


XGB_Model = xgb.XGBClassifier(tree_method="hist", early_stopping_rounds=2)

XGB_Model.fit(X_train,y_train,eval_set=[(X_test, y_test)])

# ## 4.1.3.2 Evaluation


y_pred_XGB=XGB_Model.predict(X_test)

XGB_scores={
    'Model': 'XGB',
    'accuracy_score': accuracy_score(y_test,y_pred_XGB),
    'f1_score': f1_score(y_test,y_pred_XGB,average="macro")
}
XGB_scores

# ## 4.2 Deep Learning Models


# ### 4.2.1 Training the CNN Model


 # Initialize the model
model= tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', ),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the Model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

train = model.fit(train_dataset, epochs=1, batch_size=32, validation_data=test_dataset)

CNN_scores={
    'Model': 'CNN',
    'accuracy_score': 0.2065,
}
CNN_scores

# ## 4.3 Performance Comparison


data=[SVM_scores,RF_scores,XGB_scores,CNN_scores]

score_comparison=pd.DataFrame(data)

score_comparison

# ## 5 Visualizations for XGB Model


# ## 5.1 Feature Importance using SHAP


explainer = shap.TreeExplainer(XGB_Model)

shap_values = explainer.shap_values(X_test)

shap.initjs()
shap.summary_plot(shap_values, X_test)

# ## 5.2 Confusion Matrix


cm = confusion_matrix(y_test, y_pred_XGB)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix for XGBoost Model")
plt.show()

# ## 6. K-Means Clustering


K_value=5
kmeans = KMeans(n_clusters=K_value, random_state=0)
clusters = kmeans.fit_predict(X_train)
centers = kmeans.cluster_centers_

# Reduce dimensions for visualization
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(X_train)
reduced_centers = pca.transform(centers)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clusters, cmap='viridis', s=50, alpha=0.5)
plt.scatter(reduced_centers[:, 0], reduced_centers[:, 1], c='red', s=200, marker='X', label='Cluster Centers')
plt.title(f'K-Means Clustering of MFCCs (K={K_value}) visualized with PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()

# ## 7. Summary


# This notebook applies classical and deep learning models to an audio dataset. The audio dataset contains 
# audio samples organized into 10 classes
# 
# The following models have been used:
# 
# - Classical Supervised Models
#     - SVM
#     - Random Forest
#     - XgBoost
# 
# - Classical Unsupervised Models
#     -  K-Means Clustering
# 
# - Deep Learning Models
#     - Convoluted Neural Networks
# 
# The best performing classical model was the XGB Model which achieved an accuracy level of 43%. It was  found to be the most suitable algorithm for the audio classification.
# - The Feature importance visualization reveals the following analysis: Feature 3	is the most important followed by, Feature 1,0,8,5,6,9 in that order
#   
# - The confusion matrix reveals the following analysis: The model was able to correct identify Classes 3,0,9,5 and 8 with a high level of accuracy
#         
# The Convoluted neural network achieved an accuracy level of 20%
#